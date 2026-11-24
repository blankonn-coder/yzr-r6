"""Simulasi trade bar-per-bar (tahap 3).

Aturan dasar:
- Sinyal dihitung dari bar i-1 yang sudah close (mid). Entry di open bar i.
- LONG masuk di ASK, keluar di BID. SHORT masuk di BID, keluar di ASK.
- Slippage (slip_pip) hanya diterapkan pada fill pasar (entry dan exit berbasis close).
- Bila SL dan TP tersentuh pada bar yang sama, SL dianggap lebih dulu (konservatif).
- Gap melewati SL dieksekusi di harga open (lebih buruk dari SL).
- Satu posisi per pair per metode. Cooldown dihitung dari bar exit.
"""
import numpy as np

# Parameter per metode (dari skema, usulan tahap 2 yang disetujui)
PARAMS = {
    "A": {"rr": 1.5, "cooldown": 2},
    "B": {"rr": 2.0, "cooldown": 5},
    "C": {"rr": 2.0, "cooldown": 3},
    "D": {"rr": 1.5, "cooldown": 2},
    "E": {"rr": 2.0, "cooldown": 3},
}


def _trail(nama, pos, i, hi, lo, mc, ind, pip):
    s, e, risk = pos["dir"], pos["entry"], pos["risk"]
    fav = (hi - e) if s == 1 else (e - lo)
    if fav >= risk:
        pos["be"] = True
    if not pos["be"]:
        return
    if s == 1:
        if nama == "A":
            pos["sl"] = max(pos["sl"], e + 2 * pip)
        elif nama in ("C", "E"):
            pos["sl"] = max(pos["sl"], e)
        elif nama == "B":
            pos["sl"] = max(pos["sl"], ind["ema50"][i])
        if nama == "C":
            pos["ext"] = max(pos["ext"], hi)
            pos["sl"] = max(pos["sl"], pos["ext"] - 0.5 * ind["atr14"][i])
    else:
        if nama == "A":
            pos["sl"] = min(pos["sl"], e - 2 * pip)
        elif nama in ("C", "E"):
            pos["sl"] = min(pos["sl"], e)
        elif nama == "B":
            pos["sl"] = min(pos["sl"], ind["ema50"][i])
        if nama == "C":
            pos["ext"] = min(pos["ext"], lo)
            pos["sl"] = min(pos["sl"], pos["ext"] + 0.5 * ind["atr14"][i])


def _exit_close(nama, pos, i, mc, ind):
    """Aturan keluar berbasis close bar i. Return alasan atau None."""
    s = pos["dir"]
    bars = i - pos["i0"]
    if nama == "A" and 1 <= bars <= 2:
        f = ind["fisher9"][i]
        if (s == 1 and f < -1.5) or (s == -1 and f > 1.5):
            return "Fisher kembali ke ekstrem"
    if nama == "B" and 1 <= bars <= 3:
        if (s == 1 and mc < ind["ema50"][i]) or (s == -1 and mc > ind["ema50"][i]):
            return "close kembali melewati EMA50"
    if nama == "C" and bars >= 2:
        h0, h1, h2 = ind["macd_hist"][i], ind["macd_hist"][i - 1], ind["macd_hist"][i - 2]
        if s == 1 and h2 > 0 and h2 > h1 > h0 and h0 <= 0:
            return "histogram mengecil dan berbalik"
        if s == -1 and h2 < 0 and h2 < h1 < h0 and h0 >= 0:
            return "histogram mengecil dan berbalik"
    if nama == "D":
        k = ind["stoch_k"][i]
        if (s == 1 and k >= 50) or (s == -1 and k <= 50):
            return "Stochastic kembali ke 50"
        if (s == 1 and mc < ind["ma200"][i]) or (s == -1 and mc > ind["ma200"][i]):
            return "close menembus MA200 berlawanan"
        if bars >= 4:
            return "time stop 4 jam"
    if nama == "E" and 1 <= bars <= 2:
        if (s == 1 and mc < ind["bb_upper"][i]) or (s == -1 and mc > ind["bb_lower"][i]):
            return "false breakout"
    return None


def simulate(nama, sig, bid, ask, mid, ind, pip, slip_pip=0.3, entry_ok=None):
    """sig: DataFrame kolom direction (int) dan sl_dist (float), indeks 0..n-1.
    bid/ask/mid: DataFrame kolom open, high, low, close (panjang sama dengan sig).
    ind: DataFrame indikator (lihat indicators.build) dengan indeks 0..n-1.
    Return (trades, jumlah_posisi_terbuka_di_akhir)."""
    p = PARAMS[nama]
    n = len(sig)
    d = sig["direction"].to_numpy(int)
    sld = sig["sl_dist"].to_numpy(float)
    bo, bh, bl, bc = (bid[c].to_numpy(float) for c in ("open", "high", "low", "close"))
    ao, ah, al, ac = (ask[c].to_numpy(float) for c in ("open", "high", "low", "close"))
    mc = mid["close"].to_numpy(float)
    slip = slip_pip * pip
    if entry_ok is None:
        entry_ok = np.ones(n, dtype=bool)
    ind = {c: ind[c].to_numpy(float) for c in ind.columns}

    trades = []
    pos = None
    cool_until = -1
    for i in range(1, n):
        if pos is None and i > cool_until and d[i - 1] != 0 and np.isfinite(sld[i - 1]) and entry_ok[i]:
            s, dist = int(d[i - 1]), float(sld[i - 1])
            if s == 1:
                e = ao[i] + slip
                sl, tp = e - dist, e + p["rr"] * dist
            else:
                e = bo[i] - slip
                sl, tp = e + dist, e - p["rr"] * dist
            pos = {"dir": s, "entry": e, "sl": sl, "tp": tp, "risk": dist, "i0": i,
                   "be": False, "ext": e}
        if pos is None:
            continue

        s = pos["dir"]
        if s == 1:
            hi, lo, opn = bh[i], bl[i], bo[i]
        else:
            hi, lo, opn = ah[i], al[i], ao[i]

        exit_p, alasan = None, None
        if s == 1:
            if lo <= pos["sl"]:
                exit_p, alasan = min(pos["sl"], opn), "SL"
            elif hi >= pos["tp"]:
                exit_p, alasan = pos["tp"], "TP"
        else:
            if hi >= pos["sl"]:
                exit_p, alasan = max(pos["sl"], opn), "SL"
            elif lo <= pos["tp"]:
                exit_p, alasan = pos["tp"], "TP"

        if exit_p is None:
            _trail(nama, pos, i, hi, lo, mc[i], ind, pip)
            alasan = _exit_close(nama, pos, i, mc[i], ind)
            if alasan is not None:
                exit_p = (bc[i] - slip) if s == 1 else (ac[i] + slip)

        if exit_p is not None:
            e = pos["entry"]
            trades.append({
                "dir": s, "entry_i": pos["i0"], "exit_i": i, "sig_i": pos["i0"] - 1,
                "entry": e, "exit": exit_p, "sl": pos["sl"], "tp": pos["tp"], "risk": pos["risk"],
                "r": (exit_p - e) * s / pos["risk"],
                "pips": (exit_p - e) * s / pip,
                "reason": alasan, "bars": i - pos["i0"],
            })
            cool_until = i + p["cooldown"]
            pos = None
    return trades, (1 if pos is not None else 0)
