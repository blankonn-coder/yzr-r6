"""Klasifikasi regime pasar H1 (§4)."""
import config as C
from indicators import hurst, ok


def _res(label, adx=None, h=None, ap=None, squeeze=False):
    return {"label": label, "adx": adx, "hurst": h, "atr_pct": ap, "squeeze": squeeze}


def classify(ind, i, closes):
    adx, ap, bw = ind["adx"][i], ind["atr_pct"][i], ind["bb_w_pct"][i]
    squeeze = bw is not None and bw < C.BB_SQUEEZE_PCT
    if i < C.HURST_LOOKBACK or not ok(adx, ap):
        return _res("BELUM SIAP", adx, None, ap, squeeze)
    rets = [closes[j] - closes[j - 1] for j in range(i - C.HURST_LOOKBACK + 1, i + 1)]
    h = hurst(rets)
    if h is None:
        return _res("BELUM SIAP", adx, None, ap, squeeze)

    strong = adx > C.REG_ADX_STRONG and h > C.REG_HURST_STRONG and ap > C.REG_ATRPCT_STRONG
    weak = (C.REG_ADX_WEAK_MIN <= adx <= C.REG_ADX_STRONG) or (C.REG_HURST_WEAK_MIN <= h <= C.REG_HURST_STRONG)
    ranging = adx < C.REG_ADX_WEAK_MIN and h < C.REG_HURST_WEAK_MIN and ap < C.REG_ATRPCT_STRONG
    choppy = ap > C.REG_ATRPCT_CHOP and adx < C.REG_ADX_STRONG

    matches = [name for name, flag in (("TRENDING KUAT", strong), ("TRENDING LEMAH", weak),
                                       ("RANGING", ranging), ("VOLATIL/CHOPPY", choppy)) if flag]
    if not matches:
        label = "TIDAK JELAS"
    elif len(matches) == 1:
        label = matches[0]
    else:
        label = "MIXED"
    return _res(label, adx, h, ap, squeeze)
