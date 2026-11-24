"""Analisa SMC Scalping 30 Menit (Skema v7.0).

Alur:
  1. Bias      : struktur swing D1 dan H4 (HH/HL = bullish, LL/LH = bearish)
  2. Likuiditas: liquidity sweep di H1 (+ BOS/CHoCH setelah sweep = reversal)
  3. OB & FVG  : zona H1 yang belum dimitigasi, searah bias
  4. Retest    : harga M5 kembali menyentuh zona
  5. Entry     : candle rejection M5 (pin bar / engulfing) di dalam zona
  SL di luar zona, TP = RR 1:2.

Output memakai kontrak yang sama dengan skema sebelumnya:
keputusan, skor, alasan, level, rsi, tren.
"""
import config as C
from config import pip_size


def pivots(cs, lb):
    """Pivot terkonfirmasi: ('H', idx, harga) dan ('L', idx, harga), urut menurut index."""
    out = []
    n = len(cs)
    for i in range(lb, n - lb):
        kiri, kanan = cs[i - lb:i], cs[i + 1:i + lb + 1]
        # kiri harus strictly lebih rendah/tinggi, kanan boleh sama: hindari pivot ganda pada plateau
        if cs[i]["h"] > max(x["h"] for x in kiri) and cs[i]["h"] >= max(x["h"] for x in kanan):
            out.append(("H", i, cs[i]["h"]))
        if cs[i]["l"] < min(x["l"] for x in kiri) and cs[i]["l"] <= min(x["l"] for x in kanan):
            out.append(("L", i, cs[i]["l"]))
    return out


def _last_two(ps, kind):
    sel = [p for p in ps if p[0] == kind]
    return sel[-2:] if len(sel) >= 2 else None


def structure(cs, lb=C.SWING_LB):
    """1 = bullish (HH & HL), -1 = bearish (LL & LH), 0 = tidak jelas."""
    ps = pivots(cs, lb)
    hs, ls = _last_two(ps, "H"), _last_two(ps, "L")
    if not hs or not ls:
        return 0
    if hs[1][2] > hs[0][2] and ls[1][2] > ls[0][2]:
        return 1
    if hs[1][2] < hs[0][2] and ls[1][2] < ls[0][2]:
        return -1
    return 0


def get_bias(data):
    """D1 = trend utama, H4 = konfirmasi. Return (label, arah) dengan arah 1/-1/0."""
    h4 = structure(data["4h"])
    d1 = structure(data["1d"])
    if h4 == 1 and d1 >= 0:
        return "NAIK", 1
    if h4 == -1 and d1 <= 0:
        return "TURUN", -1
    return "SIDEWAYS", 0


def find_sweep(cs, arah):
    """Liquidity sweep di H1 dalam SWEEP_BARS candle terakhir.
    arah=1: wick menembus swing low lalu close kembali di atasnya.
    arah=-1: wick menembus swing high lalu close kembali di bawahnya."""
    n = len(cs)
    start = n - 1 - C.SWEEP_BARS
    kind = "L" if arah == 1 else "H"
    cand = [p for p in pivots(cs, C.SWING_LB) if p[0] == kind and p[1] < start]
    if not cand:
        return None
    lvl = cand[-1][2]
    for i in range(start, n):
        c = cs[i]
        if arah == 1 and c["l"] < lvl and c["c"] > lvl:
            return {"idx": i, "level": lvl}
        if arah == -1 and c["h"] > lvl and c["c"] < lvl:
            return {"idx": i, "level": lvl}
    return None


def find_bos(cs, arah, sweep_idx):
    """BOS (searah sweep) / CHoCH setelah sweep: close menembus swing sebelum sweep."""
    kind = "H" if arah == 1 else "L"
    prev = [p for p in pivots(cs, C.SWING_LB) if p[0] == kind and p[1] < sweep_idx]
    if not prev:
        return None
    lvl = prev[-1][2]
    for j in range(sweep_idx + 1, len(cs)):
        if (arah == 1 and cs[j]["c"] > lvl) or (arah == -1 and cs[j]["c"] < lvl):
            return j
    return None


def find_zones(cs, arah):
    """Zona H1 searah arah yang belum dimitigasi: FVG (3 candle) dan OB (candle lawan arah
    terakhir sebelum impuls). Return list, zona terbaru di akhir."""
    n = len(cs)
    start = max(2, n - 1 - C.ZONE_BARS)
    zones = []
    for i in range(start, n):
        a, c = cs[i - 2], cs[i]
        if arah == 1 and a["h"] < c["l"]:
            low, high, ref = a["h"], c["l"], i - 2
        elif arah == -1 and a["l"] > c["h"]:
            low, high, ref = c["h"], a["l"], i - 2
        else:
            continue
        fvg = {"kind": "FVG", "low": low, "high": high, "idx": ref}
        ob = None
        for k in range(ref, max(-1, ref - 6), -1):
            x = cs[k]
            if (arah == 1 and x["c"] < x["o"]) or (arah == -1 and x["c"] > x["o"]):
                ob = {"kind": "OB", "low": x["l"], "high": x["h"], "idx": k}
                break
        if ob:
            zones.append(ob)
        zones.append(fvg)

    valid = []
    for z in zones:
        mitigated = False
        for j in range(z["idx"] + 3, n):
            cl = cs[j]["c"]
            if (arah == 1 and cl < z["low"]) or (arah == -1 and cl > z["high"]):
                mitigated = True
                break
        if not mitigated:
            valid.append(z)
    return sorted(valid, key=lambda z: z["idx"])


def touches(c, zone):
    return c["l"] <= zone["high"] and c["h"] >= zone["low"]


def retest(m5, zone):
    return any(touches(c, zone) for c in m5[-C.RETEST_BARS:])


def rejection(m5, arah, zone):
    """Candle M5 terakhir sudah tertutup: menyentuh zona + pola rejection searah."""
    cur, prev = m5[-1], m5[-2]
    if not touches(cur, zone):
        return None
    o, c, h, l = cur["o"], cur["c"], cur["h"], cur["l"]
    body = abs(c - o)
    upper = h - max(o, c)
    lower = min(o, c) - l
    mid = (h + l) / 2
    if arah == 1:
        pin = lower >= 2 * body and c > mid
        engulf = prev["c"] < prev["o"] and c > o and o <= prev["c"] and c >= prev["o"]
        if pin:
            return "pin bar bullish"
        if engulf:
            return "bullish engulfing"
    else:
        pin = upper >= 2 * body and c < mid
        engulf = prev["c"] > prev["o"] and c < o and o >= prev["c"] and c <= prev["o"]
        if pin:
            return "pin bar bearish"
        if engulf:
            return "bearish engulfing"
    return None


def build_trade(arah, zone, entry, pair):
    """SL di luar zona + buffer, TP = RR x risiko. Return dict atau (None, alasan)."""
    pip = pip_size(pair)
    buf = C.SL_BUFFER_PIPS * pip
    if arah == 1:
        sl = zone["low"] - buf
        risk = entry - sl
    else:
        sl = zone["high"] + buf
        risk = sl - entry
    if risk <= 0:
        return None, "SL tidak valid"
    if risk > C.MAX_RISK_PIPS * pip:
        return None, f"jarak SL {risk / pip:.1f} pip melebihi batas {C.MAX_RISK_PIPS} pip"
    tp = entry + arah * C.RR * risk
    d = 5
    return {"entry": round(entry, d), "sl": round(sl, d), "tp": round(tp, d),
            "rr": C.RR, "risk_pip": round(risk / pip, 1)}, None


def evaluate(data, price, pair):
    """data: {timeframe: candles} sudah terkalibrasi. Hasil: satu keputusan BUY/SELL/NETRAL."""
    bias_label, arah = get_bias(data)
    h1, m5 = data["1h"], data["5m"]
    res = {"keputusan": "NETRAL", "skor": 0, "alasan": [], "level": None,
           "rsi": {}, "tren": bias_label}

    if arah == 0:
        res["alasan"].append("Bias D1/H4 tidak jelas (SIDEWAYS)")
        return res

    arah_txt = "BUY" if arah == 1 else "SELL"
    checks = []  # (label, lolos, wajib)

    # 1-2. Liquidity sweep + BOS/CHoCH (reversal) atau trend searah (continuation)
    sweep = find_sweep(h1, arah)
    bos = find_bos(h1, arah, sweep["idx"]) if sweep else None
    reversal = sweep is not None and bos is not None
    if reversal:
        setup = "Reversal" + (" bullish" if arah == 1 else " bearish")
        checks.append(("Ada sweep liquidity", True, True))
        checks.append(("Ada BOS/CHoCH", True, True))
    else:
        setup = "Continuation" + (" bullish" if arah == 1 else " bearish")
        checks.append(("Sweep liquidity (tidak wajib untuk continuation)", True, False))
        checks.append((f"Trend searah bias {bias_label}", True, True))

    # 3. OB/FVG H1 yang valid
    zones = find_zones(h1, arah)
    if not zones:
        checks.append(("Ada area OB/FVG", False, True))
        return _finish(res, checks, arah_txt, setup, None, None, pair)
    zone = zones[-1]
    checks.append((f"Ada area {zone['kind']} H1", True, True))

    # 4. Retest zona di M5
    checks.append(("Harga retest zona", retest(m5, zone), True))

    # 5. Konfirmasi candle rejection M5
    pola = rejection(m5, arah, zone)
    checks.append((f"Ada konfirmasi candle ({pola or 'belum ada rejection'})", pola is not None, True))

    trade = None
    if all(ok for _, ok, wajib in checks if wajib):
        entry = m5[-1]["c"]
        trade, gagal_rr = build_trade(arah, zone, entry, pair)
        if trade is None:
            checks.append((f"RR 1:{C.RR} dapat dihitung ({gagal_rr})", False, True))
        else:
            checks.append((f"RR minimal 1:{C.RR}", True, True))

    return _finish(res, checks, arah_txt, setup, zone, trade, pair)


def _finish(res, checks, arah_txt, setup, zone, trade, pair):
    wajib = [c for c in checks if c[2]]
    lolos = [c for c in wajib if c[1]]
    res["skor"] = round(100 * len(lolos) / len(wajib)) if wajib else 0
    semua_ok = len(lolos) == len(wajib)

    if zone is not None:
        res["level"] = {"type": "S" if arah_txt == "BUY" else "R",
                        "price": round((zone["low"] + zone["high"]) / 2, 5),
                        "tf": "1h"}

    if semua_ok and trade is not None:
        res["keputusan"] = arah_txt
        res["alasan"] = [f"{setup} (zona {zone['kind']} H1 {round(zone['low'], 5)}-{round(zone['high'], 5)})"]
        res["alasan"] += [lbl for lbl, ok, w in checks if ok and w]
        res["alasan"].append(f"Entry {trade['entry']} / SL {trade['sl']} / TP {trade['tp']} "
                             f"(RR 1:{trade['rr']}, risiko {trade['risk_pip']} pip)")
    else:
        belum = [lbl for lbl, ok, w in checks if w and not ok]
        res["alasan"] = [f"Belum memenuhi: {', '.join(belum) if belum else 'syarat tidak lengkap'}"]
    return res
