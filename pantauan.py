"""Pemantauan entry dan saran analisa cadangan.

Setiap entry (ENTRY LONG/SHORT) dan saran cadangan (BUKAN sinyal) dicatat saat run dibuat.
Acuannya adalah bar H1 yang sudah tutup, jadi waktu mulai = close bar itu.
Titik cek tiap 15 menit memakai close candle M15 yang sudah tutup sejak waktu mulai.
Setelah 60 menit (4 titik), atau saat SL/TP kena, dibuat evaluasi 1 jam.
Jika SL dan TP kena di candle yang sama, dihitung SL (konservatif).

Pemantauan tidak mengubah label, ranking, atau keputusan apa pun.
"""
import analisa_cadangan as CD
import config as C

CANDLE_SEC = 900
TITIK = C.PANTAU_TOTAL_MENIT // C.PANTAU_TITIK_MENIT  # 4 titik: 15, 30, 45, 60 menit
SUMBER_ENTRY = "ENTRY"
SUMBER_CADANGAN = "ANALISA CADANGAN (bukan sinyal)"
SUMBER_LEADLAG = "LEAD-LAG (analisa cadangan, bukan sinyal)"


def _pair_key(pair):
    return pair.replace("/", "_")


def _pnl(s, harga):
    """Selisih harga dalam pip, positif = untung."""
    pip = C.pip_size(_pair_key(s["pair"]))
    selisih = harga - s["entry"] if s["arah"] == "BUY" else s["entry"] - harga
    return round(selisih / pip, 1)


def _rekam(now, sumber, r, arah, entry, sl, tp, metode=None):
    pip = C.pip_size(_pair_key(r["pair"]))
    return {"sumber": sumber, "pair": r["pair"], "arah": arah, "metode": metode,
            "entry": round(entry, 5), "sl": round(sl, 5), "tp": round(tp, 5),
            "sl_pip": round(abs(entry - sl) / pip, 1), "bar_terakhir": r["bar_terakhir"],
            "dibuat": C.fmt(now)}


def buat_entry(now, rows):
    """Entry baru dari run ini. Arah LONG/SHORT diubah ke BUY/SELL."""
    out = []
    for r in rows:
        if not r["label"].startswith("ENTRY") or r.get("entry") is None:
            continue
        arah = "BUY" if r["arah"] == "LONG" else "SELL"
        out.append(_rekam(now, SUMBER_ENTRY, r, arah, r["entry"], r["sl"], r["tp"], metode=r["metode"]))
    return out


def perbarui(now, aktif, ambil_m15):
    """Cek catatan aktif terhadap candle M15 yang sudah tutup sejak waktu mulai.
    ambil_m15(pair_key) -> list candle M15 atau None.

    Return dict:
      aktif   : catatan yang masih dipantau (disimpan ke state)
      tampil  : baris pemantauan run ini (titik 15/30/45/60 menit + hasil sementara)
      selesai : evaluasi 1 jam yang baru ditutup (diarsipkan)
    """
    cache, hasil = {}, {"aktif": [], "tampil": [], "selesai": []}
    for s in aktif:
        key = _pair_key(s["pair"])
        if key not in cache:
            cache[key] = ambil_m15(key)
        m15 = cache[key] or []
        # Saran lead-lag punya titik awal sendiri (close M5 terakhir); saran lain mulai di close H1
        awal = C.to_epoch(s["mulai"]) if s.get("mulai") else C.to_epoch(s["bar_terakhir"]) + C.TF_MAIN_SEC
        bars = [b for b in m15 if b["t"] >= awal][:TITIK]

        buy = s["arah"] == "BUY"
        titik = {}
        kena, harga_akhir, menit_kena = None, None, None
        fav_max, adv_max = None, None  # gerak terbaik/terburuk dalam harga, sejak entry
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
            if sl_kena:
                kena, harga_akhir, menit_kena = "SL kena", s["sl"], menit
                break
            if tp_kena:
                kena, harga_akhir, menit_kena = "TP kena", s["tp"], menit
                break
            titik[str(menit)] = _pnl(s, b["c"])
            harga_akhir = b["c"]

        pip_size = C.pip_size(_pair_key(s["pair"]))
        umur = round((now.timestamp() - C.to_epoch(s["dibuat"])) / 60)
        selesai = kena is not None or len(bars) >= TITIK or umur >= C.PANTAU_TIMEOUT_MENIT
        if selesai and kena is None:
            kena = "Selesai 60 menit" if len(bars) >= TITIK else "Data M15 tidak lengkap"
        if kena is None:
            kena = "BERJALAN" if bars else "Menunggu data M15"

        rec = {**s, "titik": titik, "hasil": kena, "menit_kena": menit_kena,
               "harga_skrg": harga_akhir,
               "pip": _pnl(s, harga_akhir) if harga_akhir is not None else None,
               "mfe": round(fav_max / pip_size, 1) if fav_max is not None else None,
               "mae": round(adv_max / pip_size, 1) if adv_max is not None else None,
               "umur_menit": umur, "status": "SELESAI" if selesai else "AKTIF"}
        hasil["tampil"].append(rec)
        if selesai:
            hasil["selesai"].append({**rec, "ditutup": C.fmt(now)})
        else:
            hasil["aktif"].append(s)
    return hasil


def jalankan(now, rows, ambil_m15, prioritas=None, cadangan_aktif=True):
    """Satu run: pantau catatan aktif, lalu catat entry dan saran cadangan baru dari run ini.
    Catatan baru belum punya candle sesudahnya, jadi baru dinilai di run berikutnya.

    prioritas: saran lead-lag (sudah berurutan). Diisi dulu, sisanya diisi saran cadangan biasa
    Saran analisa cadangan kini berasal dari lead-lag (menggantikan saran level H1 lama).
    cadangan_aktif=False saat ada ENTRY di run ini: tidak ada saran baru. Pemantauan saran
    yang sudah berjalan tetap dilanjutkan agar evaluasinya selesai.
    """
    state = C.load_json(C.PANTAU_AKTIF_PATH, {"aktif": []})
    hasil = perbarui(now, state.get("aktif", []), ambil_m15)

    entry = buat_entry(now, rows)
    # Pair yang masih dipantau sebagai saran tidak diberi saran baru
    aktif_cadangan = {s["pair"] for s in hasil["aktif"] if s["sumber"] == SUMBER_CADANGAN}
    aktif_leadlag = {s["pair"] for s in hasil["aktif"] if s["sumber"] == SUMBER_LEADLAG}
    ll = []
    if cadangan_aktif:
        ll = [s for s in (prioritas or []) if s["pair"] not in aktif_cadangan | aktif_leadlag][:C.LEADLAG_SARAN_N]
    std = []  # saran level H1 tidak dipakai lagi: lead-lag menggantikannya
    baru_leadlag = [{**s, "sumber": SUMBER_LEADLAG, "titik": {}, "dibuat": C.fmt(now)} for s in ll]
    baru_cadangan = [{**s, "sumber": SUMBER_CADANGAN, "titik": {}, "dibuat": C.fmt(now)} for s in std]
    C.save_json(C.PANTAU_AKTIF_PATH, {"aktif": hasil["aktif"] + entry + baru_leadlag + baru_cadangan})
    CD._append_jsonl(C.PANTAU_ARSIP_PATH, hasil["selesai"])
    return {"saran": ll + std, "entry": entry, "tampil": hasil["tampil"], "selesai": hasil["selesai"],
            "cadangan_aktif": cadangan_aktif}
