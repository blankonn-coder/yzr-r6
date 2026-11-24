"""Indikator teknikal (pure Python).

Input: list candle dict {"t","o","h","l","c"} atau list float.
Output: list dengan panjang sama. None = belum cukup data (warm-up).
"""
import math

import config as C


def ok(*vals):
    return all(v is not None for v in vals)


def bullish(c):
    return c["c"] > c["o"]


def bearish(c):
    return c["c"] < c["o"]


def ema(vals, p):
    n = len(vals)
    out = [None] * n
    if n < p:
        return out
    k = 2.0 / (p + 1)
    s = sum(vals[:p]) / p
    out[p - 1] = s
    for i in range(p, n):
        s = vals[i] * k + s * (1 - k)
        out[i] = s
    return out


def ema_from(vals, p):
    """EMA pada bagian non-None pertama yang kontinu (garis sinyal MACD)."""
    out = [None] * len(vals)
    start = next((i for i, v in enumerate(vals) if v is not None), None)
    if start is None:
        return out
    for j, v in enumerate(ema(vals[start:], p)):
        out[start + j] = v
    return out


def sma(vals, p):
    n = len(vals)
    out = [None] * n
    for i in range(p - 1, n):
        win = vals[i - p + 1:i + 1]
        if any(v is None for v in win):
            continue
        out[i] = sum(win) / p
    return out


def atr(cs, p=C.ATR_PERIOD):
    """ATR Wilder."""
    n = len(cs)
    out = [None] * n
    if n < p:
        return out
    tr = [cs[0]["h"] - cs[0]["l"]]
    for i in range(1, n):
        h, l, pc = cs[i]["h"], cs[i]["l"], cs[i - 1]["c"]
        tr.append(max(h - l, abs(h - pc), abs(l - pc)))
    a = sum(tr[:p]) / p
    out[p - 1] = a
    for i in range(p, n):
        a = (a * (p - 1) + tr[i]) / p
        out[i] = a
    return out


def adx(cs, p=C.ADX_PERIOD):
    """ADX Wilder. Nilai pertama di index 2p-1."""
    n = len(cs)
    out = [None] * n
    if n < 2 * p:
        return out
    tr = [0.0] * n
    pdm = [0.0] * n
    mdm = [0.0] * n
    for i in range(1, n):
        h, l = cs[i]["h"], cs[i]["l"]
        pc = cs[i - 1]["c"]
        tr[i] = max(h - l, abs(h - pc), abs(l - pc))
        up = h - cs[i - 1]["h"]
        dn = cs[i - 1]["l"] - l
        pdm[i] = up if up > dn and up > 0 else 0.0
        mdm[i] = dn if dn > up and dn > 0 else 0.0

    def _dx(st, sp, sm):
        if st == 0:
            return 0.0
        pdi, mdi = 100 * sp / st, 100 * sm / st
        s = pdi + mdi
        return 0.0 if s == 0 else 100 * abs(pdi - mdi) / s

    st, sp, sm = sum(tr[1:p + 1]), sum(pdm[1:p + 1]), sum(mdm[1:p + 1])
    dx = [None] * n
    dx[p] = _dx(st, sp, sm)
    for i in range(p + 1, n):
        st = st - st / p + tr[i]
        sp = sp - sp / p + pdm[i]
        sm = sm - sm / p + mdm[i]
        dx[i] = _dx(st, sp, sm)
    a = sum(dx[p:2 * p]) / p
    out[2 * p - 1] = a
    for i in range(2 * p, n):
        a = (a * (p - 1) + dx[i]) / p
        out[i] = a
    return out


def macd(closes, f=C.MACD_FAST, s=C.MACD_SLOW, g=C.MACD_SIG):
    e_f, e_s = ema(closes, f), ema(closes, s)
    line = [(a - b) if ok(a, b) else None for a, b in zip(e_f, e_s)]
    sig = ema_from(line, g)
    hist = [(m - q) if ok(m, q) else None for m, q in zip(line, sig)]
    return line, sig, hist


def stoch(cs, kp=C.STOCH_K, ks=C.STOCH_SMOOTH, dp=C.STOCH_D):
    n = len(cs)
    raw = [None] * n
    for i in range(kp - 1, n):
        w = cs[i - kp + 1:i + 1]
        hh = max(x["h"] for x in w)
        ll = min(x["l"] for x in w)
        raw[i] = 50.0 if hh == ll else 100 * (cs[i]["c"] - ll) / (hh - ll)
    k = sma(raw, ks)
    d = sma(k, dp)
    return k, d


def bollinger(closes, p=C.BB_PERIOD, m=C.BB_MULT):
    n = len(closes)
    up, mid, lo, w = [None] * n, [None] * n, [None] * n, [None] * n
    for i in range(p - 1, n):
        win = closes[i - p + 1:i + 1]
        mu = sum(win) / p
        sd = math.sqrt(sum((x - mu) ** 2 for x in win) / p)
        mid[i] = mu
        up[i] = mu + m * sd
        lo[i] = mu - m * sd
        w[i] = (2 * m * sd) / mu if mu else None
    return up, mid, lo, w


def fisher(cs, p=C.FISHER_PERIOD):
    """Fisher Transform (Ehlers)."""
    n = len(cs)
    out = [None] * n
    val, f_prev = 0.0, 0.0
    for i in range(p - 1, n):
        w = cs[i - p + 1:i + 1]
        hi = max(x["h"] for x in w)
        lo = min(x["l"] for x in w)
        x = (cs[i]["h"] + cs[i]["l"]) / 2
        r = 0.5 if hi == lo else (x - lo) / (hi - lo)
        val = 0.33 * 2 * (r - 0.5) + 0.67 * val
        val = max(-0.999, min(0.999, val))
        f = 0.5 * math.log((1 + val) / (1 - val)) + 0.5 * f_prev
        out[i] = f
        f_prev = f
    return out


def pct_series(s, win):
    """Persentil nilai s[i] terhadap win nilai terakhir (0-100)."""
    n = len(s)
    out = [None] * n
    for i in range(win - 1, n):
        w = s[i - win + 1:i + 1]
        if any(v is None for v in w):
            continue
        out[i] = 100 * sum(1 for v in w if v <= s[i]) / win
    return out


def hurst(rets):
    """Eksponen Hurst via R/S. None jika data tidak cukup."""
    xs, ys = [], []
    for s in C.HURST_CHUNKS:
        if s > len(rets):
            continue
        rs = []
        for start in range(0, len(rets) - s + 1, s):
            ch = rets[start:start + s]
            m = sum(ch) / s
            acc, dev = 0.0, []
            for x in ch:
                acc += x - m
                dev.append(acc)
            r = max(dev) - min(dev)
            sd = math.sqrt(sum((x - m) ** 2 for x in ch) / s)
            if sd > 0 and r > 0:
                rs.append(r / sd)
        if rs:
            xs.append(math.log(s))
            ys.append(math.log(sum(rs) / len(rs)))
    if len(xs) < 2:
        return None
    mx, my = sum(xs) / len(xs), sum(ys) / len(ys)
    den = sum((x - mx) ** 2 for x in xs)
    return None if den == 0 else sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / den


def compute(cs):
    """Semua seri indikator untuk satu timeframe."""
    closes = [c["c"] for c in cs]
    ind = {"close": closes}
    ind["ema50"] = ema(closes, C.EMA_FAST)
    ind["ema200"] = ema(closes, C.EMA_SLOW)
    ind["ma200"] = sma(closes, C.MA_PERIOD)
    ind["atr"] = atr(cs)
    ind["adx"] = adx(cs)
    ind["macd"], ind["macd_sig"], ind["macd_hist"] = macd(closes)
    ind["stoch_k"], ind["stoch_d"] = stoch(cs)
    ind["bb_up"], ind["bb_mid"], ind["bb_lo"], bbw = bollinger(closes)
    ind["bb_w_pct"] = pct_series(bbw, C.PCT_LOOKBACK)
    ind["atr_pct"] = pct_series(ind["atr"], C.PCT_LOOKBACK)
    ind["fisher"] = fisher(cs)
    return ind
