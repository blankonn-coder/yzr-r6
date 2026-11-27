"""Mesin skema final: indikator, persiapan data, trigger, korelasi, filter, dan keputusan.

Dipakai bersama oleh live (main.py) dan backtest (backtest.py), jadi hasilnya identik.
Korelasi memakai prefix sum: setiap jendela dihitung O(1), tidak mengulang loop per bar.
"""
import bisect
import math
import statistics
from datetime import datetime, timezone

import config as C


# ---------------- indikator (causal: nilai bar i hanya memakai bar <= i) ----------------

def ema(vals, n):
    out = [None] * len(vals)
    if len(vals) < n:
        return out
    k = 2.0 / (n + 1)
    s = sum(vals[:n]) / n
    out[n - 1] = s
    for i in range(n, len(vals)):
        s = vals[i] * k + s * (1 - k)
        out[i] = s
    return out


def atr(cs, n):
    """ATR Wilder dari candle {"h","l","c"}."""
    out = [None] * len(cs)
    if len(cs) <= n:
        return out
    tr = [cs[0]["h"] - cs[0]["l"]]
    for i in range(1, len(cs)):
        pc = cs[i - 1]["c"]
        tr.append(max(cs[i]["h"] - cs[i]["l"], abs(cs[i]["h"] - pc), abs(cs[i]["l"] - pc)))
    s = sum(tr[1:n + 1]) / n
    out[n] = s
    for i in range(n + 1, len(cs)):
        s = (s * (n - 1) + tr[i]) / n
        out[i] = s
    return out


def _sma(vals, n):
    out = [None] * len(vals)
    for i in range(n - 1, len(vals)):
        win = vals[i - n + 1:i + 1]
        if None not in win:
            out[i] = sum(win) / n
    return out


def stoch(cs):
    """Stochastic %K (dihaluskan) dan %D."""
    raw = [None] * len(cs)
    for i in range(C.STOCH_K - 1, len(cs)):
        w = cs[i - C.STOCH_K + 1:i + 1]
        hh, ll = max(x["h"] for x in w), min(x["l"] for x in w)
        raw[i] = 50.0 if hh == ll else 100 * (cs[i]["c"] - ll) / (hh - ll)
    k = _sma(raw, C.STOCH_SMOOTH)
    return k, _sma(k, C.STOCH_D)


def log_returns(closes):
    out = [None] * len(closes)
    for i in range(1, len(closes)):
        out[i] = math.log(closes[i] / closes[i - 1])
    return out


def _sign(x):
    return 0 if x is None or x == 0 else (1 if x > 0 else -1)


# ---------------- persiapan data ----------------

def h4_trend(t_m15, h4):
    """Tren H4 per bar M15: sign(close - EMA50) dari bar H4 yang sudah tutup (ht + 4h <= t + 15m)."""
    opens = [c["t"] for c in h4]
    closes = [c["c"] for c in h4]
    e = ema(closes, C.EMA_N)
    out = []
    for t in t_m15:
        j = bisect.bisect_right(opens, t + C.TF_SEC - C.TF_H4_SEC) - 1
        if j < 0 or e[j] is None:
            out.append(None)
        else:
            out.append(_sign(closes[j] - e[j]))
    return out


def persentil_atr(atr_s, win):
    """Persentil tiap bar ATR terhadap win nilai ATR terakhir (termasuk bar itu). None jika belum cukup.
    Sliding window dengan daftar terurut: O(n log win), tidak mengulang loop per bar."""
    out, buf, ordered = [None] * len(atr_s), [], []
    for i, a in enumerate(atr_s):
        if a is None:
            continue
        buf.append(a)
        bisect.insort(ordered, a)
        if len(buf) > win:
            old = buf.pop(0)
            del ordered[bisect.bisect_left(ordered, old)]
        if len(buf) == win:
            out[i] = 100.0 * bisect.bisect_right(ordered, a) / win
    return out


def build(raw, h4):
    """raw: {pair: candle M15}. h4: candle H4 pemicu. Semua pair disejajarkan ke timestamp yang sama."""
    common = None
    for pair in C.PAIRS:
        ts = {c["t"] for c in raw[pair]}
        common = ts if common is None else common & ts
    t = sorted(common)
    p = {}
    for pair in C.PAIRS:
        by_t = {c["t"]: c for c in raw[pair]}
        cs = [by_t[x] for x in t]
        closes = [c["c"] for c in cs]
        lr = log_returns(closes)
        lr[0] = 0.0                       # tidak dipakai: jendela korelasi selalu mulai dari bar >= 1
        p[pair] = {"c": closes, "h": [c["h"] for c in cs], "l": [c["l"] for c in cs],
                   "ema": ema(closes, C.EMA_N), "atr": atr(cs, C.ATR_N), "lr": lr}
    e = p[C.PEMICU]
    for pair in C.PAIRS:
        q = p[pair]
        q["s1"], q["s2"], q["sxy"] = _prefix(q["lr"], e["lr"], pair != C.PEMICU)
    e["k"], e["d"] = stoch([{"h": a, "l": b, "c": c} for a, b, c in zip(e["h"], e["l"], e["c"])])
    e["ema_cepat"] = ema(e["c"], C.EMA_TRIGGER_CEPAT)
    e["pct"] = persentil_atr(e["atr"], C.ATR_PCT_WIN)
    return {"t": t, "p": p, "h4": h4_trend(t, h4),
            "sinkron": bool(t) and t[-1] == max(c["t"] for c in raw[C.PEMICU])}


def _prefix(lr, ref, cross):
    """Prefix sum: s1 = sum x, s2 = sum x^2, sxy = sum x*ref (x = lr pair)."""
    n = len(lr)
    s1, s2, sxy = [0.0] * (n + 1), [0.0] * (n + 1), [0.0] * (n + 1)
    for k in range(n):
        x = lr[k]
        s1[k + 1] = s1[k] + x
        s2[k + 1] = s2[k] + x * x
        sxy[k + 1] = sxy[k] + (x * ref[k] if cross else 0.0)
    return s1, s2, sxy


# ---------------- korelasi ----------------

def pearson(x, y):
    """Pearson biasa untuk daftar pendek (dipakai lead-lag saja)."""
    n = len(x)
    if n < 3:
        return None
    mx, my = sum(x) / n, sum(y) / n
    sxy = sum((a - mx) * (b - my) for a, b in zip(x, y))
    sxx = sum((a - mx) ** 2 for a in x)
    syy = sum((b - my) ** 2 for b in y)
    if sxx <= 0 or syy <= 0:
        return None
    return sxy / math.sqrt(sxx * syy)


def corr(prep, pair, i, w):
    """Korelasi return EUR/USD vs pair pada jendela w bar yang berakhir di i, lewat prefix sum."""
    if i - w + 1 < 1:
        return None
    a, b = i - w + 1, i + 1
    e, q = prep["p"][C.PEMICU], prep["p"][pair]
    sx, sy = e["s1"][b] - e["s1"][a], q["s1"][b] - q["s1"][a]
    vx = e["s2"][b] - e["s2"][a] - sx * sx / w
    vy = q["s2"][b] - q["s2"][a] - sy * sy / w
    if vx <= 1e-15 or vy <= 1e-15:
        return None
    cov = q["sxy"][b] - q["sxy"][a] - sx * sy / w
    return cov / math.sqrt(vx * vy)


def corr_adapt(prep, pair, i):
    cs = {w: corr(prep, pair, i, w) for w in C.CORR_WIN}
    if any(v is None for v in cs.values()):
        return None
    adapt = sum(b * cs[w] for b, w in zip(C.CORR_BOBOT, C.CORR_WIN))
    w0, w1, w2 = C.CORR_WIN
    return {"c50": cs[w0], "c200": cs[w1], "c500": cs[w2], "adapt": adapt}   # kunci nama lama, nilai ikut CORR_WIN


def stability(prep, pair, i):
    vals = [corr(prep, pair, j, C.CORR_WIN[0]) for j in range(i - C.STAB_WIN + 1, i + 1)]
    if None in vals:
        return None
    mu = sum(vals) / len(vals)
    sd = math.sqrt(sum((v - mu) ** 2 for v in vals) / len(vals))
    return max(0.0, min(1.0, 1 - sd))


def weights(prep, i):
    """Bobot adaptif (§7). Bobot nol jika korelasi runtuh atau tidak ada pair positif."""
    pairs, raw = {}, {}
    for pair in C.KONFIRMASI:
        ca = corr_adapt(prep, pair, i)
        st = stability(prep, pair, i)
        lr_now = prep["p"][pair]["lr"][i]
        rec = {"c50": None, "c200": None, "c500": None, "adapt": None, "stab": None,
               "w_raw": 0.0, "w": 0.0, "dir": _sign(lr_now)}
        if ca is not None:
            rec.update({k: round(v, 4) for k, v in ca.items()})
            if st is not None:
                rec["stab"] = round(st, 4)
                rec["w_raw"] = max(0.0, ca["adapt"]) * st * C.LIKUIDITAS.get(pair, C.LIKUIDITAS_DEFAULT)
        pairs[pair] = rec
        raw[pair] = rec["w_raw"]
    c50 = [abs(pairs[p]["c50"]) for p in C.KONFIRMASI if pairs[p]["c50"] is not None]
    rata = sum(c50) / len(c50) if c50 else 0.0
    kolaps = rata < C.KORELASI_MIN or not c50
    total = sum(raw.values())
    ok = not kolaps and total > 0
    for pair, rec in pairs.items():
        if ok:
            rec["w"] = round(raw[pair] / total, 6)
        rec["w_raw"] = round(rec["w_raw"], 6)
    return {"pairs": pairs, "rata_c50": round(rata, 4), "kolaps": kolaps, "ok": ok}


def score(wd, prep, i):
    """Confirmation score (§8): sum(w_i * sign(return_i) * sign(corr_adapt_i)).

    Direction trigger TIDAK dikalikan (lihat README), agar threshold BUY (>= q70) dan SELL (<= q30) konsisten.
    """
    total = 0.0
    for pair, rec in wd["pairs"].items():
        if rec["w"] > 0:
            total += rec["w"] * _sign(prep["p"][pair]["lr"][i]) * _sign(rec["adapt"])
    return round(total, 6)


def leadlag(prep, pair, i):
    """Lag dengan |korelasi| tertinggi (§6). lag > 0: pair mengikuti EUR/USD. Hanya informasi."""
    e, lr = prep["p"][C.PEMICU]["lr"], prep["p"][pair]["lr"]
    m = max(abs(x) for x in C.LAGS)
    t0, t1 = i - C.LEADLAG_WIN + 1, i - m
    if t0 - m < 1:
        return None
    best = None
    for lag in sorted(C.LAGS, key=lambda x: (abs(x), x)):
        r = pearson([e[t] for t in range(t0, t1 + 1)], [lr[t + lag] for t in range(t0, t1 + 1)])
        if r is not None and (best is None or abs(r) > abs(best["corr"])):
            best = {"lag": lag, "corr": round(r, 4)}
    return best


def leadlag_summary(prep, i):
    per = {pair: leadlag(prep, pair, i) for pair in C.KONFIRMASI}
    lags = [v["lag"] for v in per.values() if v]
    return {"per_pair": per,
            "eur_layak_pemantik": sum(x > 0 for x in lags) > sum(x < 0 for x in lags) if lags else None}


# ---------------- trigger (§4) ----------------

def zona_stoch(k, i):
    """Zona jenuh beli/jual. Adaptif: persentil K dalam STOCH_WIN bar terakhir (sampai bar i)."""
    if not C.STOCH_ADAPTIF:
        return C.STOCH_OS, C.STOCH_OB
    win = sorted(x for x in k[max(0, i - C.STOCH_WIN + 1):i + 1] if x is not None)
    if len(win) < C.STOCH_WIN // 2:
        return C.STOCH_OS, C.STOCH_OB
    return quantile(win, C.STOCH_Q_OS), quantile(win, C.STOCH_Q_OB)


def trigger(prep, i):
    """+1 BUY, -1 SELL, 0 tidak ada. Syarat murah dicek dulu, median ATR baru dihitung bila perlu."""
    p = prep["p"][C.PEMICU]
    k, d, pct = p["k"], p["d"], p["pct"][i]
    cepat = pct is not None and pct > C.EMA_PCT_SWITCH
    ema_v = p["ema_cepat"][i] if cepat else p["ema"][i]
    if i < 1 or pct is None or ema_v is None or None in (p["atr"][i], k[i], d[i], k[i - 1], d[i - 1]):
        return 0, {"alasan": "warm-up indikator"}
    close = p["c"][i]
    os_lvl, ob_lvl = zona_stoch(k, i)
    ema_up = close > ema_v or not C.TRIGGER_EMA_WAJIB
    ema_dn = close < ema_v or not C.TRIGGER_EMA_WAJIB
    cross_up = k[i - 1] <= d[i - 1] and k[i] > d[i] and k[i - 1] < os_lvl and ema_up
    cross_dn = k[i - 1] >= d[i - 1] and k[i] < d[i] and k[i - 1] > ob_lvl and ema_dn
    detail = {"ema": round(ema_v, 5), "ema_len": C.EMA_TRIGGER_CEPAT if cepat else C.EMA_TRIGGER_LAMBAT,
              "persentil_atr": round(pct, 1),
              "stoch": {"k": round(k[i], 2), "d": round(d[i], 2), "k_prev": round(k[i - 1], 2),
                        "zona_os": round(os_lvl, 1), "zona_ob": round(ob_lvl, 1)},
              "atr": round(p["atr"][i], 6), "atr_median": None, "close": round(close, 5)}
    if not (cross_up or cross_dn):
        return 0, {**detail, "alasan": "trigger tidak terpenuhi (EMA/stochastic)"}
    if C.ATR_MEDIAN_AKTIF:
        win = p["atr"][max(0, i - C.ATR_MED_N + 1):i + 1]
        if None in win or len(win) < C.ATR_MED_N:
            return 0, {"alasan": "warm-up median ATR"}
        med = statistics.median(win)
        detail["atr_median"] = round(med, 6)
        if p["atr"][i] <= med:
            return 0, {**detail, "alasan": "trigger tidak terpenuhi (ATR di bawah median)"}
    return (1 if cross_up else -1), detail


# ---------------- regime (§9) ----------------

def atr_percentile(prep, i):
    return prep["p"][C.PEMICU]["pct"][i]


def regime(prep, i, d, news_bersih, wd):
    cek = []

    def add(nama, lulus, detail):
        cek.append({"nama": nama, "lulus": bool(lulus), "detail": detail})

    pct = atr_percentile(prep, i)
    add("volatilitas ATR", pct is not None and C.ATR_PCT_MIN <= pct <= C.ATR_PCT_MAX,
        "belum cukup histori ATR" if pct is None else f"persentil {pct:.1f} (batas {C.ATR_PCT_MIN}-{C.ATR_PCT_MAX})")
    trend = prep["h4"][i]
    add("tren H4", trend is not None and trend == d,
        f"{'BUY butuh close H4 > EMA50' if d > 0 else 'SELL butuh close H4 < EMA50'}; hasil "
        f"{'belum siap' if trend is None else f'{trend:+d}'}")
    if C.SPREAD_TERSEDIA:
        add("spread", False, "spread live belum diimplementasi")
    else:
        add("spread", True, "dilewati: data spread tidak tersedia")
    if news_bersih is None:
        add("kalender ekonomi", False, "kalender gagal diperiksa, entry ditahan")
    else:
        add("kalender ekonomi", news_bersih,
            "bersih dalam ±30 menit" if news_bersih else "ada news high-impact dalam ±30 menit")
    add("korelasi", not wd["kolaps"], f"rata-rata |corr_50| {wd['rata_c50']} (min {C.KORELASI_MIN})")
    return all(c["lulus"] for c in cek), cek


# ---------------- target (§10) dan entry (§11) ----------------

def quantile(sorted_vals, q):
    pos = q * (len(sorted_vals) - 1)
    lo, hi = math.floor(pos), math.ceil(pos)
    return sorted_vals[lo] + (sorted_vals[hi] - sorted_vals[lo]) * (pos - lo)


def thresholds(riwayat):
    """(threshold_buy, threshold_sell, aktif). Di bawah SKOR_MIN_SAMPEL, pakai default warm-up."""
    if len(riwayat) < C.SKOR_MIN_SAMPEL:
        return C.SKOR_WARMUP, C.SKOR_WARMUP, False
    s = sorted(riwayat)
    return round(quantile(s, C.SKOR_Q_BUY), 6), round(quantile(s, C.SKOR_Q_SELL), 6), True


def sisi(pair):
    """Arah pair terhadap EUR/USD dari eksposur mata uang: +1 searah EUR/USD, -1 berlawanan, 0 tidak ada eksposur.
    EUR/USD -> +1, EUR/JPY -> +1, GBP/USD -> +1, USD/JPY -> -1, USD/CHF -> -1, EUR/CHF tidak dipakai."""
    base, quote = pair.split("_")
    return _sign(C.EKSPOSUR.get(base, 0) - C.EKSPOSUR.get(quote, 0))


def corr_bertahan(prep, pair, i):
    """Syarat §10D: corr_adapt > CORR_PERSIST_MIN di setiap bar dari CORR_PERSIST_BAR bar terakhir."""
    for j in range(i - C.CORR_PERSIST_BAR + 1, i + 1):
        ca = corr_adapt(prep, pair, j)
        if ca is None or ca["adapt"] <= C.CORR_PERSIST_MIN:
            return False
    return True


def target_check(prep, i, d, pair):
    """Konfirmasi satu target. d = arah trigger. Return (ok, detail).
    Spesifikasi: EUR/JPY aligned (USD/JPY tidak berlawanan), EUR/GBP divergent (GBP/USD tidak searah).
    Pair lain (aturan generik): return terakhir pair searah arah trade. Semua: close di sisi EMA50 arah trade."""
    ds = d * sisi(pair)
    t = prep["p"][pair]
    ema_v = t["ema"][i]
    ema_ok = ema_v is not None and ((t["c"][i] > ema_v) if ds > 0 else (t["c"][i] < ema_v))
    detail = {"target": C.disp(pair), "arah_trade": ds,
              "ema50": None if ema_v is None else round(ema_v, C.desimal(pair))}
    if pair in C.TARGET_RULES:
        ref, sgn = C.TARGET_RULES[pair]
        cnt = _sign(prep["p"][ref]["lr"][i])
        dir_ok = cnt * d * sgn >= 0
        detail.update(logika="aligned" if sgn > 0 else "divergent", pair_konfirmasi=C.disp(ref))
    else:
        cnt = _sign(t["lr"][i])
        dir_ok = cnt * ds >= 0
        detail.update(logika="generik", pair_konfirmasi="return sendiri")
    detail.update(arah_konfirmasi=cnt, syarat_ok=dir_ok, ema_ok=ema_ok)
    # Aturan generik (non-spesifikasi): syarat EMA50 tidak dipakai, agar entry lebih sering (keputusan pengguna).
    ema_wajib = pair in C.TARGET_RULES and C.EMA_WAJIB_SPESIFIKASI
    detail["ema_wajib"] = ema_wajib
    ema_lolos = ema_ok or not ema_wajib
    persist_ok = True
    if C.CORR_PERSIST_AKTIF and pair in C.CORR_PERSIST_PAIRS and dir_ok and ema_lolos:   # syarat mahal hanya bila syarat murah lolos
        persist_ok = corr_bertahan(prep, pair, i)
        detail["corr_bertahan"] = persist_ok
    return dir_ok and ema_lolos and persist_ok, detail


def entry_levels(prep, i, d, pair):
    """Entry = close M15 pair. SL = clamp(1.5 x ATR, 10, 15) pip. TP = 10 pip. d = arah trade pair itu."""
    t = prep["p"][pair]
    pip, dec = C.pip_size(pair), C.desimal(pair)
    if t["atr"][i] is None:
        return None
    sl_pip = round(min(C.SL_MAX_PIP, max(C.SL_MIN_PIP, C.SL_ATR_MULT * t["atr"][i] / pip)), 1)
    entry = round(t["c"][i], dec)
    return {"entry": entry, "sl": round(entry - d * sl_pip * pip, dec), "tp": round(entry + d * C.TP_PIP * pip, dec),
            "sl_pip": sl_pip, "tp_pip": C.TP_PIP, "atr_pip": round(t["atr"][i] / pip, 1)}


# ---------------- keputusan satu bar ----------------

def bar_time(t):
    return C.fmt(datetime.fromtimestamp(t, timezone.utc))


def analyze(prep, i, riwayat, news_bersih, posisi_pairs=(), posisi_total=0):
    """Return (hasil, skor). skor None jika tidak ada trigger atau bobot nol (riwayat tidak berubah).

    Trigger, skor, dan regime dihitung sekali (gerbang bersama). Tiap target dicek sendiri.
    Batas posisi dihitung dari posisi aktif plus entry yang sudah diterima pada bar ini,
    urut sesuai C.TARGETS. posisi_pairs berisi kunci pair seperti 'EUR_JPY'.
    hasil["entri"] berisi target yang lolos semua syarat; hasil["targets"] berisi semua target untuk laporan."""
    res = {"bar_terakhir": bar_time(prep["t"][i]), "harga_pemicu": round(prep["p"][C.PEMICU]["c"][i], 5),
           "label": "NO SIGNAL", "decision": "NO_SIGNAL", "status": "Trigger EUR/USD tidak ada",
           "alasan": [], "targets": [], "entri": [], "bar_terpakai": len(prep["t"])}
    d, tdet = trigger(prep, i)
    res["trigger"] = {"arah": {1: "BUY", -1: "SELL"}.get(d, "-"), **tdet}
    if d == 0:
        res["alasan"].append(tdet["alasan"])
        return res, None

    res.update(label="NO TRADE", decision="NO_TRADE", status="Trigger ada - ditahan")
    wd = weights(prep, i)
    res["bobot"] = {"rata_c50": wd["rata_c50"], "kolaps": wd["kolaps"],
                    "pair": {k.replace("_", "/"): v for k, v in wd["pairs"].items()}}
    sc = None
    if not wd["ok"]:
        res["alasan"].append("sum bobot = 0 (korelasi runtuh atau corr_adapt negatif)")
    else:
        sc = score(wd, prep, i)
        tb, ts, aktif = thresholds(riwayat)
        skor_ok = sc >= tb if d > 0 else sc <= ts
        res["skor"] = {"nilai": sc, "threshold_buy": tb, "threshold_sell": ts,
                       "riwayat": len(riwayat), "threshold_aktif": aktif, "lulus": skor_ok}
        if not skor_ok:
            res["alasan"].append(f"skor {sc} {'<' if d > 0 else '>'} threshold {tb if d > 0 else ts}")
        regime_ok, cek = regime(prep, i, d, news_bersih, wd)
        res["regime"] = {"lulus": regime_ok, "cek": cek}
        res["alasan"] += [f"{c['nama']}: {c['detail']}" for c in cek if not c["lulus"]]

    terbuka, total = set(posisi_pairs), posisi_total
    for pair in C.TARGETS:
        ok, tc = target_check(prep, i, d, pair)
        ds = tc["arah_trade"]
        alasan = []
        if not ok:
            gagal = []
            if not tc["syarat_ok"]:
                gagal.append(f"arah {tc['pair_konfirmasi']}" if tc["logika"] == "generik"
                             else f"arah vs {tc['pair_konfirmasi']}")
            if not tc["ema_ok"] and tc["ema_wajib"]:
                gagal.append("close vs EMA50")
            if tc.get("corr_bertahan") is False:
                gagal.append(f"corr_adapt > {C.CORR_PERSIST_MIN} tidak bertahan {C.CORR_PERSIST_BAR} bar")
            alasan.append("konfirmasi tidak mendukung: " + ", ".join(gagal))
        if pair in terbuka:
            alasan.append(f"posisi {C.disp(pair)} masih dipantau (maks {C.MAKS_PER_PAIR} per pair)")
        if total >= C.MAKS_TOTAL:
            alasan.append(f"posisi terbuka {total} (maks {C.MAKS_TOTAL})")
        lv = entry_levels(prep, i, ds, pair) if ds != 0 else None
        if lv is None:
            alasan.append("ATR target belum tersedia atau arah tidak ada (EUR/USD tidak memuat mata uang ini)")
        row = {"pair": C.disp(pair), "key": pair, "arah": "BUY" if ds > 0 else ("SELL" if ds < 0 else "-"),
               "harga": round(prep["p"][pair]["c"][i], C.desimal(pair)), "bar_terakhir": res["bar_terakhir"],
               "entry": lv["entry"] if lv else None, "sl": lv["sl"] if lv else None,
               "tp": lv["tp"] if lv else None, "levels": lv, "alasan": alasan, "target_cek": tc}
        if not res["alasan"] and not alasan:
            row.update(label=f"ENTRY {'LONG' if ds > 0 else 'SHORT'}", decision=row["arah"],
                       metode="TRIGGER M15 + KONFIRMASI")
            terbuka.add(pair)
            total += 1
            res["entri"].append(row)
        else:
            row.update(label="NO TRADE", decision="NO_TRADE", metode=None)
        res["targets"].append(row)

    if res["entri"]:
        res.update(label="ENTRY", decision=", ".join(r["pair"] + " " + r["decision"] for r in res["entri"]),
                   status=f"Semua syarat terpenuhi untuk {len(res['entri'])} target",
                   leadlag=leadlag_summary(prep, i))
    elif res["alasan"]:
        res["status"] = "Trigger ada - ditahan (gerbang bersama)"
    else:
        res["status"] = "Trigger ada - tidak ada target yang lolos"
    return res, sc
