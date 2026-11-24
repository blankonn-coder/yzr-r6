"""Metrik backtest (tahap 3, bagian 6 STEP 5)."""
import numpy as np


def ringkas(r, fold=None, n_folds=4):
    """r: array R bersih per trade. fold: indeks fold per trade (0..n_folds-1)."""
    r = np.asarray(r, dtype=float)
    n = len(r)
    out = {"trade": int(n)}
    if n == 0:
        out.update({"win_rate": None, "pf": None, "expectancy_r": None, "total_r": 0.0,
                    "max_dd_r": None, "avg_win_r": None, "avg_loss_r": None,
                    "rr_aktual": None, "max_loss_beruntun": 0, "fold_profit": 0, "stabilitas": 0.0})
        return out
    menang = r[r > 0]
    kalah = r[r <= 0]
    gw, gl = menang.sum(), -kalah.sum()
    pf = float(gw / gl) if gl > 0 else (float("inf") if gw > 0 else 0.0)
    eq = np.r_[0.0, np.cumsum(r)]
    max_dd = max(0.0, float(-(eq - np.maximum.accumulate(eq)).min()))
    beruntun = cur = 0
    for x in r:
        cur = cur + 1 if x <= 0 else 0
        beruntun = max(beruntun, cur)
    avg_w = float(menang.mean()) if len(menang) else None
    avg_l = float(kalah.mean()) if len(kalah) else None
    out.update({
        "win_rate": float(len(menang) / n),
        "pf": pf,
        "expectancy_r": float(r.mean()),
        "total_r": float(r.sum()),
        "max_dd_r": max_dd,
        "avg_win_r": avg_w,
        "avg_loss_r": avg_l,
        "rr_aktual": (avg_w / abs(avg_l)) if (avg_w is not None and avg_l) else None,
        "max_loss_beruntun": int(beruntun),
    })
    if fold is not None:
        fold = np.asarray(fold)
        untung = 0
        for f in range(n_folds):
            sub = r[fold == f]
            if len(sub) and sub.sum() > 0:
                untung += 1
        out["fold_profit"] = int(untung)
        out["stabilitas"] = untung / n_folds
    else:
        out["fold_profit"] = 0
        out["stabilitas"] = 0.0
    return out
