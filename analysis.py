"""Analisa per pair: bangun konteks, tentukan regime, lalu cek trigger metode PRIORITAS."""
import bisect

import config as C
import regime as R
from indicators import compute
from strategies import REGISTRY

DIR_TXT = {1: "LONG", -1: "SHORT"}
BIAS_TXT = {1: "NAIK", -1: "TURUN", 0: "SIDEWAYS"}


def bias_series(h1_times, h4_times, h4_ind):
    """Bias H4 (EMA50 vs EMA200) untuk tiap bar H1 memakai bar H4 yang sudah TUTUP.

    Bar H4 dibuka di ht dan tutup di ht+4j. Bar H1 dibuka di t dan tutup di t+1j,
    jadi bar H4 valid jika ht <= t-3j.
    """
    sign = []
    for a, b in zip(h4_ind["ema50"], h4_ind["ema200"]):
        if a is None or b is None:
            sign.append(None)
        else:
            sign.append(1 if a > b else -1 if a < b else 0)
    out = []
    for t in h1_times:
        j = bisect.bisect_right(h4_times, t - 3 * 3600) - 1
        out.append(sign[j] if j >= 0 and sign[j] is not None else 0)
    return out


def build(h1, h4):
    ind4 = compute(h4)
    ind1 = compute(h1)
    bias = bias_series([c["t"] for c in h1], [c["t"] for c in h4], ind4)
    return {"cs": h1, "ind": ind1, "bias": bias, "closes": [c["c"] for c in h1]}


def evaluate(ctx, pair, ranking, news_bersih):
    """news_bersih: True = tidak ada news, False = ada news, None = kalender gagal."""
    cs = ctx["cs"]
    i = len(cs) - 1
    reg = R.classify(ctx["ind"], i, ctx["closes"])
    out = {"regime": reg["label"], "bias": BIAS_TXT[ctx["bias"][i]], "label": "NO TRADE",
           "metode": None, "arah": None, "harga": round(cs[i]["c"], 5),
           "entry": None, "sl": None, "tp": None, "catatan": []}

    kandidat = ranking.get((pair, reg["label"]), [])
    if not kandidat:
        out["catatan"].append(f"tidak ada metode PRIORITAS untuk regime {reg['label']}")
        return out

    picked = None
    for c in kandidat:
        strat = REGISTRY[c["metode"]]
        s = strat.signal(ctx, i)
        if s == 0 or DIR_TXT[s] != c["arah"]:
            continue
        d = strat.sl_dist(ctx, i, pair)
        if not d:
            out["catatan"].append(f"{c['metode']}: SL tidak bisa dihitung")
            continue
        picked = (c, s, d, strat)
        break

    if picked is None:
        out["label"] = "WATCHLIST"
        out["catatan"].append("trigger belum terpenuhi untuk: " + ", ".join(
            f"{c['metode']} {c['arah']}" for c in kandidat))
        return out

    c, s, d, strat = picked
    price = cs[i]["c"]
    out.update(metode=c["metode"], arah=DIR_TXT[s], entry=round(price, 5),
               sl=round(price - s * d, 5), tp=round(price + s * strat.TP_R * d, 5))
    if news_bersih is None:
        out["label"] = "WATCHLIST"
        out["catatan"].append("kalender gagal diperiksa: tidak ada ENTRY baru")
    elif not news_bersih:
        out["label"] = "WATCHLIST"
        out["catatan"].append("ada news high-impact dalam ±30 menit")
    elif not C.SPREAD_TERSEDIA:
        out["label"] = "WATCHLIST"
        out["catatan"].append("spread belum terverifikasi (OANDA belum tersambung)")
    else:
        out["label"] = f"ENTRY {DIR_TXT[s]}"
    return out
