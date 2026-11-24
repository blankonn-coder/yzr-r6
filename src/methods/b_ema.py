"""Metode B: EMA 50/200 Trend Following (tahap 2).
Cross EMA50 terhadap EMA200 terjadi dalam 3 bar terakhir (termasuk bar sinyal).
Pada bar sinyal: jarak EMA50-EMA200 >= 0.2 x ATR, close di sisi EMA50 searah, candle searah,
dan bias H4 searah (EMA50 > EMA200 di H4 untuk LONG, sebaliknya untuk SHORT).
Pemicu hanya pada bar pertama kondisi terpenuhi. SL: 1.0 x ATR14.
"""
import pandas as pd

from ..indicators import atr, ema
from .common import sl_jarak, bull, bear, hasil, edge

NAMA = "B_EMA_CROSS"


def signals(h1, pip, h4_bias=None, **_):
    c = h1["close"]
    e50, e200 = ema(c, 50), ema(c, 200)
    a = atr(h1, 14)
    up = (e50.shift(1) <= e200.shift(1)) & (e50 > e200)
    dn = (e50.shift(1) >= e200.shift(1)) & (e50 < e200)
    recent_up = up.rolling(3).max().fillna(0).astype(bool)
    recent_dn = dn.rolling(3).max().fillna(0).astype(bool)

    h4 = pd.Series(0, index=h1.index)
    if h4_bias is not None:
        t_sinyal = pd.to_datetime(h1["time"], utc=True) + pd.Timedelta(hours=1)
        tmp = pd.DataFrame({"t": t_sinyal, "ord": range(len(h1))}).sort_values("t")
        m = pd.merge_asof(tmp, h4_bias.sort_values("close_time"), left_on="t", right_on="close_time", direction="backward")
        h4 = pd.Series(m.sort_values("ord")["h4_bias"].fillna(0).to_numpy(), index=h1.index)

    jarak_ok = (e50 - e200).abs() >= 0.2 * a
    long_c = recent_up & jarak_ok & (c > e50) & bull(h1) & (h4 == 1)
    short_c = recent_dn & jarak_ok & (c < e50) & bear(h1) & (h4 == -1)
    sl = sl_jarak(a, pip, 1.0)
    return hasil(h1.index, edge(long_c), edge(short_c), sl,
                 "EMA50 cross ke atas EMA200, H4 searah", "EMA50 cross ke bawah EMA200, H4 searah")
