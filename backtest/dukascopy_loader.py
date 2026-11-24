"""Loader M1 BID/ASK untuk backtest dari cache lokal (DUKASCOPY_CACHE_DIR).

PERHATIAN: integrasi langsung ke paket dukascopy-downloader BELUM dibuat karena API paketnya
belum diverifikasi. Siapkan file CSV per pair di DUKASCOPY_CACHE_DIR, nama EUR_USD_M1.csv,
dengan kolom: time (epoch detik atau ISO-8601 UTC), bid_open, bid_high, bid_low, bid_close,
ask_open, ask_high, ask_low, ask_close.
"""
import csv
import os

import config as C


def load_m1(pair):
    cache = os.environ.get("DUKASCOPY_CACHE_DIR", "").strip()
    if not cache:
        raise FileNotFoundError("DUKASCOPY_CACHE_DIR belum diatur")
    path = os.path.join(cache, f"{pair}_M1.csv")
    if not os.path.exists(path):
        raise FileNotFoundError(f"cache tidak ada: {path}")
    rows = []
    with open(path, encoding="utf-8", newline="") as f:
        for r in csv.DictReader(f):
            rows.append({"t": C.to_epoch(r["time"]),
                         "bo": float(r["bid_open"]), "bh": float(r["bid_high"]),
                         "bl": float(r["bid_low"]), "bc": float(r["bid_close"]),
                         "ao": float(r["ask_open"]), "ah": float(r["ask_high"]),
                         "al": float(r["ask_low"]), "ac": float(r["ask_close"])})
    rows.sort(key=lambda x: x["t"])
    return rows
