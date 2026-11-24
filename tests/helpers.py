import numpy as np
import pandas as pd


def m1_sintetis(n_menit=60 * 24 * 14, seed=1, awal="2026-10-01T00:00:00Z"):
    """Data M1 acak deterministik (random walk) untuk uji."""
    rng = np.random.default_rng(seed)
    close = 1.10 + np.cumsum(rng.normal(0, 0.00015, n_menit))
    open_ = np.r_[close[0], close[:-1]]
    high = np.maximum(open_, close) + np.abs(rng.normal(0, 0.00008, n_menit))
    low = np.minimum(open_, close) - np.abs(rng.normal(0, 0.00008, n_menit))
    t = pd.date_range(awal, periods=n_menit, freq="min", tz="UTC")
    return pd.DataFrame({"time": t, "open": open_, "high": high, "low": low,
                         "close": close, "volume": rng.integers(1, 50, n_menit)})


def ohlc_acak(n=600, seed=2):
    rng = np.random.default_rng(seed)
    close = 1.10 + np.cumsum(rng.normal(0, 0.0004, n))
    open_ = np.r_[close[0], close[:-1]]
    high = np.maximum(open_, close) + np.abs(rng.normal(0, 0.0002, n))
    low = np.minimum(open_, close) - np.abs(rng.normal(0, 0.0002, n))
    t = pd.date_range("2026-10-01", periods=n, freq="h", tz="UTC")
    return pd.DataFrame({"time": t, "open": open_, "high": high, "low": low, "close": close})
