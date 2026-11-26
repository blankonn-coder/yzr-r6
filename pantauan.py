"""Pemantauan entry. Logika tidak berubah dari versi sebelumnya.

Titik cek tiap 15 menit memakai close candle M15 yang sudah tutup sejak waktu mulai (close bar sinyal).
Setelah 60 menit, atau saat SL/TP kena, entry diarsipkan. Jika SL dan TP kena di candle yang sama, dihitung SL.
Batas posisi di engine.py memakai catatan aktif di sini (maks 60 menit), bukan posisi nyata di broker.
"""
import config as C

TITIK = C.PANTAU_TOTAL_MENIT // C.PANTAU_TITIK_MENIT   # 4 titik: 15, 30, 45, 60 menit


def _pnl(s, harga):
    """Selisih dalam pip, positif = untung."""
    pip = C.pip_size(s["pair"].replace("/", "_"))
    selisih = harga - s["entry"] if s["arah"] == "BUY" else s["entry"] - harga
    return round(selisih / pip, 1)


def buat_entry(now, rows):
    """Entry baru dari hasil analisa (label ENTRY). Arah = decision (BUY/SELL)."""
    out = []
    for r in rows:
        if not str(r.get("label", "")).startswith("ENTRY") or r.get("entry") is None:
            continue
        pip = C.pip_size(r["pair"].replace("/", "_"))
        out.append({"sumber": "ENTRY", "pair": r["pair"], "arah": r["decision"], "metode": r.get("metode"),
                    "entry": r["entry"], "sl": r["sl"], "tp": r["tp"],
                    "sl_pip": round(abs(r["entry"] - r["sl"]) / pip, 1),
                    "bar_terakhir": r["bar_terakhir"], "dibuat": C.fmt(now)})
    return out


def perbarui(now, aktif, ambil_m15):
    """Cek catatan aktif terhadap candle M15. ambil_m15(pair_key) -> list candle atau None."""
    cache, hasil = {}, {"aktif": [], "tampil": [], "selesai": []}
    for s in aktif:
        key = s["pair"].replace("/", "_")
        if key not in cache:
            cache[key] = ambil_m15(key) or []
        awal = C.to_epoch(s["bar_terakhir"]) + C.TF_SEC    # close bar sinyal
        bars = [b for b in cache[key] if b["t"] >= awal][:TITIK]
        buy = s["arah"] == "BUY"
        titik, kena, harga_akhir, menit_kena = {}, None, None, None
        fav_max = adv_max = None
        for i, b in enumerate(bars):
            menit = C.PANTAU_TITIK_MENIT * (i + 1)
            if buy:
                sl_kena, tp_kena = b["l"] <= s["sl"], b["h"] >= s["tp"]
                fav, adv = b["h"] - s["entry"], b["l"] - s["entry"]
            else:
                sl_kena, tp_kena = b["h"] >= s["sl"], b["l"] <= s["tp"]
                fav, adv = s["entry"] - b["l"], s["entry"] - b["h"]
            fav_max = fav if fav_max is None else max(fav_max, fav)
            adv_max = adv if adv_max is None else min(adv_max, adv)
            if sl_kena or tp_kena:
                kena, harga_akhir, menit_kena = ("SL kena", s["sl"], menit) if sl_kena else ("TP kena", s["tp"], menit)
                break
            titik[str(menit)] = _pnl(s, b["c"])
            harga_akhir = b["c"]

        pip = C.pip_size(key)
        umur = round((now.timestamp() - C.to_epoch(s["dibuat"])) / 60)
        selesai = kena is not None or len(bars) >= TITIK or umur >= C.PANTAU_TIMEOUT_MENIT
        if kena is None:
            kena = ("Selesai 60 menit" if len(bars) >= TITIK else "Data M15 tidak lengkap") if selesai \
                else ("BERJALAN" if bars else "Menunggu data M15")
        rec = {**s, "titik": titik, "hasil": kena, "menit_kena": menit_kena, "harga_skrg": harga_akhir,
               "pip": _pnl(s, harga_akhir) if harga_akhir is not None else None,
               "mfe": round(fav_max / pip, 1) if fav_max is not None else None,
               "mae": round(adv_max / pip, 1) if adv_max is not None else None,
               "umur_menit": umur, "status": "SELESAI" if selesai else "AKTIF"}
        hasil["tampil"].append(rec)
        if selesai:
            hasil["selesai"].append({**rec, "ditutup": C.fmt(now)})
        else:
            hasil["aktif"].append(s)
    return hasil


def aktif_saat_ini():
    return C.load_json(C.PANTAU_AKTIF, {"aktif": []})["aktif"]


def perbarui_state(now, ambil_m15):
    """Awal run: perbarui catatan aktif, arsipkan yang selesai, simpan state."""
    hasil = perbarui(now, aktif_saat_ini(), ambil_m15)
    C.save_json(C.PANTAU_AKTIF, {"aktif": hasil["aktif"]})
    C.append_jsonl(C.PANTAU_ARSIP, hasil["selesai"])
    return hasil


def tambah(now, rows):
    """Akhir run: catat entry baru. Pair dan bar yang sama tidak dicatat dua kali."""
    aktif = aktif_saat_ini()
    kunci = {(s["pair"], s["bar_terakhir"]) for s in aktif}
    baru = [b for b in buat_entry(now, rows) if (b["pair"], b["bar_terakhir"]) not in kunci]
    C.save_json(C.PANTAU_AKTIF, {"aktif": aktif + baru})
    return baru
