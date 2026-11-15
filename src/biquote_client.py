"""Ambil candle OHLC dari biquote (publik, tanpa API key).

Endpoint: GET https://biquote.io/api/{symbol}/ohlc?interval=...&limit=...
- Bar terbaru datang lebih dulu, dan bar yang masih berjalan ditandai isOpen=true.
  Bar tersebut dibuang dan urutan diubah menjadi lama -> baru.
- Harga yang dipakai adalah open/high/low/close dari feed (bukan bid/ask terpisah).
"""
import time

import requests

from . import config as C


class PriceError(Exception):
    pass


def fetch_candles(pair, interval, count=C.CANDLE_COUNT, max_retry=5):
    symbol = pair.replace("_", "")  # EUR_USD -> EURUSD
    url = f"{C.BIQUOTE_HOST}/api/{symbol}/ohlc"
    params = {"interval": interval, "limit": count}
    delay = 1.0
    for _ in range(max_retry):
        r = requests.get(url, params=params, timeout=20)
        if r.status_code in (429, 503) or r.status_code >= 500:
            time.sleep(min(delay, 30))  # exponential backoff
            delay *= 2
            continue
        if r.status_code != 200:
            raise PriceError(f"HTTP {r.status_code}: {r.text[:150]}")
        bars = r.json().get("bars", [])
        out = [{"time": b["openTime"], "o": float(b["open"]), "h": float(b["high"]),
                "l": float(b["low"]), "c": float(b["close"])}
               for b in bars if not b.get("isOpen")]
        out.sort(key=lambda x: x["time"])
        if len(out) < 60:
            raise PriceError(f"data bar kurang ({len(out)}) untuk {symbol} {interval}")
        return out
    raise PriceError(f"gagal setelah {max_retry} percobaan (rate limit/server)")
