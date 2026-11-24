"""Helper bersama untuk metode A-E (tahap 2)."""
import pandas as pd


def sl_jarak(atr, pip, mult=1.0, min_pip=None, max_pip=None):
    """Jarak SL dalam harga: mult x ATR, dijepit ke [min_pip, max_pip] bila diberikan."""
    d = mult * atr
    if min_pip is not None:
        d = d.clip(lower=min_pip * pip)
    if max_pip is not None:
        d = d.clip(upper=max_pip * pip)
    return d


def bull(df):
    return df["close"] > df["open"]


def bear(df):
    return df["close"] < df["open"]


def hasil(index, long_, short_, sl, alasan_long, alasan_short):
    """Satu baris per bar sinyal. direction: +1 LONG, -1 SHORT, 0 tidak ada.
    Sinyal dihitung dari bar yang sudah close; entry sebenarnya dilakukan di open bar berikutnya
    (dikerjakan modul backtest, bukan di sini)."""
    long_ = long_.fillna(False).astype(bool)
    short_ = short_.fillna(False).astype(bool)
    arah = pd.Series(0, index=index)
    arah[long_ & ~short_] = 1
    arah[short_ & ~long_] = -1
    alasan = pd.Series("", index=index)
    alasan[arah == 1] = alasan_long
    alasan[arah == -1] = alasan_short
    return pd.DataFrame({"direction": arah, "sl_dist": sl.where(arah != 0), "reason": alasan})


def edge(cond):
    """Pemicu sekali: hanya bar pertama ketika kondisi menjadi benar."""
    c = cond.fillna(False).astype(bool)
    return c & ~c.shift(1, fill_value=False)
