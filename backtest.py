"""Backtest skema final (§12): python backtest.py

Butuh BACKTEST_CACHE_DIR berisi {PAIR}_M15.csv (kolom time, open, high, low, close) untuk semua pair.
Memakai engine.analyze yang sama dengan live, bar demi bar tanpa look-ahead.

Aturan simulasi:
- Entry = close M15 bar sinyal pada pair target. Keluar = SL atau TP pertama kali kena, tanpa batas waktu.
  Jika SL dan TP kena di bar yang sama, dihitung SL.
- Biaya per trade = spread + slippage (pip), dikurangkan dari hasil.
- Batas posisi (MAKS_PER_PAIR, MAKS_TOTAL) dihitung dari trade yang belum keluar.
- Berita tidak bisa diuji (tidak ada histori kalender), diasumsikan bersih, jadi hasil cenderung optimistis.
- Tidak ada parameter yang dioptimasi.
"""
import csv
import os
import sys
from datetime import datetime, timezone

import config as C
import engine as E


# ---------------- data ----------------

def load_m15(pair):
    cache = os.environ.get("BACKTEST_CACHE_DIR", "").strip()
    if not cache:
        raise SystemExit("BACKTEST_CACHE_DIR belum diatur")
    with open(os.path.join(cache, f"{pair}_M15.csv"), encoding="utf-8", newline="") as f:
        rows = [{"t": C.to_epoch(r["time"]), "o": float(r["open"]), "h": float(r["high"]),
                 "l": float(r["low"]), "c": float(r["close"])} for r in csv.DictReader(f)]
    return sorted(rows, key=lambda x: x["t"])


def resample(m15, sec):
    """Agregasi M15 ke H4. Hanya bar yang lengkap (16 sub-bar) yang dipakai."""
    per = sec // C.TF_SEC
    groups = {}
    for c in m15:
        groups.setdefault(c["t"] - c["t"] % sec, []).append(c)
    out = []
    for key in sorted(groups):
        g = groups[key]
        if len(g) == per:
            out.append({"t": key, "o": g[0]["o"], "h": max(x["h"] for x in g),
                        "l": min(x["l"] for x in g), "c": g[-1]["c"]})
    return out


# ---------------- simulasi ----------------

def _trade(prep, i, lv, d):
    t = prep["p"][C.TARGET]
    pip = C.pip_size(C.TARGET)
    outcome, exit_i, exit_p = "BELUM SELESAI", len(prep["t"]) - 1, t["c"][-1]
    for j in range(i + 1, len(prep["t"])):
        sl_kena = t["l"][j] <= lv["sl"] if d > 0 else t["h"][j] >= lv["sl"]
        tp_kena = t["h"][j] >= lv["tp"] if d > 0 else t["l"][j] <= lv["tp"]
        if sl_kena or tp_kena:
            outcome, exit_i, exit_p = ("SL", j, lv["sl"]) if sl_kena else ("TP", j, lv["tp"])
            break
    net = d * (exit_p - lv["entry"]) / pip - (C.spread_pip(C.TARGET) + C.SLIPPAGE_PIP)
    return {"entry_i": i, "exit_i": exit_i, "waktu": prep["t"][i], "arah": "BUY" if d > 0 else "SELL",
            "pair": C.disp(C.TARGET), "hasil": outcome, "entry": lv["entry"], "sl": lv["sl"], "tp": lv["tp"],
            "sl_pip": lv["sl_pip"], "net_pip": round(net, 2), "R": round(net / lv["sl_pip"], 4)}


def run(prep, warmup=None):
    """Jalankan skema di seluruh histori. Return list trade urut waktu."""
    if warmup is None:
        warmup = max(C.CORR_WIN) + C.STAB_WIN + C.ATR_PCT_WIN   # corr_500 + stabilitas + persentil ATR
    riwayat, trades, buka = [], [], []
    for i in range(warmup, len(prep["t"]) - 1):
        buka = [x for x in buka if x["exit_i"] > i]
        d, _ = E.trigger(prep, i)
        if d == 0:                                       # cepat: analisa penuh hanya saat trigger
            continue
        posisi_pair = C.TARGET if any(x["pair"] == C.disp(C.TARGET) for x in buka) else None
        res, skor = E.analyze(prep, i, riwayat, True, posisi_pair, len(buka))
        if skor is not None:
            riwayat.append(skor)
        if res["label"].startswith("ENTRY"):
            tr = _trade(prep, i, res["levels"], d)
            trades.append(tr)
            buka.append(tr)
    return trades


# ---------------- metrik ----------------

def metrik(trades, bars):
    """Metrik §12.5 dalam R. DD% = DD_R x RISIKO_PERSEN (aproksimasi risiko tetap, tanpa bunga majemuk)."""
    n = len(trades)
    bulan = bars / (96 * 30) if bars > 0 else 0
    base = {"n": n, "wr": None, "pf": None, "exp_R": None, "total_R": 0, "dd_R": 0, "dd_persen": 0,
            "trade_per_bulan": round(n / bulan, 2) if bulan and n else 0}
    if n == 0:
        return base
    win = sum(t["R"] for t in trades if t["R"] > 0)
    loss = -sum(t["R"] for t in trades if t["R"] <= 0)
    eq = peak = dd = 0.0
    for t in trades:
        eq += t["R"]
        peak = max(peak, eq)
        dd = max(dd, peak - eq)
    return {**base, "wr": round(100 * sum(t["R"] > 0 for t in trades) / n, 1),
            "pf": round(win / loss, 3) if loss > 0 else None, "exp_R": round(eq / n, 4),
            "total_R": round(eq, 2), "dd_R": round(dd, 2), "dd_persen": round(dd * C.RISIKO_PERSEN, 2)}


def evaluasi(trades, n_bar):
    """In-sample, out-of-sample, dan walk-forward (tanpa optimasi, hanya pembagian periode)."""
    is_end, oos_end = int(n_bar * C.IS_FRAC), int(n_bar * (C.IS_FRAC + C.OOS_FRAC))

    def seg(a, b):
        return [t for t in trades if a <= t["entry_i"] < b]

    oos = seg(is_end, oos_end)
    wf, start = [], oos_end
    while start < n_bar:
        end = min(n_bar, start + C.WF_BAR)
        wf.append({"mulai": start, "selesai": end, **metrik(seg(start, end), end - start)})
        start = end
    m_oos = metrik(oos, oos_end - is_end)
    return {"in_sample": metrik(seg(0, is_end), is_end), "out_of_sample": m_oos, "walk_forward": wf,
            "kriteria": {"expectancy_oos_positif": (m_oos["exp_R"] or 0) > 0,
                         "dd_oos_di_bawah_batas": m_oos["dd_persen"] < C.DD_MAKS_PERSEN,
                         "trade_oos_cukup": m_oos["n"] >= C.TRADE_OOS_MIN,
                         "walk_forward_positif": sum((w["exp_R"] or 0) > 0 for w in wf),
                         "walk_forward_total": len(wf)}}


def tulis_md(h):
    k = h["kriteria"]
    lulus = (k["expectancy_oos_positif"] and k["dd_oos_di_bawah_batas"] and k["trade_oos_cukup"]
             and k["walk_forward_total"] > 0 and k["walk_forward_positif"] == k["walk_forward_total"])

    def fmt(m):
        if m["n"] == 0:
            return "tidak ada trade"
        return (f"n {m['n']} · WR {m['wr']}% · PF {m['pf']} · exp {m['exp_R']}R · total {m['total_R']}R · "
                f"DD {m['dd_R']}R (~{m['dd_persen']}%) · {m['trade_per_bulan']} trade/bulan")

    lines = ["# Backtest Skema Final", "", f"- Periode: {h['periode']} · bar M15: {h['bar']}",
             f"- Biaya: spread {C.spread_pip(C.TARGET)} pip + slippage {C.SLIPPAGE_PIP} pip",
             "- **Berita tidak diuji**: hasil cenderung optimistis. Tidak ada parameter yang dioptimasi.", "",
             f"## In-sample (60%, hanya dicatat)\n- {fmt(h['in_sample'])}", "",
             f"## Out-of-sample (20% berikutnya)\n- {fmt(h['out_of_sample'])}", "",
             "## Walk-forward (uji 3 bulan)", "", "| Mulai bar | Selesai bar | Hasil |", "|---|---|---|"]
    lines += [f"| {w['mulai']} | {w['selesai']} | {fmt(w)} |" for w in h["walk_forward"]]
    lines += ["", "## Kriteria lulus (§12.7)", "",
              f"- Expectancy OOS positif: {k['expectancy_oos_positif']}",
              f"- DD OOS < {C.DD_MAKS_PERSEN}%: {k['dd_oos_di_bawah_batas']}",
              f"- Trade OOS >= {C.TRADE_OOS_MIN}: {k['trade_oos_cukup']}",
              f"- Walk-forward positif: {k['walk_forward_positif']} dari {k['walk_forward_total']}", "",
              f"**Hasil: {'LULUS' if lulus else 'GAGAL, ulangi desain sebelum live (§15.6)'}**"]
    return "\n".join(lines) + "\n"


def main():
    raw = {pair: load_m15(pair) for pair in C.PAIRS}
    prep = E.build(raw, resample(raw[C.PEMICU], C.TF_H4_SEC))
    trades = run(prep)
    n = len(prep["t"])
    h = {"periode": f"{datetime.fromtimestamp(prep['t'][0], timezone.utc):%Y-%m-%d} s/d "
                    f"{datetime.fromtimestamp(prep['t'][-1], timezone.utc):%Y-%m-%d}",
         "bar": n, **evaluasi(trades, n)}
    C.save_json("database/backtest_hasil.json", h)
    os.makedirs("reports", exist_ok=True)
    with open("reports/backtest.md", "w", encoding="utf-8") as f:
        f.write(tulis_md(h))
    print(f"Backtest selesai: {h['out_of_sample']['n']} trade OOS -> reports/backtest.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())
