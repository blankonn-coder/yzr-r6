"""Kirim ringkasan scanner ke Discord lewat webhook (embed). Tidak pernah melempar error.

Konfigurasi GitHub:
  Secret   DISCORD_WEBHOOK_URL   URL webhook
  Variable DISCORD_NOTIFY_MODE   signal (default) | always | off
    signal : kirim jika ada ENTRY, WATCHLIST, atau DATA INVALID
    always : kirim setiap run
    off    : tidak pernah kirim
"""
import os
import time

import requests

import config as C

WEBHOOK_ENV = "DISCORD_WEBHOOK_URL"
MODE_ENV = "DISCORD_NOTIFY_MODE"
FIELD_MAX = 1024


def _mode():
    return os.environ.get(MODE_ENV, "").strip().lower() or "signal"


def should_send(mode, rows):
    if mode == "off":
        return False
    if mode == "always":
        return True
    return any(r["label"] in ("WATCHLIST", "DATA INVALID") or r["label"].startswith("ENTRY") for r in rows)


def _cut(text, limit=FIELD_MAX):
    return text if len(text) <= limit else text[:limit - 12].rstrip() + "\n… (dipotong)"


def build_embed(now, status, rows, ranking_ok):
    entry = [r for r in rows if r["label"].startswith("ENTRY")]
    watch = [r for r in rows if r["label"] == "WATCHLIST"]
    invalid = [r for r in rows if r["label"] == "DATA INVALID"]
    warna = 0x2ECC71 if entry else (0xF1C40F if watch else 0x95A5A6)
    desc = f"Status: **{status}** · Ranking: **{'ada' if ranking_ok else 'kosong'}** · Pair: **{len(rows)}**"

    def baris(r):
        extra = f" · {r['metode']} {r['arah']}" if r["metode"] else ""
        return f"**{r['pair']}** · {r['regime']} · {r['bias']}{extra}\n" + "\n".join(f"• {c}" for c in r["catatan"][:2])

    fields = [
        {"name": f"🟢 ENTRY ({len(entry)})", "value": _cut("\n\n".join(map(baris, entry)) or "—"), "inline": False},
        {"name": f"🟡 WATCHLIST ({len(watch)})", "value": _cut("\n\n".join(map(baris, watch)) or "—"), "inline": False},
    ]
    if invalid:
        fields.append({"name": f"⚠️ DATA INVALID ({len(invalid)})",
                       "value": _cut(", ".join(r["pair"] for r in invalid)), "inline": False})
    return {"title": f"📊 Adaptive Forex Scanner · {now:%H:%M} UTC", "description": desc,
            "color": warna, "fields": fields,
            "footer": {"text": "Laporan lengkap: reports/scanner_latest.md"},
            "timestamp": now.isoformat()}


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


def notify(now, status, rows, ranking_ok):
    url = os.environ.get(WEBHOOK_ENV, "").strip()
    if not url:
        return "Discord: webhook belum diatur, dilewati"
    if not should_send(_mode(), rows):
        return f"Discord: mode {_mode()}, tidak ada yang dikirim"
    try:
        ok = _post(url, build_embed(now, status, rows, ranking_ok))
        return "Discord: terkirim" if ok else "Discord: gagal kirim (cek URL webhook)"
    except Exception as e:  # URL tidak boleh ikut tercetak
        return f"Discord: error {type(e).__name__}"
