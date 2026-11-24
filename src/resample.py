"""Pembentukan candle M15, H1, H4 dari M1 (tahap 2).

Hanya bar yang lengkap (jumlah menit = seharusnya) yang dipakai.
Bar yang belum selesai dibuang agar tidak dipakai sebagai sinyal.
"""
import pandas as pd

ATURAN = {"M15": ("15min", 15), "H1": ("1h", 60), "H4": ("4h", 240)}


def resample_ohlc(m1, nama):
    rule, lengkap = ATURAN[nama]
    df = m1.copy()
    df.index = pd.to_datetime(df["time"], utc=True)
    df.index.name = "time"
    df = df.sort_index()
    g = df.resample(rule, label="left", closed="left")
    out = g.agg({"open": "first", "high": "max", "low": "min", "close": "last", "volume": "sum"})
    jumlah = g.size()
    out = out[jumlah >= lengkap].dropna(subset=["open", "close"])
    return out.reset_index()


def bias_h4(h4):
    """Bias H4 per bar: +1 jika EMA50 > EMA200, -1 jika sebaliknya.
    close_time = waktu bar H4 selesai, supaya tidak dipakai sebelum selesai."""
    from .indicators import ema

    c = h4["close"]
    bias = (ema(c, 50) > ema(c, 200)).astype(int) * 2 - 1
    return pd.DataFrame({"close_time": pd.to_datetime(h4["time"], utc=True) + pd.Timedelta(hours=4),
                         "h4_bias": bias.to_numpy()})
