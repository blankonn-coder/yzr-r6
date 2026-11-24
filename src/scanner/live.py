"""Scanner live adaptif (tahap 4, bagian 8-10 skema).

Alur per pair (dijalankan setelah candle H1 close):
  1. Ambil H1 dan H4 dari biquote (hanya candle tertutup).
  2. Validasi data. Gagal -> DATA INVALID.
  3. Hitung indikator, regime, dan bias H4.
  4. Ambil metode berperingkat PRIORITAS untuk pair + regime saat ini, urut bintang tertinggi.
  5. Cek trigger metode pada bar terakhir yang sudah close.
  6. Cek news (biquote calendar). Gagal diperiksa -> tidak ada ENTRY baru.
  7. Spread: belum bisa diverifikasi (biquote tidak memberi bid/ask). Sinyal tetap WATCHLIST
     sampai sumber spread (OANDA) disambungkan.

Label: ENTRY LONG / ENTRY SHORT / WATCHLIST / NO TRADE / DATA INVALID.
"""
import json
import os
from datetime import datetime, timedelta, timezone

import numpy as np
import pandas as pd
import requests

from .. import config as C
from ..biquote_client import fetch_candles
from ..data.validate import check_candles
from ..indicators import build
from ..methods import METODE
from ..regime import classify
from ..resample import bias_h4

RANKING_PATH = "results/ranking/ranking.json"
LAPORAN_JSON = "results/scanner/latest.json"
LAPORAN_MD = "reports/scanner_latest.md"
NEWS_MENIT = 30
SPREAD_TERSEDIA = False       # ubah ke True setelah OANDA disambungkan dan diuji
MAKS_UMUR_BAR_JAM = 2         # candle terakhir lebih tua dari ini = data basi
CALENDAR_URL = "https://biquote.io/api/calendar"


def _waktu(s):
    if pd.api.types.is_numeric_dtype(s):
        return pd.to_datetime(s, unit="ms", utc=True)
    return pd.to_datetime(s, utc=True)


def ambil(pair, interval, count):
    bars = fetch_candles(pair, interval, count=count)
    df = pd.DataFrame(bars)
    df["time"] = _waktu(df["time"])
    return df


def ambil_data(pair):
    """Return (h1, h4, error). error berisi alasan DATA INVALID bila ada."""
    try:
        h1 = ambil(pair, "1h", 600)
        h4 = ambil(pair, "4h", 300)
    except Exception as e:
        return None, None, f"gagal ambil data: {e}"
    rep = check_candles(h1)
    if not rep["lolos"]:
        return None, None, "H1 tidak lolos validasi: " + ", ".join(rep["alasan"])
    umur = datetime.now(timezone.utc) - h1["time"].iloc[-1].to_pydatetime()
    if umur > timedelta(hours=MAKS_UMUR_BAR_JAM + 1):
        return None, None, f"candle H1 terakhir terlalu lama ({umur})"
    return h1, h4, None


def cek_news(pair, sekarang):
    """Return (diblokir, ok). ok=False jika kalender tidak bisa diperiksa."""
    mata_uang = {pair.split("_")[0], pair.split("_")[1]}
    try:
        r = requests.get(CALENDAR_URL, params={"importance": "high", "from": (sekarang - timedelta(hours=1)).isoformat(),
                                               "to": (sekarang + timedelta(hours=1)).isoformat()}, timeout=20)
        r.raise_for_status()
        events = r.json()
        if not isinstance(events, list):
            return False, False
    except Exception:
        return False, False
    for e in events:
        if e.get("currency") not in mata_uang or not e.get("time"):
            continue
        t = pd.to_datetime(e["time"], utc=True).to_pydatetime()
        if abs((t - sekarang).total_seconds()) <= NEWS_MENIT * 60:
            return True, True
    return False, True


def muat_ranking():
    if not os.path.exists(RANKING_PATH):
        return []
    with open(RANKING_PATH, encoding="utf-8") as f:
        return json.load(f).get("baris", [])


def _sinyal_metode(kode, h1, h4_bias, pip):
    sig = METODE[kode].signals(h1, pip, h4_bias=h4_bias).reset_index(drop=True)
    last = sig.iloc[-1]
    return int(last["direction"]), float(last["sl_dist"]) if pd.notna(last["sl_dist"]) else None, str(last["reason"])


def evaluasi(pair, h1, h4, ranking, sekarang, pip=None):
    """Return dict hasil satu pair (label, metode, rencana, alasan)."""
    pip = pip or C.pip_size(pair)
    h4_bias = bias_h4(h4)
    ind = build(h1)
    reg = classify(ind)
    regime = reg["regime"].iloc[-1]
    base = {"pair": pair, "regime": regime, "waktu_bar": str(h1["time"].iloc[-1]), "label": "NO TRADE",
            "metode": None, "bintang": 0, "arah": None, "rencana": None, "alasan": []}

    cand = [r for r in ranking if r["pair"] == pair and r["regime"] == regime and r.get("status") == "PRIORITAS"]
    if not cand:
        base["alasan"].append(f"tidak ada metode PRIORITAS untuk regime {regime}")
        return base
    cand.sort(key=lambda r: (-r["bintang"], -r.get("skor", 0)))

    pemicu = None
    for r in cand:
        arah_cand = 1 if r["arah"] == "LONG" else -1
        d, sl_dist, alasan = _sinyal_metode(r["metode"], h1, h4_bias, pip)
        if d == arah_cand and sl_dist:
            pemicu = (r, d, sl_dist, alasan)
            break
    if pemicu is None:
        base["label"] = "WATCHLIST" if cand else "NO TRADE"
        base["metode"] = cand[0]["metode"]
        base["bintang"] = cand[0]["bintang"]
        base["alasan"].append("metode berperingkat ada, trigger belum terkonfirmasi di bar terakhir")
        return base

    r, d, sl_dist, alasan = pemicu
    harga = float(h1["close"].iloc[-1])
    rr = {"A": 1.5, "B": 2.0, "C": 2.0, "D": 1.5, "E": 2.0}[r["metode"]]
    sl = harga - d * sl_dist
    tp = harga + d * rr * sl_dist
    base.update({
        "metode": r["metode"], "bintang": r["bintang"], "arah": "LONG" if d == 1 else "SHORT",
        "rencana": {"harga_acuan": round(harga, 5), "sl": round(sl, 5), "tp": round(tp, 5),
                    "risk_pip": round(sl_dist / pip, 1), "rr": rr},
        "alasan": [alasan, f"metode {r['metode']} bintang {r['bintang']} untuk {pair} {regime}"],
    })

    diblokir, news_ok = cek_news(pair, sekarang)
    if not news_ok:
        base["label"] = "WATCHLIST"
        base["alasan"].append("kalender ekonomi tidak bisa diperiksa, tidak ada ENTRY baru")
    elif diblokir:
        base["label"] = "WATCHLIST"
        base["alasan"].append("news high-impact dalam jendela ±30 menit")
    elif not SPREAD_TERSEDIA:
        base["label"] = "WATCHLIST"
        base["alasan"].append("spread belum bisa diverifikasi (OANDA belum terhubung)")
    else:
        base["label"] = "ENTRY LONG" if d == 1 else "ENTRY SHORT"
    return base


def jalankan(pairs):
    sekarang = datetime.now(timezone.utc)
    ranking = muat_ranking()
    hasil = []
    catatan = []
    if not ranking:
        catatan.append("ranking backtest belum tersedia (results/ranking/ranking.json)")
    for pair in pairs:
        h1, h4, err = ambil_data(pair)
        if err:
            hasil.append({"pair": pair, "label": "DATA INVALID", "alasan": [err]})
            continue
        hasil.append(evaluasi(pair, h1, h4, ranking, sekarang))
    return {"waktu": sekarang.strftime("%Y-%m-%dT%H:%M:%SZ"), "catatan": catatan, "hasil": hasil}


def tulis(laporan):
    os.makedirs(os.path.dirname(LAPORAN_JSON), exist_ok=True)
    os.makedirs(os.path.dirname(LAPORAN_MD), exist_ok=True)
    with open(LAPORAN_JSON, "w", encoding="utf-8") as f:
        json.dump(laporan, f, ensure_ascii=False, indent=2, default=str)
    with open(LAPORAN_MD, "w", encoding="utf-8") as f:
        f.write(f"# Adaptive Forex Scanner\nWaktu: {laporan['waktu']}\n\n")
        for c in laporan["catatan"]:
            f.write(f"> {c}\n")
        f.write("\n")
        for h in laporan["hasil"]:
            f.write(f"## {h['pair'].replace('_', '/')}: {h['label']}\n")
            if h.get("metode"):
                f.write(f"- Metode: {h['metode']} ({'★' * h['bintang']}{'☆' * (5 - h['bintang'])})\n")
                f.write(f"- Regime: {h.get('regime')}\n")
            if h.get("arah"):
                f.write(f"- Arah: {h['arah']}\n")
            if h.get("rencana"):
                p = h["rencana"]
                f.write(f"- Acuan {p['harga_acuan']} | SL {p['sl']} | TP {p['tp']} | RR 1:{p['rr']} | risiko {p['risk_pip']} pip\n")
            for a in h.get("alasan", []):
                f.write(f"- {a}\n")
            f.write("\n")


def main():
    pairs = [p for p in os.environ.get("PAIRS", ",".join(C.PAIRS)).split(",") if p]
    laporan = jalankan(pairs)
    tulis(laporan)
    for h in laporan["hasil"]:
        print(h["pair"], h["label"], h.get("metode"), h.get("alasan", [""])[0])


if __name__ == "__main__":
    main()
