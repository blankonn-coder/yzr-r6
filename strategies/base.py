"""Utilitas bersama untuk kelima metode."""
import config as C


def clamp(x, lo, hi):
    return max(lo, min(hi, x))


def sl_pips(atr, pair, lo_pips, hi_pips=None):
    """Jarak SL dalam harga = clamp(ATR, lo..hi pip). hi None = tanpa batas atas."""
    if atr is None:
        return None
    pip = C.pip_size(pair)
    hi = hi_pips * pip if hi_pips is not None else float("inf")
    return clamp(atr, lo_pips * pip, hi)
