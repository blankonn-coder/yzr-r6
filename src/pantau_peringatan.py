"""Pemantauan hasil peringatan 1 jam. Dipanggil dari src/peringatan.py setiap run.

- Setiap pair yang masuk peringatan dicatat dengan harga, SL, dan TP-nya, beserta bar sumbernya.
- Tiap run dihitung sebagai satu cek. Hit SL/TP hanya dinilai dari bar yang lebih baru dari bar sumber,
  karena harga entry adalah close bar sumber.
- Berhenti saat TP kena, SL kena, atau sudah MAKS_JAM jam, atau MAKS_CEK cek, mana yang lebih dulu.
- Pair+arah yang sama tidak dicatat ulang selama masih dipantau, dan tidak dicatat ulang untuk bar sumber yang sama.
- Jika SL dan TP kena di bar yang sama, dihitung SL (konservatif).
"""
import json
import os
from datetime import datetime, timedelta, timezone

import pandas as pd
import requests

STATE = "state/peringatan_pantau.json"
ARSIP = "database/peringatan_pemantauan.jsonl"
MAKS_JAM = 6
MAKS_CEK = 24
TP_PIP = 10
TERCATAT_SIMPAN_JAM = 48
NOTE_COOLDOWN_JAM = 6


def _pip(pair):
    return 0.01 if "JPY" in pair else 0.0001


def _desimal(pair):
    return 3 if "JPY" in pair else 5


def _muat(path=STATE):
    if not os.path.exists(path):
        return {"aktif": [], "tercatat": []}
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def _simpan(state, path=STATE):
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(state, f, ensure_ascii=False, indent=2)


def _arsip(records, path=ARSIP):
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "a", encoding="utf-8") as f:   # selalu dibuat, agar git add tidak gagal
        for r in records:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")


def buka(state, sent, now):
    """Catat pair yang baru menyentuh level. Dilewati jika pair+arah masih dipantau,
    atau bar sumbernya sudah pernah dicatat (mencegah alert ulang dari bar yang sama)."""
    aktif_keys = {(w["pair"], w["arah"]) for w in state["aktif"]}
    tercatat = {(t["pair"], t["arah"], t["bar"]) for t in state["tercatat"]}
    for r in sent:
        key = (r["pair"], r["arah"])
        bar = str(r["waktu"])
        if key in aktif_keys or (r["pair"], r["arah"], bar) in tercatat:
            continue
        pair, buy = r["pair"], r["arah"] == "BUY"
        pip, dec = _pip(pair), _desimal(pair)
        entry = float(r["harga"])
        sl = entry - pip * r["sl_pip"] if buy else entry + pip * r["sl_pip"]
        tp = entry + pip * TP_PIP if buy else entry - pip * TP_PIP
        state["aktif"].append({
            "pair": pair, "arah": r["arah"], "tipe": r["tipe"], "lvl": r["lvl"],
            "entry": round(entry, dec), "sl": round(sl, dec), "tp": round(tp, dec),
            "sl_pip": r["sl_pip"], "mulai": now.isoformat(), "cek": 0,
            "bar_sumber": bar, "bar_terakhir": bar, "harga_terakhir": round(entry, dec),
            "mfe": 0.0, "mae": 0.0,
        })
        aktif_keys.add(key)
        tercatat.add((pair, r["arah"], bar))
    state["tercatat"] = [{"pair": p, "arah": a, "bar": b} for p, a, b in tercatat
                         if pd.Timestamp(b) >= pd.Timestamp(now) - pd.Timedelta(hours=TERCATAT_SIMPAN_JAM)]
    return state


def _nilai_bar(w, bar):
    """Return (hasil, harga_keluar) jika SL atau TP kena di bar ini, selain itu (None, None)."""
    buy = w["arah"] == "BUY"
    sl_kena = bar.low <= w["sl"] if buy else bar.high >= w["sl"]
    tp_kena = bar.high >= w["tp"] if buy else bar.low <= w["tp"]
    if sl_kena:
        return "SL kena", w["sl"]
    if tp_kena:
        return "TP kena", w["tp"]
    return None, None


def cek(state, data, now):
    """Cek semua pemantauan aktif satu kali. Return (masih_aktif, selesai)."""
    masih, selesai = [], []
    for w in state["aktif"]:
        w["cek"] += 1
        hasil, harga = None, None
        h = data.get(w["pair"])
        if h is not None and len(h):
            pip = _pip(w["pair"])
            buy = w["arah"] == "BUY"
            baru = h[h.index > pd.Timestamp(w["bar_terakhir"])]     # hanya bar setelah bar sumber / terakhir dinilai
            for ts, bar in baru.iterrows():
                fav = (bar.high - w["entry"]) / pip if buy else (w["entry"] - bar.low) / pip
                adv = (w["entry"] - bar.low) / pip if buy else (bar.high - w["entry"]) / pip
                w["mfe"] = round(max(w["mfe"], fav), 1)
                w["mae"] = round(max(w["mae"], adv), 1)
                w["bar_terakhir"] = str(ts)
                w["harga_terakhir"] = round(float(bar.close), _desimal(w["pair"]))
                hasil, harga = _nilai_bar(w, bar)
                if hasil:
                    break

        habis_waktu = now - datetime.fromisoformat(w["mulai"]) >= timedelta(hours=MAKS_JAM)
        habis_cek = w["cek"] >= MAKS_CEK
        if hasil is None and (habis_waktu or habis_cek):
            hasil = "selesai 6 jam" if habis_waktu else "selesai 24 cek"
            harga = w["harga_terakhir"]

        if hasil is None:
            masih.append(w)
            continue

        pip = _pip(w["pair"])
        selisih = harga - w["entry"] if w["arah"] == "BUY" else w["entry"] - harga
        selesai.append({
            **w, "hasil": hasil, "harga_keluar": round(harga, _desimal(w["pair"])),
            "pip": round(selisih / pip, 1), "selesai": now.isoformat(),
        })
    state["aktif"] = masih
    return state, selesai


def _baris(r):
    return (f"**{r['pair']}** {r['arah']} · {r['hasil']}\n"
            f"> entry {r['entry']} · keluar {r['harga_keluar']} · pip {r['pip']:+}\n"
            f"> MFE {r['mfe']} / MAE {r['mae']} pip · {r['cek']} cek")


def kirim(url, selesai, aktif):
    if not url:
        return "Pemantauan: tidak dikirim (webhook kosong)"
    if not selesai:
        return f"Pemantauan: tidak ada yang selesai, aktif {aktif}"
    isi = "\n".join(["**Hasil pemantauan peringatan**", "-# Berhenti saat TP, SL, 6 jam, atau 24 cek", ""]
                    + [_baris(r) + "\n" for r in selesai]).strip()[:1900]
    try:
        r = requests.post(url, json={"content": isi}, timeout=15)
        return f"Pemantauan Discord: HTTP {r.status_code}, aktif {aktif}"
    except requests.RequestException as e:
        return f"Pemantauan Discord: gagal kirim ({type(e).__name__})"


def kirim_pergerakan(url, aktif):
    """Kirim pergerakan semua pair yang sedang dipantau. Dipanggil setiap run, agar pemantauan terlihat di Discord."""
    if not url:
        return "Pergerakan: tidak dikirim (webhook kosong)"
    if not aktif:
        return "Pergerakan: tidak ada pair yang dipantau"
    fields = []
    for w in aktif:
        pip = _pip(w["pair"])
        buy = w["arah"] == "BUY"
        selisih = w["harga_terakhir"] - w["entry"] if buy else w["entry"] - w["harga_terakhir"]
        fields.append({
            "name": f"{w['pair']} · {w['arah']} · entry {w['entry']}",
            "value": (f"harga {w['harga_terakhir']} · {round(selisih / pip, 1):+} pip\n"
                      f"MFE {w['mfe']} / MAE {w['mae']} pip · {w['cek']} cek"),
            "inline": False,
        })
    embed = {
        "title": "Pergerakan pair yang di-note",
        "description": f"{len(aktif)} pair dipantau",
        "color": 5793266,
        "fields": fields[:25],
    }
    try:
        r = requests.post(url, json={"embeds": [embed]}, timeout=15)
        return f"Pergerakan Discord: HTTP {r.status_code}"
    except requests.RequestException as e:
        return f"Pergerakan Discord: gagal kirim ({type(e).__name__})"


def saring_note(hasil, now=None, path=STATE):
    """Pair yang sudah muncul di note tidak dimunculkan lagi selama NOTE_COOLDOWN_JAM jam.
    Mengembalikan daftar hasil baru untuk note Discord; pemantauan tetap memakai hasil asli."""
    now = now or datetime.now(timezone.utc)
    state = _muat(path)
    terakhir = {p: t for p, t in state.get("note_terakhir", {}).items()
                if now - datetime.fromisoformat(t) < timedelta(hours=NOTE_COOLDOWN_JAM)}
    keluar = []
    for r in hasil:
        if r.get("status") == "SENTUH":
            if r["pair"] in terakhir:
                r = {**r, "status": "sudah dinote"}
            else:
                terakhir[r["pair"]] = now.isoformat()
        keluar.append(r)
    state["note_terakhir"] = terakhir
    _simpan(state, path)
    return keluar


def jalankan(hasil, data, url, now=None):
    """Satu run: cek pemantauan lama, catat pair baru, simpan state, arsipkan yang selesai, kirim hasil dan pergerakan."""
    now = now or datetime.now(timezone.utc)
    state = _muat()
    state, selesai = cek(state, data, now)
    sent = [r for r in hasil if r.get("status") == "SENTUH"]
    state = buka(state, sent, now)
    _simpan(state)
    _arsip(selesai)
    msg = kirim(url, selesai, len(state["aktif"]))
    return msg + "\n" + kirim_pergerakan(url, state["aktif"])
