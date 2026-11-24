"""Lead-lag untuk analisa cadangan (BUKAN sinyal). Tidak mengubah label, ranking, atau mode entry.

Pair leader memicu pair follower yang merespons lebih lambat (5 sampai 60 menit).
1. Tiap run saat pasar buka: ambil candle M5 untuk LEADLAG_PAIRS dan gabungkan ke
   database/leadlag_backtest.json (bergulir, LEADLAG_RETENSI_BARS bar per pair).
2. Hanya jika TIDAK ada ENTRY di run ini: backtest korelasi return leader -> follower pada lag
   5..60 menit selama jendela 6 jam terakhir. Syarat sebuah pasangan lolos:
   - |korelasi| >= LEADLAG_MIN_CORR dan sampel >= LEADLAG_MIN_SAMPLE pada lag terbaik
   - korelasi di lag terbaik lebih kuat daripada korelasi di lag 0 (follower memang tertinggal)
3. Kandidat: leader sudah bergerak dalam k bar terakhir (z >= LEADLAG_TRIGGER_Z) dan follower
   belum bergerak searah (z < LEADLAG_FOLLOW_MAX_Z). Arah saran = arah leader x tanda korelasi.
4. SL dan TP memakai metode saran cadangan yang sudah ada (SL 0,5 ATR H1, TP 1,5R).

Semua fungsi di sini tidak melempar error ke pemanggil; kegagalan dicatat di field "status".
"""
import json
import math
import os
import statistics
from datetime import datetime, timezone

import config as C
from indicators import atr as hitung_atr

METODE = "LEAD-LAG"


# ---------- Statistik ----------

def _pearson(x, y):
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


def _ret(cs):
    """cs: [[t, c], ...] terurut. Return {t: return}, hanya untuk bar yang berurutan 5 menit."""
    out = {}
    for (t0, c0), (t1, c1) in zip(cs, cs[1:]):
        if t1 - t0 == C.TF_LEADLAG_SEC and c0:
            out[t1] = c1 / c0 - 1.0
    return out


def _jendela(end):
    return [end - i * C.TF_LEADLAG_SEC for i in range(C.LEADLAG_WINDOW_BARS)]


def _korelasi(ra, rb, lag, jendela):
    off = lag * C.TF_LEADLAG_SEC
    x, y = [], []
    for t in jendela:
        if t in ra and (t + off) in rb:
            x.append(ra[t])
            y.append(rb[t + off])
    return _pearson(x, y), len(x)


def _stabil(ra, rb, k, jendela, r):
    """Hubungan harus bertahan di kedua paruh jendela (3 jam): searah dengan r dan cukup kuat."""
    h = len(jendela) // 2
    for bagian in (jendela[:h], jendela[h:]):
        rh, _ = _korelasi(ra, rb, k, bagian)
        if rh is None or (rh > 0) != (r > 0) or abs(rh) < C.LEADLAG_STABIL_MIN_CORR:
            return False
    return True


def _lag_terbaik(ra, rb, jendela):
    r0, _ = _korelasi(ra, rb, 0, jendela)
    best = None
    for k in C.LEADLAG_LAGS:
        r, n = _korelasi(ra, rb, k, jendela)
        if r is None or n < C.LEADLAG_MIN_SAMPLE or abs(r) < C.LEADLAG_MIN_CORR:
            continue
        if r0 is not None and abs(r) <= abs(r0):
            continue  # follower tidak tertinggal: korelasi lag tidak lebih kuat dari lag 0
        if best is None or abs(r) > abs(best["korelasi"]):
            if _stabil(ra, rb, k, jendela, r):
                best = {"lag_bar": k, "lag_menit": k * 5, "korelasi": r, "n": n, "korelasi_lag0": r0}
    return best


def _sigma(r, jendela):
    v = [r[t] for t in jendela if t in r]
    return statistics.pstdev(v) if len(v) >= 3 else 0.0


def _z(r, end, k, sigma):
    """Gerak return kumulatif k bar terakhir, dinormalkan ke sigma per bar (z-score)."""
    if not sigma:
        return None
    vals = [r.get(end - i * C.TF_LEADLAG_SEC) for i in range(k)]
    if any(v is None for v in vals):
        return None
    return sum(vals) / (sigma * math.sqrt(k))


# ---------- Store (database/leadlag_backtest.json) ----------

def _muat_store():
    data = C.load_json(C.LEADLAG_PATH, {})
    return data.get("candles", {}), data.get("backtest")


def _gabung(lama, baru):
    """lama: [[t, c], ...]; baru: [{'t', 'c', ...}]. Bar baru menimpa bar lama dengan t yang sama."""
    peta = {t: c for t, c in lama}
    for b in baru:
        peta[b["t"]] = b["c"]
    ts = sorted(peta)[-C.LEADLAG_RETENSI_BARS:]
    return [[t, peta[t]] for t in ts]


def _simpan(data):
    d = os.path.dirname(C.LEADLAG_PATH)
    if d:
        os.makedirs(d, exist_ok=True)
    with open(C.LEADLAG_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, separators=(",", ":"))


# ---------- Backtest dan kandidat ----------

def hitung_backtest(candles, end):
    """candles: {pair_key: [[t, c], ...]}. Return (pasangan_lolos, lag_terbaik_per_pasangan, ret, sigma).

    Dipisah dari run utama agar bisa diuji dengan data sintetis.
    """
    ret = {k: _ret(cs) for k, cs in candles.items()}
    jend = _jendela(end)
    sigma = {k: _sigma(r, jend) for k, r in ret.items()}
    pasangan, lag_terbaik = [], {}
    for a in ret:
        for b in ret:
            if a == b:
                continue
            info = _lag_terbaik(ret[a], ret[b], jend)
            if info is None:
                continue
            lag_terbaik[(a, b)] = info
            pasangan.append({"leader": C.disp(a), "follower": C.disp(b), "lag_menit": info["lag_menit"],
                             "korelasi": round(info["korelasi"], 3), "korelasi_lag0": (
                                 None if info["korelasi_lag0"] is None else round(info["korelasi_lag0"], 3)),
                             "n": info["n"]})
    pasangan.sort(key=lambda x: -abs(x["korelasi"]))
    return pasangan, lag_terbaik, ret, sigma


def _buat_saran(pair_disp, bar_terakhir, a, b, info, arah_dir, atr, harga, t_terakhir):
    arah = "BUY" if arah_dir > 0 else "SELL"
    if arah == "BUY":
        sl = harga - C.CADANGAN_SARAN_SL_ATR * atr
        risk = harga - sl
        tp = harga + C.CADANGAN_SARAN_TP_R * risk
    else:
        sl = harga + C.CADANGAN_SARAN_SL_ATR * atr
        risk = sl - harga
        tp = harga - C.CADANGAN_SARAN_TP_R * risk
    mulai = datetime.fromtimestamp(t_terakhir + C.TF_LEADLAG_SEC, timezone.utc)
    return {"pair": pair_disp, "arah": arah, "metode": METODE,
            "leader": C.disp(a), "lag_menit": info["lag_menit"], "korelasi": round(info["korelasi"], 2),
            "n": info["n"], "level": None, "level_harga": None, "jarak_atr": None, "sentuhan": None,
            "entry": round(harga, 5), "sl": round(sl, 5), "tp": round(tp, 5),
            "sl_pip": round(risk / C.pip_size(b), 1), "bar_terakhir": bar_terakhir,
            "mulai": C.fmt(mulai)}


def kandidat(rows, candles, ret, sigma, lag_terbaik, end):
    """Satu kandidat terbaik per follower, diurut dari skor tertinggi.
    Skor = |korelasi| x |z leader|. ATR H1 dan bar terakhir diambil dari baris scanner follower."""
    peta_row = {r["pair"]: r for r in rows}
    terbaik = {}
    for (a, b), info in lag_terbaik.items():
        row = peta_row.get(C.disp(b))
        if not row or row["label"].startswith("ENTRY") or row["label"] == "DATA INVALID":
            continue  # follower hanya dari scanner; ENTRY dan data tidak valid dilewati
        if not candles.get(b):
            continue
        k = info["lag_bar"]
        za = _z(ret[a], end, k, sigma[a])
        zb = _z(ret[b], end, k, sigma[b])
        if za is None or zb is None or abs(za) < C.LEADLAG_TRIGGER_Z:
            continue
        arah_dir = (1 if za > 0 else -1) * (1 if info["korelasi"] > 0 else -1)
        if arah_dir * zb >= C.LEADLAG_FOLLOW_MAX_Z:
            continue  # follower sudah bergerak searah, tidak lagi tertinggal
        skor = abs(info["korelasi"]) * abs(za)
        if b in terbaik and terbaik[b][0] >= skor:
            continue
        atr = ((row.get("cadangan") or {}).get("h1") or {}).get("atr")
        if not atr or atr <= 0:
            continue
        bar_terakhir = row["bar_terakhir"]
        t_akhir, c_akhir = candles[b][-1]
        saran = _buat_saran(C.disp(b), bar_terakhir, a, b, info, arah_dir, atr, c_akhir, t_akhir)
        saran["skor"] = round(skor, 3)
        saran["z_leader"] = round(za, 2)
        terbaik[b] = (skor, saran)
    return [s for _, s in sorted(terbaik.values(), key=lambda x: -x[0])]


# ---------- Titik masuk utama ----------

def jalankan(now, rows, ambil, analisa):
    """Satu run. ambil(pair_key) -> list candle M5 dengan kunci t dan c, atau raise.
    analisa=False saat ada ENTRY: data tetap diperbarui, backtest dan saran tidak dihitung.

    Return: {"saran": [...], "backtest": {...} | None, "status": str, "gagal": [...]}
    """
    if not C.LEADLAG_ENABLED:
        return {"saran": [], "backtest": None, "status": "dimatikan", "gagal": []}
    try:
        candles, backtest_lama = _muat_store()
        gagal = []
        for key in C.LEADLAG_UNIVERSE:
            try:
                baru = ambil(key)
            except Exception:
                gagal.append(C.disp(key))
                continue
            if baru:
                candles[key] = _gabung(candles.get(key, []), baru)
            else:
                gagal.append(C.disp(key))

        ujung = [cs[-1][0] for cs in candles.values() if cs]
        if not ujung:
            return {"saran": [], "backtest": backtest_lama, "status": "tidak ada data M5", "gagal": gagal}
        end = max(ujung)

        if analisa:
            pasangan, lag_terbaik, ret, sigma = hitung_backtest(candles, end)
            kand = kandidat(rows, candles, ret, sigma, lag_terbaik, end)
            backtest = {"diperbarui": C.fmt(now), "jendela_menit": C.LEADLAG_WINDOW_BARS * C.TF_LEADLAG_SEC // 60,
                        "jumlah_lolos": len(pasangan), "pasangan_lolos": pasangan[:30],
                        "kandidat": kand}
            status = "dianalisa"
            saran = kand[:C.LEADLAG_SARAN_N]
        else:
            backtest, saran = backtest_lama, []
            status = "dilewati: ada ENTRY di run ini (data tetap diperbarui)"

        _simpan({"diperbarui": C.fmt(now), "pair_gagal": gagal, "backtest": backtest, "candles": candles})
        return {"saran": saran, "backtest": backtest, "status": status, "gagal": gagal}
    except Exception as e:  # tidak boleh menghentikan run; nama error saja, tanpa detail
        return {"saran": [], "backtest": None, "status": f"error {type(e).__name__}", "gagal": []}
