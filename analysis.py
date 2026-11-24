"""Analisa per pair: bangun konteks, tentukan regime, lalu cek trigger metode PRIORITAS.

Label:
  ENTRY LONG/SHORT : trigger ada, tidak ada news, dan spread terverifikasi. Entry/SL/TP diisi.
  WATCHLIST        : metode ada, tetapi belum boleh entry. Status menjelaskan alasannya.
  NO TRADE         : regime ini belum punya metode prioritas di ranking.
Entry/SL/TP hanya diisi untuk ENTRY. Untuk WATCHLIST tidak ada harga rencana.
"""
import bisect

import config as C
import regime as R
from indicators import compute
from strategies import REGISTRY

DIR_TXT = {1: "LONG", -1: "SHORT"}
BIAS_TXT = {1: "NAIK", -1: "TURUN", 0: "SIDEWAYS", None: "BELUM SIAP"}


def bias_series(h1_times, h4_times, h4_ind):
    """Bias H4 (EMA50 vs EMA200) untuk tiap bar H1 memakai bar H4 yang sudah TUTUP.

    Bar H4 dibuka di ht dan tutup di ht+4j. Bar H1 dibuka di t dan tutup di t+1j,
    jadi bar H4 valid jika ht <= t-3j. None = belum bisa dihitung, bukan sideways.
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
        out.append(sign[j] if j >= 0 else None)
    return out


def build(h1, h4):
    ind4 = compute(h4)
    ind1 = compute(h1)
    bias = bias_series([c["t"] for c in h1], [c["t"] for c in h4], ind4)
    return {"cs": h1, "ind": ind1, "bias": bias, "closes": [c["c"] for c in h1], "n_h4": len(h4)}


def evaluate(ctx, pair, ranking, news_bersih):
    """news_bersih: True = tidak ada news, False = ada news, None = kalender gagal."""
    cs = ctx["cs"]
    i = len(cs) - 1
    reg = R.classify(ctx["ind"], i, ctx["closes"])
    bias_val = ctx["bias"][i]
    price = round(cs[i]["c"], 5)
    out = {"regime": reg["label"], "bias": BIAS_TXT[bias_val], "label": "NO TRADE", "status": "",
           "metode": None, "arah": None, "harga": price,
           "entry": None, "sl": None, "tp": None, "catatan": []}
    if bias_val is None:
        out["catatan"].append(f"bias H4 belum bisa dihitung (bar H4: {ctx['n_h4']}, butuh 200)")

    kandidat = ranking.get((pair, reg["label"]), [])
    if not kandidat:
        out["status"] = "Tidak ada metode prioritas"
        out["catatan"].append(f"regime {reg['label']} belum punya metode prioritas di ranking")
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
        out["status"] = "Menunggu trigger"
        out["catatan"].append(f"belum ada sinyal dari {len(kandidat)} kombinasi metode prioritas")
        return out

    c, s, d, strat = picked
    out["metode"], out["arah"] = c["metode"], DIR_TXT[s]
    out["sel"] = {"regime": reg["label"], **{k: c[k] for k in ("bintang", "skor", "n", "pf", "exp", "dd", "fold", "wr")}}
    if news_bersih is None:
        out["label"] = "WATCHLIST"
        out["status"] = "Trigger ada - ditahan: kalender gagal"
        out["catatan"].append("kalender tidak bisa diperiksa, entry tidak boleh dilakukan")
    elif not news_bersih:
        out["label"] = "WATCHLIST"
        out["status"] = "Trigger ada - ditahan: news"
        out["catatan"].append("ada news high-impact dalam ±30 menit")
    elif not C.SPREAD_TERSEDIA:
        out["label"] = "WATCHLIST"
        out["status"] = "Trigger ada - ditahan: spread"
        out["catatan"].append("spread belum terverifikasi (OANDA belum tersambung)")
    else:
        out["label"] = f"ENTRY {DIR_TXT[s]}"
        out["status"] = "Semua syarat terpenuhi"
        out.update(entry=price, sl=round(price - s * d, 5), tp=round(price + s * strat.TP_R * d, 5))
    return out
