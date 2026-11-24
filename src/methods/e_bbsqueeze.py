"""Metode E: Bollinger Bands Squeeze Breakout (tahap 2).
Squeeze: bb_width_pct < 20 selama 3 bar berturut-turut sebelum bar sinyal.
LONG : close menembus Upper Band (edge), candle bullish, body >= 0.5 x ATR.
SHORT: close menembus Lower Band (edge), candle bearish, body >= 0.5 x ATR.
SL: 1.0 x ATR14 (keputusan tahap 2). TP 2R dan false-breakout exit dikerjakan di backtest.
"""
from ..indicators import atr, bollinger
from ..indicators import pct_rank
from .common import sl_jarak, bull, bear, hasil, edge

NAMA = "E_BB_SQUEEZE"


def signals(h1, pip, **_):
    b = bollinger(h1["close"], 20, 2)
    width_pct = pct_rank(b["width"], 100)
    a = atr(h1, 14)
    sq = (width_pct < 20).shift(1).fillna(False)
    sq3 = sq & sq.shift(1).fillna(False) & sq.shift(2).fillna(False)
    body = (h1["close"] - h1["open"]).abs()
    big = body >= 0.5 * a
    up = h1["close"] > b["upper"]
    dn = h1["close"] < b["lower"]
    long_c = sq3 & up & bull(h1) & big
    short_c = sq3 & dn & bear(h1) & big
    sl = sl_jarak(a, pip, 1.0)
    return hasil(h1.index, edge(long_c), edge(short_c), sl,
                 "Breakout upper band setelah squeeze", "Breakout lower band setelah squeeze")
