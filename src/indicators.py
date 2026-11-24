"""Indikator teknikal (tahap 2).

Semua fungsi hanya memakai data sampai bar t (tanpa look-ahead).
Input: DataFrame dengan kolom open, high, low, close (dan volume bila perlu).
"""
import numpy as np
import pandas as pd
from numpy.lib.stride_tricks import sliding_window_view


def ema(s, n):
    return s.ewm(span=n, adjust=False).mean()


def sma(s, n):
    return s.rolling(n).mean()


def wilder(s, n):
    """Pemulusan Wilder (alpha = 1/n), dipakai untuk ATR, ADX, RSI."""
    return s.ewm(alpha=1.0 / n, adjust=False).mean()


def true_range(df):
    pc = df["close"].shift(1)
    return pd.concat(
        [df["high"] - df["low"], (df["high"] - pc).abs(), (df["low"] - pc).abs()], axis=1
    ).max(axis=1)


def atr(df, n=14):
    return wilder(true_range(df), n)


def adx(df, n=14):
    up = df["high"].diff()
    dn = -df["low"].diff()
    plus = pd.Series(np.where((up > dn) & (up > 0), up, 0.0), index=df.index)
    minus = pd.Series(np.where((dn > up) & (dn > 0), dn, 0.0), index=df.index)
    tr = wilder(true_range(df), n)
    pdi = 100 * wilder(plus, n) / tr
    mdi = 100 * wilder(minus, n) / tr
    dx = 100 * (pdi - mdi).abs() / (pdi + mdi).replace(0, np.nan)
    return wilder(dx.fillna(0), n)


def rsi(close, n=14):
    d = close.diff()
    gain = wilder(d.clip(lower=0), n)
    loss = wilder((-d).clip(lower=0), n)
    rs = gain / loss  # loss 0 -> inf, RSI = 100
    return 100 - 100 / (1 + rs)


def macd(close, fast=12, slow=26, sig=9):
    line = ema(close, fast) - ema(close, slow)
    signal = ema(line, sig)
    return pd.DataFrame({"macd": line, "signal": signal, "hist": line - signal})


def stoch(df, k=14, smooth_k=3, d=3):
    hh = df["high"].rolling(k).max()
    ll = df["low"].rolling(k).min()
    raw = 100 * (df["close"] - ll) / (hh - ll).replace(0, np.nan)
    kk = sma(raw, smooth_k)
    return pd.DataFrame({"k": kk, "d": sma(kk, d)})


def bollinger(close, n=20, k=2):
    mid = sma(close, n)
    sd = close.rolling(n).std(ddof=0)
    upper = mid + k * sd
    lower = mid - k * sd
    return pd.DataFrame({"mid": mid, "upper": upper, "lower": lower, "width": (upper - lower) / mid})


def pct_rank(s, n=100):
    """Persentil posisi nilai terakhir terhadap n nilai terakhir (0-100)."""
    return s.rolling(n).rank(pct=True) * 100


def fisher(df, length=9):
    """Fisher Transform (Ehlers) dengan pemulusan 0.33/0.67 sesuai skema."""
    hl2 = ((df["high"] + df["low"]) / 2).to_numpy()
    hh = df["high"].rolling(length).max().to_numpy()
    ll = df["low"].rolling(length).min().to_numpy()
    n = len(hl2)
    val = np.zeros(n)
    fish = np.zeros(n)
    for i in range(n):
        prev_v = val[i - 1] if i else 0.0
        prev_f = fish[i - 1] if i else 0.0
        if np.isnan(hh[i]) or np.isnan(ll[i]) or hh[i] == ll[i]:
            val[i], fish[i] = prev_v, prev_f
            continue
        x = 0.33 * 2 * ((hl2[i] - ll[i]) / (hh[i] - ll[i]) - 0.5) + 0.67 * prev_v
        x = min(max(x, -0.999), 0.999)
        val[i] = x
        fish[i] = 0.5 * np.log((1 + x) / (1 - x)) + 0.5 * prev_f
    out = pd.Series(fish, index=df.index)
    out[np.isnan(hh) | np.isnan(ll)] = np.nan
    return out


def hurst(close, window=100, sizes=(10, 20, 50)):
    """Eksponen Hurst dengan R/S sederhana pada window return terakhir.

    Dihitung dari rata-rata R/S tiap potongan ukuran n, lalu kemiringan log(R/S) vs log(n).
    Nilai > 0.5 = persisten (trend), < 0.5 = anti-persisten (mean-reversion).
    Indeks hasil = indeks close penutup window.
    """
    c = np.asarray(close, dtype=float)
    r = np.diff(np.log(c))
    res = np.full(len(c), np.nan)
    if len(r) < window:
        return pd.Series(res, index=close.index)
    w = sliding_window_view(r, window)
    logs_n, logs_rs = [], []
    for n in sizes:
        chunks = w.reshape(w.shape[0], window // n, n)
        m = chunks.mean(axis=2, keepdims=True)
        y = np.cumsum(chunks - m, axis=2)
        rng = y.max(axis=2) - y.min(axis=2)
        sd = chunks.std(axis=2)
        with np.errstate(divide="ignore", invalid="ignore"):
            rs = np.where(sd > 0, rng / np.where(sd > 0, sd, 1), np.nan)
        logs_rs.append(np.log(np.nanmean(rs, axis=1)))
        logs_n.append(np.log(n))
    x = np.array(logs_n)
    y = np.vstack(logs_rs)
    slope = ((x - x.mean())[:, None] * (y - y.mean(axis=0))).sum(axis=0) / ((x - x.mean()) ** 2).sum()
    res[window:] = slope
    return pd.Series(res, index=close.index)


def median_spread(spread, n=20):
    return spread.rolling(n).median()


def build(df):
    """Semua indikator yang dipakai regime dan metode, dalam satu DataFrame."""
    out = pd.DataFrame(index=df.index)
    out["atr14"] = atr(df, 14)
    out["adx14"] = adx(df, 14)
    out["rsi14"] = rsi(df["close"], 14)
    out["ema50"] = ema(df["close"], 50)
    out["ema200"] = ema(df["close"], 200)
    out["ma200"] = sma(df["close"], 200)
    m = macd(df["close"])
    out["macd"], out["macd_sig"], out["macd_hist"] = m["macd"], m["signal"], m["hist"]
    s = stoch(df)
    out["stoch_k"], out["stoch_d"] = s["k"], s["d"]
    b = bollinger(df["close"])
    out["bb_upper"], out["bb_lower"], out["bb_mid"] = b["upper"], b["lower"], b["mid"]
    out["bb_width"] = b["width"]
    out["bb_width_pct"] = pct_rank(b["width"], 100)
    out["atr_pct"] = pct_rank(out["atr14"], 100)
    out["hurst100"] = hurst(df["close"], 100)
    out["fisher9"] = fisher(df, 9)
    return out
