"""Simulasi backtest (§6).

Sinyal dihitung dari candle mid. Entry LONG di ASK open bar berikutnya, SHORT di BID open.
Exit LONG di BID, SHORT di ASK. Slippage merugikan di setiap fill. SL/TP dicek ke high/low bar,
SL didahulukan jika keduanya kena dalam satu bar. Gap melewati SL: exit di open.
"""
import bisect
import statistics

import config as C
import regime as R

DIR_TXT = {1: "LONG", -1: "SHORT"}


def resample(m1, gran):
    """Agregasi M1 bid/ask ke timeframe gran (detik). Bar terakhir dibuang (belum lengkap)."""
    buckets = {}
    for r in m1:
        b = r["t"] - r["t"] % gran
        x = buckets.get(b)
        if x is None:
            buckets[b] = {"t": b, "bo": r["bo"], "bh": r["bh"], "bl": r["bl"], "bc": r["bc"],
                          "ao": r["ao"], "ah": r["ah"], "al": r["al"], "ac": r["ac"]}
        else:
            x["bh"] = max(x["bh"], r["bh"])
            x["bl"] = min(x["bl"], r["bl"])
            x["bc"] = r["bc"]
            x["ah"] = max(x["ah"], r["ah"])
            x["al"] = min(x["al"], r["al"])
            x["ac"] = r["ac"]
    out = []
    for b in sorted(buckets)[:-1]:
        x = buckets[b]
        out.append({**x, "o": (x["bo"] + x["ao"]) / 2, "h": (x["bh"] + x["ah"]) / 2,
                    "l": (x["bl"] + x["al"]) / 2, "c": (x["bc"] + x["ac"]) / 2})
    return out


def _spread_ok(cs, k, pair):
    if k < C.SPREAD_MEDIAN_BARS:
        return False
    prev = [cs[j]["ac"] - cs[j]["bc"] for j in range(k - C.SPREAD_MEDIAN_BARS, k)]
    cur = cs[k]["ac"] - cs[k]["bc"]
    return cur <= C.SPREAD_MEDIAN_MULT * statistics.median(prev) and cur <= C.spread_max_pips(pair) * C.pip_size(pair)


def _news_block(news, t):
    if not news:
        return False
    w = C.NEWS_WINDOW_MIN * 60
    j = bisect.bisect_left(news, t - w)
    return j < len(news) and news[j] <= t + w


def _close(pos, cs, k, fill, reason, metode, pair):
    d = pos["dir"]
    return {"pair": pair, "metode": metode, "arah": DIR_TXT[d], "regime": pos["regime"],
            "entry_idx": pos["entry_idx"], "exit_idx": k,
            "entry_time": pos["entry_time"], "exit_time": cs[k]["t"],
            "r": round((fill - pos["entry"]) * d / pos["risk"], 4), "alasan": reason}


def _step(pos, cs, ctx, k, method, pip, slip, pair):
    """Proses bar k untuk posisi terbuka. Return dict trade jika posisi ditutup, else None."""
    c, d = cs[k], pos["dir"]
    if d == 1:
        sl_hit, tp_hit, op = c["bl"] <= pos["sl"], c["bh"] >= pos["tp"], c["bo"]
    else:
        sl_hit, tp_hit, op = c["ah"] >= pos["sl"], c["al"] <= pos["tp"], c["ao"]
    if sl_hit:
        raw = op if (op - pos["sl"]) * d <= 0 else pos["sl"]
        return _close(pos, cs, k, raw - d * slip, "SL", method.NAME, pair)
    if tp_hit:
        raw = op if (op - pos["tp"]) * d >= 0 else pos["tp"]
        return _close(pos, cs, k, raw, "TP", method.NAME, pair)

    pos["bars"] = k - pos["entry_idx"] + 1
    pos["extreme"] = max(pos["extreme"], c["h"]) if d == 1 else min(pos["extreme"], c["l"])
    reason = method.exit_check(ctx, k, pos)
    if reason:
        raw = c["bc"] if d == 1 else c["ac"]
        return _close(pos, cs, k, raw - d * slip, reason, method.NAME, pair)
    if method.BE_R and not pos["be"] and d * (pos["extreme"] - pos["entry"]) >= method.BE_R * pos["risk"]:
        pos["sl"] = pos["entry"] + d * method.BE_OFFSET_PIP * pip
        pos["be"] = True
    method.manage(ctx, k, pos)
    return None


def simulate(pair, ctx, method, news=None):
    cs = ctx["cs"]
    n = len(cs)
    pip = C.pip_size(pair)
    slip = C.SLIP_PIPS * pip
    trades, pos, cool_until = [], None, 0
    for k in range(n):
        if pos is not None:
            done = _step(pos, cs, ctx, k, method, pip, slip, pair)
            if done is not None:
                trades.append(done)
                cool_until = k + method.COOLDOWN
                pos = None
        if pos is None and k >= cool_until and k + 1 < n:
            s = method.signal(ctx, k)
            if s and _spread_ok(cs, k, pair) and not _news_block(news, cs[k + 1]["t"]):
                reg = R.classify(ctx["ind"], k, ctx["closes"])["label"]
                d = method.sl_dist(ctx, k, pair)
                # Regime BELUM SIAP (warm-up) tidak pernah dipakai scanner: sinyal dibuang
                if d and reg != "BELUM SIAP":
                    entry = (cs[k + 1]["ao"] if s == 1 else cs[k + 1]["bo"]) + s * slip
                    pos = {"dir": s, "entry": entry, "sl": entry - s * d,
                           "tp": entry + s * method.TP_R * d, "risk": d,
                           "entry_idx": k + 1, "entry_time": cs[k + 1]["t"],
                           "extreme": entry, "be": False, "bars": 0, "regime": reg}
    return trades
