"""Registri metode A-E (tahap 2)."""
from . import a_fisher, b_ema, c_macd, d_stoch, e_bbsqueeze

METODE = {
    "A": a_fisher,
    "B": b_ema,
    "C": c_macd,
    "D": d_stoch,
    "E": e_bbsqueeze,
}
