"""Database mentah JSON: hanya BUY & SELL, retensi, tanpa analisa."""
from datetime import timedelta

import config as C


def _kosong(now):
    return {"metadata": {"created_at": C.fmt(now), "last_updated": C.fmt(now),
                         "retensi_hari": C.RETENSI_HARI, "total_entri": 0},
            "signals": []}


def load(now):
    return C.load_json(C.DB_PATH, None) or _kosong(now)


def prune(db, now):
    hari = max(C.MIN_RETENSI_HARI, int(db["metadata"].get("retensi_hari", C.RETENSI_HARI)))
    cutoff = now - timedelta(days=hari)
    sebelum = len(db["signals"])
    db["signals"] = [s for s in db["signals"] if C.parse(s["waktu"]) >= cutoff]
    return sebelum - len(db["signals"])


def add(db, records):
    ada = {s["id"] for s in db["signals"]}
    n = 0
    for r in records:
        if r["id"] not in ada:  # idempotensi
            db["signals"].append(r)
            ada.add(r["id"])
            n += 1
    return n


def mark_expired(db, ids):
    for s in db["signals"]:
        if s["id"] in ids:
            s["status_pantau"] = "EXPIRED"


def expire_stale(db, now):
    """Sinyal AKTIF yang sudah melewati batas pemantauan ditutup otomatis.
    Ini juga membereskan data lama yang tertinggal berstatus AKTIF."""
    n = 0
    for s in db["signals"]:
        umur = (now - C.parse(s["waktu"])).total_seconds() / 60
        if s.get("status_pantau") == "AKTIF" and umur >= C.MONITOR_MINUTES:
            s["status_pantau"] = "EXPIRED"
            n += 1
    return n


def save(db, now):
    if not db["metadata"].get("created_at"):
        db["metadata"]["created_at"] = C.fmt(now)
    db["metadata"]["last_updated"] = C.fmt(now)
    db["metadata"]["total_entri"] = len(db["signals"])
    C.save_json(C.DB_PATH, db)
