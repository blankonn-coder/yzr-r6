"""Registry lima metode entry (§5)."""
from . import bb_squeeze, ema_trend, fisher, macd_momentum, stoch_mr

REGISTRY = {m.NAME: m for m in (fisher, ema_trend, macd_momentum, stoch_mr, bb_squeeze)}
