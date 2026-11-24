"""C. MACD Signal-Line Momentum."""
from indicators import ok
from .base import sl_pips

NAME = "MACD"
TP_R = 2.0
COOLDOWN = 3
BE_R = 1.0
BE_OFFSET_PIP = 0
MIN_MACD_ATR = 0.1
TRAIL_ATR = 0.5


def signal(ctx, i):
    ind, cs = ctx["ind"], ctx["cs"]
    if i < 1:
        return 0
    m, s, h = ind["macd"], ind["macd_sig"], ind["macd_hist"]
    e200, atr = ind["ema200"][i], ind["atr"][i]
    if not ok(m[i - 1], s[i - 1], m[i], s[i], h[i], h[i - 1], e200, atr):
        return 0
    if abs(m[i]) < MIN_MACD_ATR * atr:
        return 0
    if m[i - 1] <= s[i - 1] and m[i] > s[i] and cs[i]["c"] > e200 and h[i] > 0 and h[i] > h[i - 1]:
        return 1
    if m[i - 1] >= s[i - 1] and m[i] < s[i] and cs[i]["c"] < e200 and h[i] < 0 and h[i] < h[i - 1]:
        return -1
    return 0


def sl_dist(ctx, i, pair):
    return sl_pips(ctx["ind"]["atr"][i], pair, 10, 30)


def exit_check(ctx, k, pos):
    if k < 2:
        return None
    h = ctx["ind"]["macd_hist"]
    if not ok(h[k], h[k - 1], h[k - 2]):
        return None
    if pos["dir"] == 1 and h[k] < h[k - 1] < h[k - 2] and h[k] < 0:
        return "histogram mengecil dan balik tanda"
    if pos["dir"] == -1 and h[k] > h[k - 1] > h[k - 2] and h[k] > 0:
        return "histogram mengecil dan balik tanda"
    return None


def manage(ctx, k, pos):
    if not pos["be"]:
        return
    atr = ctx["ind"]["atr"][k]
    if not ok(atr):
        return
    if pos["dir"] == 1:
        pos["sl"] = max(pos["sl"], pos["extreme"] - TRAIL_ATR * atr)
    else:
        pos["sl"] = min(pos["sl"], pos["extreme"] + TRAIL_ATR * atr)
