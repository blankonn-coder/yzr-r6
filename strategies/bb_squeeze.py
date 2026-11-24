"""E. Bollinger Bands Squeeze Breakout."""
from indicators import bearish, bullish, ok

NAME = "BB_SQUEEZE"
TP_R = 2.0
COOLDOWN = 3
BE_R = 1.0
BE_OFFSET_PIP = 0
SQUEEZE_BARS = 3
BODY_ATR = 0.5
SQUEEZE_PCT = 20


def _squeeze(ind, j):
    p = ind["bb_w_pct"][j]
    return p is not None and p < SQUEEZE_PCT


def signal(ctx, i):
    ind, cs = ctx["ind"], ctx["cs"]
    if i < SQUEEZE_BARS:
        return 0
    if not all(_squeeze(ind, j) for j in range(i - SQUEEZE_BARS, i)):
        return 0
    up, lo, atr = ind["bb_up"], ind["bb_lo"], ind["atr"][i]
    if not ok(up[i], up[i - 1], lo[i], lo[i - 1], atr):
        return 0
    c, cp = cs[i], cs[i - 1]
    body = abs(c["c"] - c["o"])
    if body < BODY_ATR * atr:
        return 0
    if c["c"] > up[i] and cp["c"] <= up[i - 1] and bullish(c):
        return 1
    if c["c"] < lo[i] and cp["c"] >= lo[i - 1] and bearish(c):
        return -1
    return 0


def sl_dist(ctx, i, pair):
    atr = ctx["ind"]["atr"][i]
    return atr if atr else None


def exit_check(ctx, k, pos):
    # ASUMSI: "close balik ke dalam band 1-2 bar" = close kembali masuk band pada bar ke-1..2
    if pos["bars"] > 2:
        return None
    up, lo = ctx["ind"]["bb_up"][k], ctx["ind"]["bb_lo"][k]
    if not ok(up, lo):
        return None
    close = ctx["cs"][k]["c"]
    if pos["dir"] == 1 and close < up:
        return "close kembali ke dalam band"
    if pos["dir"] == -1 and close > lo:
        return "close kembali ke dalam band"
    return None


def manage(ctx, k, pos):
    return None
