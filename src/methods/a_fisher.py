"""Metode A: Fisher Transform Reversal (tahap 2).
LONG : Fisher[t-1] < -1.5, Fisher[t] naik, candle bullish.
SHORT: Fisher[t-1] > +1.5, Fisher[t] turun, candle bearish.
SL: 1.0 x ATR14, dijepit 10-30 pip. TP dan trailing dikerjakan di modul backtest.
"""
from ..indicators import atr, fisher
from .common import sl_jarak, bull, bear, hasil

NAMA = "A_FISHER"


def signals(h1, pip, **_):
    f = fisher(h1, 9)
    f1 = f.shift(1)
    a = atr(h1, 14)
    long_ = (f1 < -1.5) & (f > f1) & bull(h1)
    short_ = (f1 > 1.5) & (f < f1) & bear(h1)
    sl = sl_jarak(a, pip, 1.0, 10, 30)
    return hasil(h1.index, long_, short_, sl, "Fisher balik dari ekstrem bawah", "Fisher balik dari ekstrem atas")
