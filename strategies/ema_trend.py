"""B. EMA 50/200 Trend Following."""
import config as C
from indicators import bearish, bullish, ok

NAME = "EMA_TREND"
TP_R = 2.0
COOLDOWN = 5
BE_R = 1.0
BE_OFFSET_PIP = 0


def _cross(ind, i):
    e5, e2 = ind["ema50"], ind["ema200"]
    for j in (i - 2, i - 1, i):
        if j < 1 or not ok(e5[j], e2[j], e5[j - 1], e2[j - 1]):
            continue
        prev = e5[j - 1] - e2[j - 1]
        cur = e5[j] - e2[j]
        if prev <= 0 < cur:
            return 1
        if prev >= 0 > cur:
            return -1
    return 0


def _cond(ctx, i, d):
    ind, cs = ctx["ind"], ctx["cs"]
    e5, e2, atr = ind["ema50"][i], ind["ema200"][i], ind["atr"][i]
    if not ok(e5, e2, atr) or _cross(ind, i) != d:
        return False
    if abs(e5 - e2) < 0.2 * atr:
        return False
    if d * (cs[i]["c"] - e5) <= 0:
        return False
    if not (bullish(cs[i]) if d == 1 else bearish(cs[i])):
        return False
    return ctx["bias"][i] == d


def signal(ctx, i):
    if i < 1:
        return 0
    for d in (1, -1):
        if _cond(ctx, i, d) and not _cond(ctx, i - 1, d):
            return d
    return 0


def sl_dist(ctx, i, pair):
    atr = ctx["ind"]["atr"][i]
    return atr if atr else None


def exit_check(ctx, k, pos):
    # ASUMSI: "close lewati EMA50 dalam 1-3 bar" = close menembus EMA50 pada bar ke-1..3
    e5 = ctx["ind"]["ema50"][k]
    if not ok(e5) or pos["bars"] > 3:
        return None
    close = ctx["cs"][k]["c"]
    if pos["dir"] * (close - e5) < 0:
        return "close lewati EMA50"
    return None


def manage(ctx, k, pos):
    if not pos["be"]:
        return
    e5 = ctx["ind"]["ema50"][k]
    if not ok(e5):
        return
    if pos["dir"] == 1 and e5 > pos["sl"]:
        pos["sl"] = e5
    elif pos["dir"] == -1 and e5 < pos["sl"]:
        pos["sl"] = e5
