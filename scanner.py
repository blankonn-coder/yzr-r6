"""Scanner live per pair (§8): ambil H1 & H4 tertutup, validasi, analisa, lalu label."""
from datetime import datetime, timezone

import biquote_client as bq
import config as C
from analysis import build, evaluate
from data_quality import validate


def fetch_news():
    """Return (waktu_news_epoch | None, pesan_error | None). Tidak pernah melempar error."""
    try:
        return bq.fetch_news_times(), None
    except Exception as e:
        return None, type(e).__name__


def news_clean(news, now):
    """True = tidak ada news high-impact dalam ±30 menit; False = ada; None = kalender gagal."""
    if news is None:
        return None
    t, w = now.timestamp(), C.NEWS_WINDOW_MIN * 60
    return not any(abs(t - x) <= w for x in news)


def _gap_count(warnings):
    for w in warnings:
        if w.startswith("gap"):
            return int(w.split(":")[1])
    return 0


def _invalid(pair, alasan):
    return {"pair": C.disp(pair), "regime": "-", "bias": "-", "label": "DATA INVALID",
            "status": "Data tidak valid", "metode": None, "arah": None, "harga": None,
            "entry": None, "sl": None, "tp": None, "catatan": [alasan],
            "gap": {"H1": 0, "H4": 0}, "bar": {}, "bar_terakhir": None}


def scan_pair(pair, ranking, news_bersih, now):
    try:
        h1 = bq.fetch_candles(pair, C.TF_MAIN, C.H1_COUNT)
        h4 = bq.fetch_candles(pair, C.TF_BIAS, C.H4_COUNT)
    except Exception as e:
        return _invalid(pair, f"gagal ambil data ({type(e).__name__}: {e})")
    ok1, e1, w1 = validate(h1, 3600)
    ok4, e4, w4 = validate(h4, 14400)
    if not (ok1 and ok4):
        return _invalid(pair, "validasi data gagal: " + "; ".join(e1 + e4))

    row = {"pair": C.disp(pair), **evaluate(build(h1, h4), pair, ranking, news_bersih)}
    # Celah waktu (gap) biasanya akhir pekan/libur: dihitung di laporan, tidak diulang per pair
    row["gap"] = {"H1": _gap_count(w1), "H4": _gap_count(w4)}
    row["catatan"] += [f"data H1 {x}" for x in w1 if not x.startswith("gap")]
    row["catatan"] += [f"data H4 {x}" for x in w4 if not x.startswith("gap")]
    row["bar"] = {"h1": len(h1), "h4": len(h4)}
    row["bar_terakhir"] = C.fmt(datetime.fromtimestamp(h1[-1]["t"], timezone.utc))
    return row
