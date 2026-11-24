"""Metode D: Stochastic + MA200 Mean Reversion (tahap 2).
LONG : close > MA200, %K[t-1] < 20 dan %K cross ke atas %D pada bar t, candle bullish.
SHORT: close < MA200, %K[t-1] > 80 dan %K cross ke bawah %D pada bar t, candle bearish.
SL: 1.0 x ATR14, minimum 15 pip (H1). Exit TP 1.5R atau %K ke 50 dikerjakan di backtest.
"""
from ..indicators import atr, sma, stoch
from .common import sl_jarak, bull, bear, hasil

NAMA = "D_STOCH_MA200"


def signals(h1, pip, **_):
    s = stoch(h1, 14, 3, 3)
    k, d = s["k"], s["d"]
    ma = sma(h1["close"], 200)
    a = atr(h1, 14)
    cross_up = (k.shift(1) <= d.shift(1)) & (k > d)
    cross_dn = (k.shift(1) >= d.shift(1)) & (k < d)
    long_ = (h1["close"] > ma) & (k.shift(1) < 20) & cross_up & bull(h1)
    short_ = (h1["close"] < ma) & (k.shift(1) > 80) & cross_dn & bear(h1)
    sl = sl_jarak(a, pip, 1.0, 15, None)
    return hasil(h1.index, long_, short_, sl, "Stoch balik dari oversold, searah MA200", "Stoch balik dari overbought, searah MA200")
