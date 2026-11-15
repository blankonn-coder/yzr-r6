"""Ambil candle OHLC dari OANDA v20 (memakai harga mid)."""
import time

import requests

from . import config as C


class OandaError(Exception):
    pass


def fetch_candles(instrument, granularity, count=C.CANDLE_COUNT, max_retry=5):
    url = f"{C.OANDA_HOST}/instruments/{instrument}/candles"
    params = {"granularity": granularity, "count": count, "price": C.PRICE_TYPE}
    headers = {"Authorization": f"Bearer {C.OANDA_API_KEY}"}
    delay = 1.0
    for _ in range(max_retry):
        r = requests.get(url, params=params, headers=headers, timeout=20)
        if r.status_code == 429 or r.status_code >= 500:
            time.sleep(delay)  # exponential backoff
            delay *= 2
            continue
        if r.status_code != 200:
            raise OandaError(f"HTTP {r.status_code}: {r.text[:150]}")
        out = []
        for c in r.json().get("candles", []):
            if not c.get("complete"):
                continue
            m = c["mid"]
            out.append({"time": c["time"], "o": float(m["o"]), "h": float(m["h"]),
                        "l": float(m["l"]), "c": float(m["c"])})
        if len(out) < 60:
            raise OandaError(f"data candle kurang ({len(out)}) untuk {instrument} {granularity}")
        return out
    raise OandaError(f"gagal setelah {max_retry} percobaan (rate limit/server)")
