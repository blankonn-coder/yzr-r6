"""Analisa cadangan (BUKAN sinyal).

Dipakai saat label NO TRADE atau WATCHLIST. Berisi:
1. Level support dan resistance terdekat dari swing H1 dan M15 untuk konteks scalping.
2. Saran BUY/SELL untuk N pair dengan level H1 terdekat, lengkap dengan entry, SL, dan TP.
   Saran ini hanya dari kedekatan harga ke level. Tidak divalidasi backtest, tidak memeriksa
   spread atau news, dan tidak memakai statistik ranking.
Pemantauan saran dan entry ada di pantauan.py.

Tidak mengubah label ENTRY/WATCHLIST/NO TRADE, ranking, atau keputusan apa pun.

Sentuhan = jumlah bar yang high-low-nya menyentuh area level (± TOUCH_ATR x ATR).
"""
import json
import os

import config as C
from indicators import atr, ok

SWING_LB = 2        # pivot: lebih tinggi/rendah dari 2 bar kiri dan kanan
CLUSTER_ATR = 0.5   # pivot yang berdekatan (dalam 0,5 ATR) digabung jadi satu level
TOUCH_ATR = 0.2     # area sentuh = level ± 0,2 ATR
MIN_TOUCH = 2       # level dengan minimal 2 sentuhan diutamakan


def _pivot_prices(cs, lb=SWING_LB):
    out = []
    for i in range(lb, len(cs) - lb):
        win = cs[i - lb:i + lb + 1]
        h, l = cs[i]["h"], cs[i]["l"]
        if h == max(x["h"] for x in win) and all(h > cs[j]["h"] for j in range(i - lb, i)):
            out.append(h)
        if l == min(x["l"] for x in win) and all(l < cs[j]["l"] for j in range(i - lb, i)):
            out.append(l)
    return out


def _levels(cs, a):
    groups = []
    for p in sorted(_pivot_prices(cs)):
        if groups and p - groups[-1][-1] <= CLUSTER_ATR * a:
            groups[-1].append(p)
        else:
            groups.append([p])
    tol = TOUCH_ATR * a
    out = []
    for g in groups:
        lvl = sum(g) / len(g)
        sentuh, last = 0, None
        for i, c in enumerate(cs):
            if c["h"] >= lvl - tol and c["l"] <= lvl + tol:
                sentuh += 1
                last = i
        out.append({"harga": lvl, "sentuhan": sentuh,
                    "umur_bar": (len(cs) - 1 - last) if last is not None else None})
    return out


def _analisa(cs, tf, max_atr):
    a = atr(cs)[-1]
    if not ok(a) or a <= 0:
        return None
    price = cs[-1]["c"]
    lv = _levels(cs, a)

    def dekat(x):
        return abs(x["harga"] - price) / a <= max_atr

    def pick(cands):
        if not cands:
            return None
        best = sorted(cands, key=lambda x: (x["sentuhan"] < MIN_TOUCH, abs(x["harga"] - price)))[0]
        return {"harga": round(best["harga"], 5), "jarak_atr": round(abs(best["harga"] - price) / a, 2),
                "sentuhan": best["sentuhan"], "umur_bar": best["umur_bar"]}

    return {"tf": tf, "atr": round(a, 5),
            "resistance": pick([x for x in lv if x["harga"] > price and dekat(x)]),
            "support": pick([x for x in lv if x["harga"] < price and dekat(x)])}


def build(h1, m15):
    """h1 wajib; m15 boleh None (gagal ambil). Return dict analisa cadangan."""
    return {"sumber": "biquote",
            "h1": _analisa(h1, "H1", C.CADANGAN_H1_MAX_ATR),
            "m15": _analisa(m15, "M15", C.CADANGAN_M15_MAX_ATR) if m15 else None,
            "m15_tersedia": m15 is not None}


# ---------- Pencatatan snapshot dan evaluasi (untuk menilai level ke depan) ----------

def _read_jsonl(path):
    if not os.path.exists(path):
        return []
    with open(path, encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


def _append_jsonl(path, recs):
    if not recs:
        return
    d = os.path.dirname(path)
    if d:
        os.makedirs(d, exist_ok=True)
    with open(path, "a", encoding="utf-8") as f:
        for r in recs:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")


def simpan_snapshot(now, rows):
    """Catat level yang ditampilkan untuk pair NO TRADE/WATCHLIST. Satu snapshot per bar."""
    sudah = {s["id"] for s in _read_jsonl(C.CADANGAN_SNAPSHOT_PATH)}
    baru = []
    for r in rows:
        if not r.get("cadangan") or r["label"] not in ("NO TRADE", "WATCHLIST") or not r.get("bar_terakhir"):
            continue
        sid = f"{r['pair'].replace('/', '_')}_{r['bar_terakhir']}"
        if sid in sudah:
            continue
        sudah.add(sid)
        baru.append({"id": sid, "waktu": C.fmt(now), "pair": r["pair"], "bar_terakhir": r["bar_terakhir"],
                     "harga": r["harga"], "label": r["label"], "cadangan": r["cadangan"]})
    _append_jsonl(C.CADANGAN_SNAPSHOT_PATH, baru)
    return len(baru)


def evaluasi(pair_disp, h1, now):
    """Catat apa yang terjadi setelah snapshot level H1: sentuh dalam 12 bar, dan perubahan harga
    dalam 1, 4, 12 bar (satuan ATR snapshot). Hanya snapshot yang bar setelahnya sudah lengkap."""
    sudah = {o["id"] for o in _read_jsonl(C.CADANGAN_OUTCOME_PATH)}
    idx = {c["t"]: i for i, c in enumerate(h1)}
    n_bar = max(C.CADANGAN_OUTCOME_BARS)
    baru = []
    for s in _read_jsonl(C.CADANGAN_SNAPSHOT_PATH):
        if s["pair"] != pair_disp or s["id"] in sudah:
            continue
        i0 = idx.get(C.to_epoch(s["bar_terakhir"]))
        if i0 is None or i0 + n_bar >= len(h1):
            continue  # bar setelahnya belum lengkap atau sudah keluar dari jendela data
        h1s = (s["cadangan"] or {}).get("h1")
        if not h1s:
            baru.append({"id": s["id"], "level": None, "dicatat": C.fmt(now)})
            continue
        for nama in ("resistance", "support"):
            lvl = h1s.get(nama)
            if not lvl:
                continue
            L = lvl["harga"]
            sentuh = any(h1[j]["h"] >= L and h1[j]["l"] <= L for j in range(i0 + 1, i0 + n_bar + 1))
            dlt = {f"{k}h": round((h1[i0 + k]["c"] - s["harga"]) / h1s["atr"], 2)
                   for k in C.CADANGAN_OUTCOME_BARS}
            baru.append({"id": s["id"], "level": nama, "harga_level": L, "sentuh_12h": sentuh,
                         "perubahan_atr": dlt, "dicatat": C.fmt(now)})
        if not any(r["id"] == s["id"] for r in baru):
            baru.append({"id": s["id"], "level": None, "dicatat": C.fmt(now)})
    _append_jsonl(C.CADANGAN_OUTCOME_PATH, baru)
    return len(baru)


# ---------- Saran buy/sell (BUKAN sinyal) ----------

def _pair_key(pair):
    return pair.replace("/", "_")


def _buat_saran(r, h1, nama, arah):
    """Saran dari satu level H1. BUY dari support (harga di atas level), SELL dari resistance."""
    lvl = h1[nama]
    a = h1["atr"]
    harga = r["harga"]
    if arah == "BUY":
        sl = lvl["harga"] - C.CADANGAN_SARAN_SL_ATR * a
        risk = harga - sl
        tp = harga + C.CADANGAN_SARAN_TP_R * risk
    else:
        sl = lvl["harga"] + C.CADANGAN_SARAN_SL_ATR * a
        risk = sl - harga
        tp = harga - C.CADANGAN_SARAN_TP_R * risk
    return {"pair": r["pair"], "arah": arah, "level": nama, "level_harga": round(lvl["harga"], 5),
            "jarak_atr": lvl["jarak_atr"], "sentuhan": lvl["sentuhan"],
            "entry": round(harga, 5), "sl": round(sl, 5), "tp": round(tp, 5),
            "sl_pip": round(risk / C.pip_size(_pair_key(r["pair"])), 1),
            "bar_terakhir": r["bar_terakhir"]}


def pilih_saran(rows, dikecualikan=()):
    """Pilih N pair dengan level H1 terdekat (jarak <= batas). Satu saran per pair.
    Level terdekat yang dipakai: support -> BUY, resistance -> SELL. Seri diurut dari sentuhan terbanyak.
    dikecualikan: pair yang masih dipantau, tidak dibuatkan saran baru."""
    calon = []
    for r in rows:
        h1 = (r.get("cadangan") or {}).get("h1")
        if not h1 or r["label"] == "DATA INVALID" or r["label"].startswith("ENTRY"):
            continue
        if r["pair"] in dikecualikan:
            continue
        for nama, arah in (("support", "BUY"), ("resistance", "SELL")):
            lvl = h1.get(nama)
            if lvl and lvl["jarak_atr"] <= C.CADANGAN_SARAN_MAX_ATR:
                calon.append((lvl["jarak_atr"], -lvl["sentuhan"], r, h1, nama, arah))
    calon.sort(key=lambda x: (x[0], x[1]))
    saran, sudah = [], set()
    for _, _, r, h1, nama, arah in calon:
        if r["pair"] in sudah:
            continue
        sudah.add(r["pair"])
        saran.append(_buat_saran(r, h1, nama, arah))
        if len(saran) == C.CADANGAN_SARAN_N:
            break
    return saran
