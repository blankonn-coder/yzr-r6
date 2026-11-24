"""Klasifikasi regime pasar H1 (tahap 2, bagian 4 skema).

Label tren: TRENDING KUAT, TRENDING LEMAH, RANGING, VOLATIL/CHOPPY, MIXED, TIDAK JELAS.
SQUEEZE dicatat sebagai flag terpisah (bb_width_pct < 20), karena kondisi volatilitas
bisa terjadi bersama label tren. Jika lebih dari satu label tren cocok, hasilnya MIXED.
"""
import numpy as np
import pandas as pd


def classify(ind):
    """ind: DataFrame dari indicators.build (kolom adx14, hurst100, atr_pct, bb_width_pct)."""
    adx_ = ind["adx14"]
    hu = ind["hurst100"]
    ap = ind["atr_pct"]

    kuat = (adx_ > 25) & (hu > 0.5) & (ap > 50)
    lemah = ((adx_ >= 20) & (adx_ <= 25)) | ((hu >= 0.45) & (hu <= 0.5))
    ranging = (adx_ < 20) & (hu < 0.45) & (ap < 50)
    volatil = (ap > 80) & (adx_ < 25)

    jumlah = kuat.astype(int) + lemah.astype(int) + ranging.astype(int) + volatil.astype(int)
    label = np.select(
        [jumlah == 0, jumlah > 1, kuat, lemah, ranging, volatil],
        ["TIDAK JELAS", "MIXED", "TRENDING KUAT", "TRENDING LEMAH", "RANGING", "VOLATIL/CHOPPY"],
        default="TIDAK JELAS",
    )
    siap = ind[["adx14", "hurst100", "atr_pct"]].notna().all(axis=1)
    label = pd.Series(np.where(siap, label, "BELUM SIAP"), index=ind.index)
    squeeze = (ind["bb_width_pct"] < 20).fillna(False).astype(bool)
    return pd.DataFrame({"regime": label, "squeeze": squeeze})
