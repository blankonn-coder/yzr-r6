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


def should_send(mode, rows, heartbeat=False):
    """signal: kirim jika ada ENTRY/WATCHLIST/DATA INVALID, atau ada analisa cadangan (NO TRADE/WATCHLIST),
    atau heartbeat harian (run jam 00 UTC)."""
    if mode == "off":
        return False
    if mode == "always":
        return True
    if heartbeat:
        return True
    return any(r["label"] in ("WATCHLIST", "DATA INVALID") or r["label"].startswith("ENTRY")
               or r.get("cadangan") for r in rows)


def _cut(text, limit=FIELD_MAX):
    return text if len(text) <= limit else text[:limit - 12].rstrip() + "\n… (dipotong)"


def _cad_lvl(tag, x):
    if not x:
        return f"{tag} —"
    return f"{tag} {x['harga']} ({x['jarak_atr']} ATR)"


def _cad_baris(r):
    cad = r["cadangan"]
    bagian = []
    for key in ("h1", "m15"):
        t = cad.get(key)
        if not t:
            bagian.append(f"{key.upper()} tidak tersedia")
            continue
        bagian.append(f"{key.upper()}: {_cad_lvl('Res', t.get('resistance'))} · {_cad_lvl('Sup', t.get('support'))}")
    return f"**{r['pair']}**\n" + "\n".join(bagian)


def _potong_baris(blok, limit=FIELD_MAX):
    """Gabungkan blok per pair menjadi teks per field, tiap field maksimal limit karakter."""
    hasil, cur = [], ""
    for b in blok:
        calon = b if not cur else cur + "\n\n" + b
        if len(calon) <= limit:
            cur = calon
        else:
            if cur:
                hasil.append(cur)
            cur = b
    if cur:
        hasil.append(cur)
    return hasil or ["—"]


def build_embed(now, status, rows, ranking_ok):
    entry = [r for r in rows if r["label"].startswith("ENTRY")]
    watch = [r for r in rows if r["label"] == "WATCHLIST"]
    invalid = [r for r in rows if r["label"] == "DATA INVALID"]
    warna = 0x2ECC71 if entry else (0xF1C40F if watch else 0x95A5A6)
    desc = f"Status: **{status}** · Ranking: **{'ada' if ranking_ok else 'kosong (semua NO TRADE)'}**"
    if not ranking_ok:
        desc += "\nBelum ada metode yang lolos backtest, jadi tidak ada sinyal. Ini normal."

    def kekuatan(r):
        sel = r.get("sel")
        if not sel:
            return ""
        return f" · {'★' * sel['bintang']} skor {sel['skor']}, n {sel['n']}"

    def baris_entry(r):
        return (f"**{r['pair']}** · {r['metode']} {r['arah']}{kekuatan(r)}\n"
                f"Entry {r['entry']} · SL {r['sl']} · TP {r['tp']}")

    def baris_watch(r):
        if not r["metode"]:
            return f"**{r['pair']}** · {r['status']}"
        return f"**{r['pair']}** · {r['metode']} {r['arah']}{kekuatan(r)} · {r['status']}"

    fields = [
        {"name": f"🟢 ENTRY ({len(entry)})", "value": _cut("\n\n".join(map(baris_entry, entry)) or "—"), "inline": False},
        {"name": f"🟡 WATCHLIST ({len(watch)})", "value": _cut("\n".join(map(baris_watch, watch)) or "—"), "inline": False},
    ]
    cad = [r for r in rows if r.get("cadangan") and not r["label"].startswith("ENTRY")]
    if cad:
        # Dipecah per pair agar tidak terpotong oleh batas 1024 karakter per field
        potongan = _potong_baris(list(map(_cad_baris, cad)))
        for i, teks in enumerate(potongan, 1):
            judul = "🔎 Analisa cadangan (bukan sinyal, tanpa entry)"
            if len(potongan) > 1:
                judul += f" {i}/{len(potongan)}"
            fields.append({"name": judul, "value": teks, "inline": False})
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
    if not should_send(_mode(), rows, heartbeat=(now.hour == 0)):
        return f"Discord: mode {_mode()}, tidak ada yang dikirim"
    try:
        ok = _post(url, build_embed(now, status, rows, ranking_ok))
        return "Discord: terkirim" if ok else "Discord: gagal kirim (cek URL webhook)"
    except Exception as e:  # URL tidak boleh ikut tercetak
        return f"Discord: error {type(e).__name__}"
