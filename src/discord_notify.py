"""Kirim ringkasan run ke Discord lewat webhook (embed).

Konfigurasi di GitHub:
  Secret   DISCORD_WEBHOOK_URL   URL webhook (wajib agar notifikasi aktif)
  Variable DISCORD_NOTIFY_MODE   signal (default) | always | off
    signal : kirim jika ada sinyal BUY/SELL baru ATAU ada pair yang masih dipantau
    always : kirim setiap run (termasuk tanpa sinyal)
    off    : tidak pernah kirim
"""
import os
import time

import requests

from . import config as C
from .monitor import aktif, umur, teks_gerak

WEBHOOK_ENV = "DISCORD_WEBHOOK_URL"
MODE_ENV = "DISCORD_NOTIFY_MODE"
FIELD_MAX = 1024
DESC_MAX = 300


def _mode():
    return os.environ.get(MODE_ENV, "").strip().lower() or "signal"


def should_send(mode, n_buy, n_sell, n_pantau=0):
    if mode == "off":
        return False
    if mode == "always":
        return True
    return (n_buy + n_sell + n_pantau) > 0


def _cut(text, limit):
    if len(text) <= limit:
        return text
    akhiran = "\n… (dipotong)"
    return text[:limit - len(akhiran)].rstrip() + akhiran


def _sinyal_lines(rows, kep):
    return [f"**{r['pair']}** · skor {r['skor_akhir']}\n" + "\n".join(f"• {a}" for a in r["alasan"])
            for r in rows if r["keputusan"] == kep]


def build_payload(now, status, calib, rows, gagal, mon, info):
    buy = [r for r in rows if r["keputusan"] == "BUY"]
    sell = [r for r in rows if r["keputusan"] == "SELL"]

    if buy and sell:
        warna = 0xF1C40F
    elif buy:
        warna = 0x2ECC71
    elif sell:
        warna = 0xE74C3C
    else:
        warna = 0x95A5A6

    deskripsi = f"Status: **{status}** · Kalibrasi: **{calib}** · Pair dianalisa: **{len(rows)}**"
    if gagal:
        deskripsi += "\nGagal ambil data: " + ", ".join(gagal)

    fields = [
        {"name": f"🟢 BUY ({len(buy)})",
         "value": _cut("\n\n".join(_sinyal_lines(rows, "BUY")) or "—", FIELD_MAX), "inline": False},
        {"name": f"🔴 SELL ({len(sell)})",
         "value": _cut("\n\n".join(_sinyal_lines(rows, "SELL")) or "—", FIELD_MAX), "inline": False},
    ]

    pantau = aktif(mon, now)
    if pantau:
        baris = []
        for m in pantau.values():
            pip, pct = C.gerak(m["pair"], m["harga_awal"], m["harga_sekarang"], m.get("keputusan", ""))
            baris.append(f"**{m['pair']}** ({m.get('keputusan', '-')}) · {teks_gerak(pip, pct)} "
                         f"· {int(umur(m, now))} menit")
        fields.append({"name": f"📈 Pemantauan {C.MONITOR_MINUTES} menit ({len(pantau)})",
                       "value": _cut("\n".join(baris), FIELD_MAX), "inline": False})

    return {
        "title": f"📊 Screening Forex · {now:%H:%M} UTC",
        "description": _cut(deskripsi, DESC_MAX),
        "color": warna,
        "fields": fields,
        "footer": {"text": f"Database: {info['total']} entri (+{info['tambah']}) · "
                           f"laporan lengkap di reports/latest_report.md"},
        "timestamp": now.isoformat(),
    }


def _post(url, embed):
    for _ in range(3):
        r = requests.post(url, json={"embeds": [embed]}, timeout=15)
        if r.status_code == 429:
            try:
                wait = float(r.json().get("retry_after", 2))
            except ValueError:
                wait = 2.0
            time.sleep(min(wait, 10))
            continue
        return r.status_code in (200, 204)
    return False


def notify(now, status, calib, rows, gagal, mon, info):
    """Return pesan status untuk log. Tidak pernah melempar error agar run tidak gagal."""
    url = os.environ.get(WEBHOOK_ENV, "").strip()
    if not url:
        return "Discord: webhook belum diatur, dilewati"
    n_buy = sum(1 for r in rows if r["keputusan"] == "BUY")
    n_sell = sum(1 for r in rows if r["keputusan"] == "SELL")
    n_pantau = len(aktif(mon, now))
    if not should_send(_mode(), n_buy, n_sell, n_pantau):
        return f"Discord: mode {_mode()}, tidak ada yang dikirim"
    try:
        embed = build_payload(now, status, calib, rows, gagal, mon, info)
        ok = _post(url, embed)
        return "Discord: terkirim" if ok else "Discord: gagal kirim (cek URL webhook)"
    except Exception as e:  # jangan sampai URL ikut tercetak
        return f"Discord: error {type(e).__name__}"
