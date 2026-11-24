"""Metode C: MACD Signal-Line Momentum (tahap 2).
LONG : MACD cross ke atas signal, close > EMA200, histogram positif dan naik, |MACD| >= 0.1 x ATR.
SHORT: MACD cross ke bawah signal, close < EMA200, histogram negatif dan turun, |MACD| >= 0.1 x ATR.
SL: 1.0 x ATR14, dijepit 10-30 pip. Exit tambahan dikerjakan di modul backtest.
"""
from ..indicators import atr, ema, macd
from .common import sl_jarak, hasil

NAMA = "C_MACD"


def signals(h1, pip, **_):
    c = h1["close"]
    m = macd(c)
    e200 = ema(c, 200)
    a = atr(h1, 14)
    cross_up = (m["macd"].shift(1) <= m["signal"].shift(1)) & (m["macd"] > m["signal"])
    cross_dn = (m["macd"].shift(1) >= m["signal"].shift(1)) & (m["macd"] < m["signal"])
    noise_ok = m["macd"].abs() >= 0.1 * a
    h = m["hist"]
    long_ = cross_up & (c > e200) & (h > 0) & (h > h.shift(1)) & noise_ok
    short_ = cross_dn & (c < e200) & (h < 0) & (h < h.shift(1)) & noise_ok
    sl = sl_jarak(a, pip, 1.0, 10, 30)
    return hasil(h1.index, long_, short_, sl, "MACD cross up di atas EMA200", "MACD cross down di bawah EMA200")
