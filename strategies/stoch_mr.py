"""D. Stochastic + MA200 Mean Reversion."""
import config as C
from indicators import bearish, bullish, ok
from .base import sl_pips

NAME = "STOCH_MR"
TP_R = 1.5
COOLDOWN = 2
BE_R = None
BE_OFFSET_PIP = 0
LOW, HIGH, MID = 20, 80, 50
TIME_STOP = 4


def signal(ctx, i):
    ind, cs = ctx["ind"], ctx["cs"]
    if i < 1:
        return 0
    k, d, ma = ind["stoch_k"], ind["stoch_d"], ind["ma200"][i]
    if not ok(k[i - 1], d[i - 1], k[i], d[i], ma):
        return 0
    c = cs[i]["c"]
    if c > ma and k[i - 1] < LOW and k[i - 1] <= d[i - 1] and k[i] > d[i] and bullish(cs[i]):
        return 1
    if c < ma and k[i - 1] > HIGH and k[i - 1] >= d[i - 1] and k[i] < d[i] and bearish(cs[i]):
        return -1
    return 0


def sl_dist(ctx, i, pair):
    return sl_pips(ctx["ind"]["atr"][i], pair, 15, None)


def exit_check(ctx, k, pos):
    ind = ctx["ind"]
    if pos["bars"] >= TIME_STOP:
        return "time stop"
    kk, ma = ind["stoch_k"][k], ind["ma200"][k]
    if not ok(kk, ma):
        return None
    close = ctx["cs"][k]["c"]
    if pos["dir"] == 1:
        if kk >= MID:
            return "%K mencapai 50"
        if close < ma:
            return "close tembus MA200"
    else:
        if kk <= MID:
            return "%K mencapai 50"
        if close > ma:
            return "close tembus MA200"
    return None


def manage(ctx, k, pos):
    return None
