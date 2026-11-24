"""Uji Tahap 1 (dijalankan manual, bukan oleh workflow screening).

Memeriksa tiga hal sebelum modul lain dibangun:
  1. Dukascopy: unduh dan validasi BID/ASK M1 satu bulan untuk satu pair.
  2. Biquote: candle H1 terbaru (batas 1000 bar) dari client yang sudah ada.
  3. Biquote calendar: apakah event high-impact tersedia dengan actual/forecast/previous.

Jalankan:  python -m src.stage1_check
Hasil:     reports/stage1_check.json (dan ringkasan di layar)
"""
import json
import os
import sys

import requests

from . import config as C
from .biquote_client import fetch_candles
from .data.dukascopy import unduh, muat
from .data.validate import check_candles, check_bid_ask

PAIR = "EUR_USD"
DUKA_START = "2026-10-01"
DUKA_END = "2026-10-31"
LAPORAN = "reports/stage1_check.json"


def cek_dukascopy():
    unduh(PAIR, DUKA_START)
    bid = muat(PAIR, "BID", DUKA_START, DUKA_END)
    ask = muat(PAIR, "ASK", DUKA_START, DUKA_END)
    return {
        "bid": check_candles(bid),
        "ask": check_candles(ask),
        "bid_ask": check_bid_ask(bid, ask),
    }


def cek_biquote_h1():
    try:
        bars = fetch_candles(PAIR, "1h", count=1000)
    except Exception as e:  # jaringan atau batas API
        return {"lolos": False, "error": str(e)}
    return {
        "lolos": True,
        "jumlah_bar": len(bars),
        "awal": bars[0]["time"] if bars else None,
        "akhir": bars[-1]["time"] if bars else None,
    }


def cek_kalender():
    try:
        r = requests.get(
            "https://biquote.io/api/calendar",
            params={"importance": "high", "countries": "US,EU"},
            timeout=20,
        )
        r.raise_for_status()
        events = r.json()
    except Exception as e:
        return {"lolos": False, "error": str(e)}
    if not isinstance(events, list):
        return {"lolos": False, "error": "format respons bukan daftar"}
    kunci = {"actual", "forecast", "previous"}
    ada_nilai = sum(1 for e in events if any(e.get(k) is not None for k in kunci))
    return {
        "lolos": len(events) > 0 and ada_nilai > 0,
        "jumlah_event": len(events),
        "event_dengan_nilai": ada_nilai,
        "contoh": events[0] if events else None,
    }


def main():
    hasil = {}
    for nama, fungsi in [("dukascopy", cek_dukascopy), ("biquote_h1", cek_biquote_h1), ("kalender", cek_kalender)]:
        print(f"Menjalankan: {nama} ...")
        try:
            hasil[nama] = fungsi()
        except Exception as e:
            hasil[nama] = {"lolos": False, "error": str(e)}

    semua_lolos = (
        hasil["dukascopy"].get("bid", {}).get("lolos", False)
        and hasil["dukascopy"].get("ask", {}).get("lolos", False)
        and hasil["dukascopy"].get("bid_ask", {}).get("lolos", False)
        and hasil["biquote_h1"].get("lolos", False)
        and hasil["kalender"].get("lolos", False)
    )
    hasil["ringkasan_lolos"] = semua_lolos

    os.makedirs(os.path.dirname(LAPORAN), exist_ok=True)
    with open(LAPORAN, "w", encoding="utf-8") as f:
        json.dump(hasil, f, ensure_ascii=False, indent=2, default=str)

    print(json.dumps(hasil, ensure_ascii=False, indent=2, default=str))
    print("\nTAHAP 1:", "LOLOS" if semua_lolos else "BELUM LOLOS (lihat detail di atas)")
    sys.exit(0 if semua_lolos else 1)


if __name__ == "__main__":
    main()
