"""Ambil candle dan kalender dari biquote (publik, tanpa API key).

Candle: GET {host}/api/{symbol}/ohlc?interval=...&limit=...
- Bar yang masih berjalan (isOpen=true) dibuang; urutan diubah lama -> baru.
- Waktu dinormalisasi ke epoch detik (C.to_epoch).
ASUMSI: skema JSON 'bars' dan 'openTime' sama dengan skema yang dipakai scalper lama.
"""
import time

import requests

import config as C


class PriceError(Exception):
    pass


def fetch_candles(pair, interval, count, max_retry=5):
    symbol = pair.replace("_", "")
    url = f"{C.BIQUOTE_HOST}/api/{symbol}/ohlc"
    params = {"interval": interval, "limit": count}
    delay = 1.0
    for _ in range(max_retry):
        r = requests.get(url, params=params, timeout=20)
        if r.status_code in (429, 503) or r.status_code >= 500:
            time.sleep(min(delay, 30))
            delay *= 2
            continue
        if r.status_code != 200:
            raise PriceError(f"HTTP {r.status_code}")
        bars = r.json().get("bars", [])
        out = [{"t": C.to_epoch(b["openTime"]), "o": float(b["open"]), "h": float(b["high"]),
                "l": float(b["low"]), "c": float(b["close"])}
               for b in bars if not b.get("isOpen")]
        out.sort(key=lambda x: x["t"])
        if len(out) < 60:
            raise PriceError(f"bar kurang ({len(out)}) untuk {symbol} {interval}")
        return out
    raise PriceError(f"gagal setelah {max_retry} percobaan (rate limit/server)")


def fetch_news_times():
    """Waktu (epoch detik) event high-impact dari kalender biquote.

    ASUMSI: endpoint dan skema JSON ('events', 'impact', 'time') belum diverifikasi.
    Apa pun kegagalannya, pemanggil memperlakukannya sebagai 'kalender gagal' (tanpa ENTRY).
    """
    r = requests.get(C.BIQUOTE_HOST + C.BIQUOTE_CALENDAR_PATH, timeout=20)
    if r.status_code != 200:
        raise PriceError(f"kalender HTTP {r.status_code}")
    out = [C.to_epoch(e["time"]) for e in r.json().get("events", [])
           if str(e.get("impact", "")).lower() == "high"]
    return sorted(out)
