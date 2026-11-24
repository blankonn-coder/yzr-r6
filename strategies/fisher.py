"""A. Fisher Transform Reversal."""
from indicators import bearish, bullish, ok
from .base import sl_pips

NAME = "FISHER"
TP_R = 1.5
COOLDOWN = 2
BE_R = 1.0
BE_OFFSET_PIP = 2
EXTREME = 1.5


def signal(ctx, i):
    f = ctx["ind"]["fisher"]
    if i < 1 or not ok(f[i - 1], f[i]):
        return 0
    cs = ctx["cs"]
    if f[i - 1] < -EXTREME and f[i] > f[i - 1] and bullish(cs[i]):
        return 1
    if f[i - 1] > EXTREME and f[i] < f[i - 1] and bearish(cs[i]):
        return -1
    return 0


def sl_dist(ctx, i, pair):
    return sl_pips(ctx["ind"]["atr"][i], pair, 10, 30)


def exit_check(ctx, k, pos):
    # ASUMSI: "Fisher balik ekstrem dalam 1-2 bar" = 1-2 bar setelah bar entry
    f = ctx["ind"]["fisher"][k]
    if not ok(f) or not (2 <= pos["bars"] <= 3):
        return None
    if pos["dir"] == 1 and f < -EXTREME:
        return "Fisher kembali ekstrem"
    if pos["dir"] == -1 and f > EXTREME:
        return "Fisher kembali ekstrem"
    return None


def manage(ctx, k, pos):
    return None
