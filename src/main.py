"""Entry point: python -m src.main [--pairs EUR_USD,GBP_USD]"""
import argparse
import os
import sys

from . import config as C
from . import signal_store as store
from .analysis import evaluate
from .calibration import get_offsets, save_offsets, shift
from .discord_notify import notify
from .monitor import update as monitor_update, saring_cooldown, catat_cooldown
from .biquote_client import fetch_candles
from .report import build_report


def market_open(now):
    wd = now.weekday()  # Senin=0 ... Minggu=6
    if wd == 5:
        return False
    if wd == 6:
        return now.hour >= 22
    if wd == 4:
        return now.hour < 22
    return True


def slot_delay_menit(now):
    slot = now.replace(minute=(now.minute // 15) * 15, second=0, microsecond=0)
    return (now - slot).total_seconds() / 60


def tulis_laporan(teks):
    os.makedirs(os.path.dirname(C.REPORT_PATH), exist_ok=True)
    with open(C.REPORT_PATH, "w", encoding="utf-8") as f:
        f.write(teks)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pairs", default="", help="uji coba, dipisah koma; kosong = semua pair")
    args = ap.parse_args()
    now = C.utc_now()

    if not market_open(now):
        tulis_laporan(build_report(now, "PASAR TUTUP", "-", [], [], {}, None))
        print("Pasar forex tutup.")
        return 0

    pairs = [p.strip().upper().replace("/", "_") for p in args.pairs.split(",") if p.strip()] or C.PAIRS
    status = "TERLAMBAT" if slot_delay_menit(now) > C.LATE_MINUTES else "TEPAT WAKTU"

    # 1. Ambil data OANDA
    raw, gagal = {}, []
    for p in pairs:
        try:
            raw[p] = {tf: fetch_candles(p, g) for tf, g in C.TF_GRAN.items()}
        except Exception as e:
            gagal.append(f"{C.disp(p)} ({e})")

    # 2. Kalibrasi ke Finex
    mids = {p: d["5m"][-1]["c"] for p, d in raw.items()}
    offsets, calib = get_offsets(mids)
    save_offsets(offsets, now)

    # 3. Analisa & keputusan tunggal per pair
    rows, prices = [], {}
    for p, data in raw.items():
        off = offsets.get(p, 0.0)
        cal = {tf: shift(cs, off) for tf, cs in data.items()}
        price = round(cal["5m"][-1]["c"], 5)
        res = evaluate(cal, price, p)
        rows.append({"pair": C.disp(p), "keputusan": res["keputusan"], "skor_akhir": res["skor"],
                     "alasan": res["alasan"], "harga": price, "level": res["level"],
                     "rsi": res["rsi"], "tren": res["tren"]})
        prices[C.disp(p)] = price

    # 4. Cooldown: sinyal searah di pair yang masih cooldown tidak masuk hasil screening
    mon = C.load_json(C.MONITOR_PATH, {})
    cooldown = C.load_json(C.COOLDOWN_PATH, {})
    cooldown, ditahan = saring_cooldown(cooldown, mon, rows, now)

    # 5. Pemantauan
    sinyal = [r for r in rows if r["keputusan"] in ("BUY", "SELL")]
    records = []
    for r in sinyal:
        r["id"] = f"{now:%Y%m%dT%H%M%SZ}_{r['pair'].replace('/', '')}"
        records.append({"id": r["id"], "waktu": C.fmt(now), "tanggal": now.strftime("%Y-%m-%d"),
                        "jam_utc": now.strftime("%H:%M"), "pair": r["pair"],
                        "keputusan": r["keputusan"], "skor_akhir": r["skor_akhir"],
                        "harga_saat_itu": r["harga"], "level_terdekat": r["level"],
                        "rsi": r["rsi"], "tren": r["tren"], "alasan": r["alasan"],
                        "status_pantau": "AKTIF"})
    mon, expired = monitor_update(
        mon, [{"pair": r["pair"], "id": r["id"], "harga": r["harga"], "keputusan": r["keputusan"]} for r in sinyal],
        prices, now)
    C.save_json(C.MONITOR_PATH, mon)
    C.save_json(C.COOLDOWN_PATH, catat_cooldown(cooldown, sinyal, now))
    # Hanya sinyal yang benar-benar masuk pemantauan yang berstatus AKTIF
    tracked = {m["signal_id"] for m in mon.values()}
    for r in records:
        r["status_pantau"] = "AKTIF" if r["id"] in tracked else "TIDAK DIPANTAU"

    # 6. Database mentah (prune dulu, lalu append)
    db = store.load(now)
    pruned = store.prune(db, now)
    store.mark_expired(db, set(expired))
    store.expire_stale(db, now)
    added = store.add(db, records)
    store.save(db, now)

    # 7. Laporan
    info = {"total": len(db["signals"]), "tambah": added, "hapus": pruned}
    tulis_laporan(build_report(now, status, calib, rows, gagal, mon, info))
    print(notify(now, status, calib, rows, gagal, mon, info))
    print(f"Selesai: {len(rows)} pair dianalisa, {len(sinyal)} sinyal, {ditahan} ditahan cooldown, {len(gagal)} gagal.")
    return 0 if rows else 1


if __name__ == "__main__":
    sys.exit(main())
