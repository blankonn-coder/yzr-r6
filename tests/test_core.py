import math
import random

import config as C
import indicators as I
import ranking
import regime as R
from analysis import bias_series
from backtest.engine import resample, simulate
from data_quality import validate
from strategies import REGISTRY


def _walk(n, seed=1, start=1.1000, step=0.0004, t0=1_700_000_000 - 1_700_000_000 % 3600):
    rnd = random.Random(seed)
    cs, p = [], start
    for i in range(n):
        o = p
        p = max(0.5, p + rnd.gauss(0, step))
        h, l = max(o, p) + abs(rnd.gauss(0, step / 2)), min(o, p) - abs(rnd.gauss(0, step / 2))
        cs.append({"t": t0 + 3600 * i, "o": o, "h": h, "l": l, "c": p})
    return cs


def test_ema_warmup_and_value():
    v = I.ema([1.0] * 10, 5)
    assert v[:4] == [None] * 4 and abs(v[4] - 1.0) < 1e-12


def test_fisher_sign_follows_trend():
    up = [{"t": i, "o": 1 + i * 0.01, "h": 1 + i * 0.01 + 0.005, "l": 1 + i * 0.01 - 0.005,
           "c": 1 + i * 0.01 + 0.004} for i in range(60)]
    assert I.fisher(up)[-1] > 0


def test_hurst_random_walk_near_half():
    rnd = random.Random(3)
    h_rand = I.hurst([rnd.gauss(0, 1) for _ in range(100)])
    assert 0.2 < h_rand < 0.8


def test_validate_flags_bad_ohlc_and_duplicates():
    cs = _walk(20)
    cs[5]["h"] = cs[5]["l"] - 1  # OHLC tidak logis
    cs[7]["t"] = cs[6]["t"]      # duplikat
    ok, errs, _ = validate(cs, 3600)
    assert not ok and any("OHLC" in e for e in errs) and any("duplikat" in e for e in errs)


def test_resample_drops_incomplete_last_bar():
    m1 = []
    for i in range(180):
        t = 1_700_000_000 - 1_700_000_000 % 3600 + 60 * i
        m1.append({"t": t, "bo": 1.0, "bh": 1.1, "bl": 0.9, "bc": 1.0, "ao": 1.0002, "ah": 1.1002,
                   "al": 0.9002, "ac": 1.0002})
    h1 = resample(m1, 3600)
    assert len(h1) == 2  # 3 bucket, bucket terakhir dibuang


def test_bias_uses_only_closed_h4_bar():
    h4_times = [0, 14400]
    h4_ind = {"ema50": [2.0, 1.0], "ema200": [1.0, 2.0]}
    # H1 bar pada t=14400 (tutup 18000) belum boleh memakai H4 bar 14400 (tutup 28800)
    bias = bias_series([14400, 14400 + 3 * 3600], h4_times, h4_ind)
    assert bias[0] == 1 and bias[1] == -1


def test_ranking_gates_and_provisional():
    trades = [{"r": 1.0, "fold": i % 4} for i in range(10)] + [{"r": -0.5, "fold": i % 4} for i in range(5)]
    rec = ranking.make_record("EUR_USD", "RANGING", "FISHER", "LONG", trades,
                              {"waktu": "x", "news_filter": False, "periode": "p"})
    assert rec["provisional"] and rec["bintang"] is None and rec["lolos"]
    assert rec["n"] == 15 and rec["fold"] == "4/4"


def test_simulate_runs_for_all_methods_without_error():
    cs = _walk(900, seed=7)
    for c in cs:
        spread = 0.0002
        c.update({"bo": c["o"] - spread / 2, "bh": c["h"] - spread / 2, "bl": c["l"] - spread / 2,
                  "bc": c["c"] - spread / 2, "ao": c["o"] + spread / 2, "ah": c["h"] + spread / 2,
                  "al": c["l"] + spread / 2, "ac": c["c"] + spread / 2})
    import analysis
    ctx = analysis.build(cs, [{"t": x["t"] - x["t"] % 14400, "o": x["o"], "h": x["h"], "l": x["l"], "c": x["c"]}
                              for x in cs[::4]])
    for name, m in REGISTRY.items():
        for t in simulate("EUR_USD", ctx, m):
            assert t["exit_idx"] >= t["entry_idx"]
            assert math.isfinite(t["r"])
