"""Entry point scanner live: python main.py [--pairs EUR_USD,GBP_USD]"""
import argparse
import os
import sys

import analisa_cadangan as CD
import config as C
import pantauan
import ranking
import report
import scanner
from discord_notify import notify


def market_open(now):
    wd = now.weekday()  # Senin=0 ... Minggu=6
    if wd == 5:
        return False
    if wd == 6:
        return now.hour >= 22
    if wd == 4:
        return now.hour < 22
    return True


def _tulis(path, text):
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pairs", default="", help="uji coba, dipisah koma; kosong = semua pair")
    args = ap.parse_args()
    now = C.utc_now()
    pairs = [p.strip().upper().replace("/", "_") for p in args.pairs.split(",") if p.strip()] or C.PAIRS

    ranking_map = ranking.load_active()
    ranking_ok = bool(ranking_map)
    is_open = market_open(now)
    rows, news_bersih, news_err = [], None, None
    if is_open:
        news, news_err = scanner.fetch_news()
        news_bersih = scanner.news_clean(news, now)
        rows = [scanner.scan_pair(p, ranking_map, news_bersih, now) for p in pairs]
    if is_open:
        n_invalid = sum(1 for r in rows if r["label"] == "DATA INVALID")
        status = f"OK, {len(rows) - n_invalid} pair dianalisa, {n_invalid} data tidak valid"
    else:
        status = "PASAR TUTUP, tidak ada analisa"

    # Saran dan pemantauan cadangan hanya dihitung saat pasar buka. Saat tutup, state tidak diubah.
    cad = None
    if is_open:
        cad = pantauan.jalankan(now, rows, scanner.fetch_m15)

    _tulis(C.SCANNER_MD_PATH, report.build_scanner_md(now, status, rows, ranking_ok, news_bersih,
                                                       news_err, is_open, ranking.load_meta(), cad))
    C.save_json(C.SCANNER_JSON_PATH, report.build_scanner_json(now, status, rows, cad))
    print(notify(now, status, rows, ranking_ok, cad))

    if C.CADANGAN_ENABLED:
        print(f"Snapshot analisa cadangan baru: {CD.simpan_snapshot(now, rows)}")
    counts = {}
    for r in rows:
        counts[r["label"]] = counts.get(r["label"], 0) + 1
    print(f"Selesai: {len(rows)} pair, {counts}")
    if not is_open:
        return 0
    return 0 if any(r["label"] != "DATA INVALID" for r in rows) else 1


if __name__ == "__main__":
    sys.exit(main())
