"""S/R, RSI, EMA, filter tren, dan skoring keputusan tunggal."""
from . import config as C
from .config import pip_size


def rsi(closes, period=C.RSI_PERIOD):
    if len(closes) < period + 1:
        return None
    gains, losses = [], []
    for i in range(1, len(closes)):
        d = closes[i] - closes[i - 1]
        gains.append(max(d, 0.0))
        losses.append(max(-d, 0.0))
    ag = sum(gains[:period]) / period
    al = sum(losses[:period]) / period
    for g, lo in zip(gains[period:], losses[period:]):
        ag = (ag * (period - 1) + g) / period  # Wilder smoothing
        al = (al * (period - 1) + lo) / period
    if al == 0:
        return 100.0
    return round(100 - 100 / (1 + ag / al), 2)


def ema(values, period=C.EMA_PERIOD):
    if len(values) < period:
        return None
    k = 2 / (period + 1)
    e = sum(values[:period]) / period
    for v in values[period:]:
        e = v * k + e * (1 - k)
    return e


def _tol(pair):
    """Toleransi dalam harga, dari jumlah pip (JPY dan non-JPY otomatis benar)."""
    return C.SR_TOL_PIPS * pip_size(pair)


def find_levels(cs, tf, pair):
    tol = _tol(pair)
    n, lb = len(cs), C.SR_LOOKBACK
    levels = []
    for i in range(lb, n - lb):
        if n - 1 - i > C.SR_MAX_AGE:
            continue
        win = cs[i - lb:i + lb + 1]
        kandidat = []
        if cs[i]["h"] == max(x["h"] for x in win):
            kandidat.append(("R", cs[i]["h"]))
        if cs[i]["l"] == min(x["l"] for x in win):
            kandidat.append(("S", cs[i]["l"]))
        for jenis, harga in kandidat:
            sentuh = sum(1 for x in cs if x["l"] <= harga + tol and x["h"] >= harga - tol)
            if sentuh >= C.SR_MIN_TOUCH:
                levels.append({"type": jenis, "price": harga, "tf": tf})
    return levels


def nearest_level(price, levels, pair):
    """Satu level terdekat dari harga (support atau resistance) dalam toleransi, atau None."""
    tol = _tol(pair)
    best = None
    for lv in levels:
        d = abs(price - lv["price"])
        if d <= tol and (best is None or d < best[0]):
            best = (d, lv)
    return best[1] if best else None


def get_trend(data, price):
    arah = []
    for tf in C.TREND_TFS:
        e = ema([x["c"] for x in data[tf]])
        if e is None:
            return "SIDEWAYS"
        arah.append(1 if price > e else -1 if price < e else 0)
    if all(a == 1 for a in arah):
        return "NAIK"
    if all(a == -1 for a in arah):
        return "TURUN"
    return "SIDEWAYS"


def evaluate(data, price, pair):
    """data: {timeframe: candles} sudah terkalibrasi. Hasil: satu keputusan BUY/SELL/NETRAL."""
    buy = sell = 0
    alasan = []
    semua_level = []
    for tf in C.SR_TFS:
        lv = find_levels(data[tf], tf, pair)
        semua_level += lv
        w = C.SR_WEIGHTS[tf]
        dekat = nearest_level(price, lv, pair)  # hanya satu level per timeframe
        if dekat is None:
            continue
        if dekat["type"] == "S":
            buy += w
            alasan.append(f"Dekat support {tf} ({dekat['price']:.5f})")
        else:
            sell += w
            alasan.append(f"Dekat resistance {tf} ({dekat['price']:.5f})")

    rsi_map = {}
    for tf in C.RSI_TFS:
        v = rsi([x["c"] for x in data[tf]])
        rsi_map[tf] = v
        if v is None:
            continue
        w = C.RSI_WEIGHTS[tf]
        if v < C.RSI_OVERSOLD:
            buy += w
            alasan.append(f"RSI {tf} oversold ({v})")
        elif v > C.RSI_OVERBOUGHT:
            sell += w
            alasan.append(f"RSI {tf} overbought ({v})")

    tren = get_trend(data, price)
    keputusan, skor = "NETRAL", max(buy, sell)
    if buy != sell and max(buy, sell) >= C.THRESHOLD and abs(buy - sell) >= C.MIN_DIFF:
        arah = "BUY" if buy > sell else "SELL"
        if (arah == "BUY" and tren == "NAIK") or (arah == "SELL" and tren == "TURUN"):
            keputusan = arah
            skor = buy if arah == "BUY" else sell
        else:
            alasan.append(f"Ditolak filter tren ({tren})")
    if not alasan:
        alasan.append("Tidak ada sinyal kuat")

    lvl = None
    if keputusan != "NETRAL":
        jenis = "S" if keputusan == "BUY" else "R"
        kand = [x for x in semua_level if x["type"] == jenis]
        if kand:
            b = min(kand, key=lambda x: abs(price - x["price"]))
            lvl = {"type": jenis, "price": round(b["price"], 5), "tf": b["tf"]}

    return {"keputusan": keputusan, "skor": skor, "alasan": alasan,
            "level": lvl, "rsi": rsi_map, "tren": tren}
