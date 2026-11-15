"""Kalibrasi harga biquote -> Finex (offset per pair)."""
import json
import os

from . import config as C


def fetch_finex_reference():
    """Harga referensi Finex (mid) per pair, dibaca dari env FINEX_REFERENCE_JSON,
    contoh: {"EUR_USD": 1.16340, "GBP_USD": 1.33100}.
    Catatan: library MetaTrader5 hanya jalan di Windows. Di GitHub Actions, isi
    secret ini secara berkala dari terminal Finex Anda. Jika kosong, bot memakai
    offset terakhir dan laporan ditandai TANPA KALIBRASI."""
    raw = os.environ.get("FINEX_REFERENCE_JSON", "").strip()
    if not raw:
        return None
    try:
        return {k: float(v) for k, v in json.loads(raw).items()}
    except (ValueError, TypeError, AttributeError):
        return None


def get_offsets(oanda_mid):
    """oanda_mid: {pair: harga mid terakhir dari feed}. Return (offsets, status)."""
    state = C.load_json(C.CALIB_PATH, {"offsets": {}})
    offsets = {k: float(v) for k, v in state.get("offsets", {}).items()}
    ref = fetch_finex_reference()
    if not ref:
        return offsets, "TANPA KALIBRASI"
    for pair, finex_price in ref.items():
        pair = pair.strip().upper().replace("/", "_")
        if pair in oanda_mid:
            offsets[pair] = finex_price - oanda_mid[pair]
    return offsets, "TERKALIBRASI"


def save_offsets(offsets, now):
    C.save_json(C.CALIB_PATH, {"offsets": offsets, "updated": C.fmt(now)})


def shift(candles, off):
    if not off:
        return candles
    return [{**c, "o": c["o"] + off, "h": c["h"] + off,
             "l": c["l"] + off, "c": c["c"] + off} for c in candles]
