"""Validasi kualitas data (§3).

Gagal (error): NaN, duplikat timestamp, urutan waktu mundur, OHLC tidak logis, bid > ask.
Dilaporkan saja (warning): gap dan candle flat. Bar belum lengkap dibuang di pemanggil.
"""
import math

import config as C  # noqa: F401  (dipertahankan untuk konsistensi import proyek)


def _bad(v):
    return v is None or (isinstance(v, float) and math.isnan(v))


def validate(cs, gran_sec, bidask=False):
    """Return (ok, errors, warnings)."""
    if len(cs) < 2:
        return False, ["data terlalu sedikit"], []
    err_cnt = {"NaN": 0, "duplikat timestamp": 0, "urutan waktu mundur": 0,
               "OHLC tidak logis": 0, "bid > ask": 0}
    warn_cnt = {"gap": 0, "candle flat": 0}
    seen, prev_t = set(), None
    for c in cs:
        keys = ["o", "h", "l", "c"] + (["bo", "bh", "bl", "bc", "ao", "ah", "al", "ac"] if bidask else [])
        if any(_bad(c.get(k)) for k in keys):
            err_cnt["NaN"] += 1
            continue
        t = c["t"]
        if t in seen:
            err_cnt["duplikat timestamp"] += 1
        seen.add(t)
        if prev_t is not None:
            if t < prev_t:
                err_cnt["urutan waktu mundur"] += 1
            elif t - prev_t > 3 * gran_sec:
                warn_cnt["gap"] += 1
        prev_t = t
        if not (c["h"] >= c["l"] and c["l"] <= min(c["o"], c["c"]) and c["h"] >= max(c["o"], c["c"])):
            err_cnt["OHLC tidak logis"] += 1
        if bidask:
            if any(c[b] > c[a] for b, a in (("bo", "ao"), ("bh", "ah"), ("bl", "al"), ("bc", "ac"))):
                err_cnt["bid > ask"] += 1
        if c["o"] == c["h"] == c["l"] == c["c"]:
            warn_cnt["candle flat"] += 1
    errors = [f"{k}: {v}" for k, v in err_cnt.items() if v]
    warnings = [f"{k}: {v}" for k, v in warn_cnt.items() if v]
    return not errors, errors, warnings
