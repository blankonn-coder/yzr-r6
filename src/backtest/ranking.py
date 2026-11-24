"""Skor dan bintang (tahap 3, bagian 7 skema). Ditentukan HANYA dari hasil out-of-sample."""
import math

BATAS = {"pf_nol": 1.0, "pf_penuh": 2.0, "exp_penuh": 0.3, "dd_nol": 15.0, "sampel_penuh": 100, "sampel_min": 30}


def _klem(x):
    return max(0.0, min(1.0, x))


def skor(m):
    """Skor 0-100. Komponen: PF 25, expectancy 25, max DD 20, stabilitas fold 15, sampel 10, konsistensi win rate 5."""
    if not m["trade"] or m["pf"] is None:
        return 0.0
    pf = m["pf"] if math.isfinite(m["pf"]) else BATAS["pf_penuh"]
    pf_pts = 25 * _klem((pf - BATAS["pf_nol"]) / (BATAS["pf_penuh"] - BATAS["pf_nol"]))
    exp_pts = 25 * _klem(m["expectancy_r"] / BATAS["exp_penuh"])
    dd_pts = 20 * _klem(1 - m["max_dd_r"] / BATAS["dd_nol"])
    stab_pts = 15 * m["stabilitas"]
    sampel_pts = 10 * _klem(m["trade"] / BATAS["sampel_penuh"])
    wr = m["win_rate"] or 0.0
    cons_pts = 5 * _klem(1 - max(0.0, abs(wr - 0.5) - 0.15) / 0.15)
    return round(pf_pts + exp_pts + dd_pts + stab_pts + sampel_pts + cons_pts, 1)


def bintang(score, sampel, eligible):
    """Konversi bintang. Sampel kurang atau tidak lolos kelayakan: tidak diberi bintang."""
    if sampel < BATAS["sampel_min"]:
        return 0, "PROVISIONAL / BELUM CUKUP DATA"
    if not eligible:
        return 0, "TIDAK PRIORITAS (gagal kelayakan)"
    if score >= 90: b = 5
    elif score >= 80: b = 4
    elif score >= 70: b = 3
    elif score >= 60: b = 2
    else: b = 1
    return b, "PRIORITAS" if b >= 3 else "TIDAK DIPRIORITASKAN"


def kelayakan(m):
    """Penguci kelayakan (skema bagian 7): PF > 1, expectancy > 0, DD dalam batas, sampel cukup."""
    alasan = []
    if m["pf"] is None or m["pf"] <= 1:
        alasan.append("PF <= 1")
    if m["expectancy_r"] is None or m["expectancy_r"] <= 0:
        alasan.append("expectancy <= 0")
    if m["max_dd_r"] is not None and m["max_dd_r"] > BATAS["dd_nol"]:
        alasan.append("drawdown melewati batas")
    if m["trade"] < BATAS["sampel_min"]:
        alasan.append("sampel kurang")
    return (len(alasan) == 0), alasan
