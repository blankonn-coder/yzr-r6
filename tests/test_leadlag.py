"""Lead-lag: backtest korelasi, kandidat, store, gerbang ENTRY, dan prioritas di pemantauan."""
import json
from datetime import datetime, timezone

import config as C
import leadlag as LL
import pantauan as PT
from backtest.leadlag_sintetis import DITANAM, buat_sintetis


def _row(pair, harga, atr=0.001, label="NO TRADE", bar="2026-11-24T10:00:00Z"):
    return {"pair": pair, "harga": harga, "label": label, "bar_terakhir": bar,
            "cadangan": {"h1": {"tf": "H1", "atr": atr, "support": None, "resistance": None},
                         "m15": None, "m15_tersedia": False}}


def _set_last(cs, n, fn):
    """Ubah n close terakhir: fn(close_sebelumnya) -> close baru, berurutan."""
    for i in range(len(cs) - n, len(cs)):
        cs[i][1] = fn(cs[i - 1][1])


def _ambil_dari(candles):
    return lambda key: [{"t": t, "c": c} for t, c in candles[key]]


# ---------- backtest korelasi ----------

def test_hubungan_tertanam_terdeteksi_dengan_lag_benar():
    candles = buat_sintetis()
    end = max(cs[-1][0] for cs in candles.values())
    pasangan, _, _, _ = LL.hitung_backtest(candles, end)
    cari = {(p["leader"], p["follower"]): p for p in pasangan}
    for lead, fol, lag, _ in DITANAM:
        p = cari.get((C.disp(lead), C.disp(fol)))
        assert p is not None, f"{lead}->{fol} tidak terdeteksi"
        assert p["lag_menit"] == lag * 5
        assert p["korelasi"] >= C.LEADLAG_MIN_CORR and p["n"] >= C.LEADLAG_MIN_SAMPLE


def test_lag_nol_yang_lebih_kuat_ditolak():
    # Follower identik dengan leader tanpa jeda: korelasi lag 0 terkuat, jadi bukan 'tertinggal'
    candles = buat_sintetis(ditanam=[])
    candles["NZD_JPY"] = [[t, c] for t, c in candles["GBP_JPY"]]
    end = max(cs[-1][0] for cs in candles.values())
    pasangan, _, _, _ = LL.hitung_backtest(candles, end)
    assert not any(p["leader"] == "GBP/JPY" and p["follower"] == "NZD/JPY" for p in pasangan)


def test_jendela_hanya_6_jam_terakhir():
    assert len(LL._jendela(1_000_000)) == C.LEADLAG_WINDOW_BARS == 72
    assert C.LEADLAG_WINDOW_BARS * C.TF_LEADLAG_SEC == 6 * 3600


# ---------- kandidat (pemicu) ----------

def _kasus_pemicu(follower_bergerak):
    candles = buat_sintetis()
    _set_last(candles["GBP_JPY"], 3, lambda p: p * 1.005)      # leader naik tajam 3 bar terakhir
    if follower_bergerak:
        _set_last(candles["NZD_JPY"], 3, lambda p: p * 1.005)  # follower sudah ikut naik
    else:
        _set_last(candles["NZD_JPY"], 3, lambda p: p)          # follower belum bergerak
    end = max(cs[-1][0] for cs in candles.values())
    _, lag_terbaik, ret, sigma = LL.hitung_backtest(candles, end)
    rows = [_row("NZD/JPY", candles["NZD_JPY"][-1][1], atr=0.05)]
    return LL.kandidat(rows, candles, ret, sigma, lag_terbaik, end), candles


def test_kandidat_leader_bergerak_follower_belum_menghasilkan_saran():
    kand, candles = _kasus_pemicu(follower_bergerak=False)
    assert len(kand) == 1
    s = kand[0]
    assert s["pair"] == "NZD/JPY" and s["metode"] == "LEAD-LAG" and s["leader"] == "GBP/JPY"
    assert s["arah"] == "BUY"  # leader naik, korelasi positif
    assert s["lag_menit"] == 15
    assert s["sl"] < s["entry"] < s["tp"]
    assert s["entry"] == round(candles["NZD_JPY"][-1][1], 5)
    t_akhir = candles["NZD_JPY"][-1][0]
    assert s["mulai"] == C.fmt(datetime.fromtimestamp(t_akhir + C.TF_LEADLAG_SEC, timezone.utc))


def test_pasangan_belum_dipicu_tetap_punya_arah_dan_sl_tp():
    candles = buat_sintetis()
    end = max(cs[-1][0] for cs in candles.values())
    _, lag_terbaik, ret, sigma = LL.hitung_backtest(candles, end)
    rows = [_row("NZD/JPY", candles["NZD_JPY"][-1][1], atr=0.05)]
    kand = LL.kandidat(rows, candles, ret, sigma, lag_terbaik, end)
    assert kand and all(k["arah"] in ("BUY", "SELL") and k["sl"] != k["tp"] for k in kand)
    assert all(isinstance(k["dipicu"], bool) for k in kand)


def test_kandidat_follower_sudah_bergerak_dilewati():
    kand, _ = _kasus_pemicu(follower_bergerak=True)
    assert kand == []


def test_kandidat_lewati_follower_entry_dan_tanpa_atr():
    kand, candles = _kasus_pemicu(follower_bergerak=False)
    end = max(cs[-1][0] for cs in candles.values())
    _, lag_terbaik, ret, sigma = LL.hitung_backtest(candles, end)
    entry = [_row("NZD/JPY", 90.0, label="ENTRY LONG")]
    tanpa_atr = [_row("NZD/JPY", 90.0, atr=0.0)]
    assert LL.kandidat(entry, candles, ret, sigma, lag_terbaik, end) == []
    assert LL.kandidat(tanpa_atr, candles, ret, sigma, lag_terbaik, end) == []
    assert LL.kandidat([], candles, ret, sigma, lag_terbaik, end) == []  # follower harus ada di scanner


def test_follower_di_luar_scanner_tidak_dipakai():
    kand, candles = _kasus_pemicu(follower_bergerak=False)
    end = max(cs[-1][0] for cs in candles.values())
    _, lag_terbaik, ret, sigma = LL.hitung_backtest(candles, end)
    assert LL.kandidat([], candles, ret, sigma, lag_terbaik, end) == []


# ---------- store ----------

def test_gabung_menimpa_duplikat_dan_membatasi_retensi(monkeypatch):
    monkeypatch.setattr(C, "LEADLAG_RETENSI_BARS", 5)
    lama = [[100, 1.0], [200, 2.0], [300, 3.0]]
    baru = [{"t": 300, "c": 3.3}, {"t": 400, "c": 4.0}, {"t": 500, "c": 5.0}, {"t": 600, "c": 6.0},
            {"t": 700, "c": 7.0}]
    hasil = LL._gabung(lama, baru)
    assert [t for t, _ in hasil] == [300, 400, 500, 600, 700]
    assert dict(hasil)[300] == 3.3


def test_jalankan_saat_entry_hanya_perbarui_data(monkeypatch, tmp_path):
    monkeypatch.setattr(C, "LEADLAG_PATH", str(tmp_path / "ll.json"))
    candles = buat_sintetis()
    hasil = LL.jalankan(datetime(2026, 11, 24, 12, tzinfo=timezone.utc), [], _ambil_dari(candles),
                        analisa=False)
    assert hasil["saran"] == [] and hasil["backtest"] is None
    assert hasil["status"].startswith("dilewati")
    data = json.loads((tmp_path / "ll.json").read_text(encoding="utf-8"))
    assert len(data["candles"]) == len(C.LEADLAG_PAIRS)


def test_jalankan_gagal_ambil_tidak_melempar(monkeypatch, tmp_path):
    monkeypatch.setattr(C, "LEADLAG_PATH", str(tmp_path / "ll.json"))

    def gagal(key):
        raise RuntimeError("jaringan")

    hasil = LL.jalankan(datetime(2026, 11, 24, 12, tzinfo=timezone.utc), [], gagal, analisa=True)
    assert hasil["saran"] == [] and hasil["status"] == "tidak ada data M5"
    assert len(hasil["gagal"]) == len(C.LEADLAG_UNIVERSE)


# ---------- pemantauan ----------

def test_pemantauan_mulai_dari_candle_m5_bukan_close_h1(monkeypatch, tmp_path):
    monkeypatch.setattr(C, "PANTAU_AKTIF_PATH", str(tmp_path / "p.json"))
    mulai = C.to_epoch("2026-11-24T11:00:00Z")
    saran = {"pair": "NZD/JPY", "arah": "BUY", "entry": 90.0, "sl": 89.0, "tp": 91.5,
             "sl_pip": 100.0, "bar_terakhir": "2026-11-24T10:00:00Z", "mulai": "2026-11-24T11:00:00Z",
             "sumber": PT.SUMBER_LEADLAG, "titik": {}, "dibuat": "2026-11-24T11:00:00Z"}
    # Candle sebelum mulai punya TP; harus diabaikan. Candle sesudahnya belum menyentuh apa pun.
    m15 = [{"t": mulai - 900, "o": 90, "h": 92, "l": 90, "c": 91.6},
           {"t": mulai, "o": 90, "h": 90.2, "l": 89.8, "c": 90.1}]
    hasil = PT.perbarui(datetime(2026, 11, 24, 11, 20, tzinfo=timezone.utc), [saran], lambda k: m15)
    assert hasil["tampil"][0]["hasil"] == "BERJALAN"
    assert hasil["tampil"][0]["titik"] == {"15": 10.0}  # (90,1 - 90,0) / pip 0,01 JPY


def test_jalankan_pemantauan_prioritas_lead_lag_lalu_cadangan(monkeypatch, tmp_path):
    monkeypatch.setattr(C, "PANTAU_AKTIF_PATH", str(tmp_path / "p.json"))
    monkeypatch.setattr(C, "PANTAU_ARSIP_PATH", str(tmp_path / "arsip.jsonl"))
    rows = []
    for i, pair in enumerate(["EUR/USD", "GBP/USD", "AUD/USD", "USD/CAD"]):
        r = _row(pair, 1.0 + i * 0.01, atr=0.001, bar="2026-11-24T10:00:00Z")
        r["cadangan"]["h1"]["support"] = {"harga": 1.0 + i * 0.01 - 0.0002, "jarak_atr": 0.2,
                                          "sentuhan": 5, "umur_bar": 0}
        rows.append(r)
    ll = {"pair": "USD/CAD", "arah": "BUY", "metode": "LEAD-LAG", "entry": 1.04, "sl": 1.0395,
          "tp": 1.0408, "sl_pip": 5.0, "bar_terakhir": "2026-11-24T10:00:00Z",
          "mulai": "2026-11-24T11:00:00Z", "leader": "GBP/JPY", "lag_menit": 15, "korelasi": 0.7,
          "n": 60, "level": None, "level_harga": None, "jarak_atr": None, "sentuhan": None}
    now = datetime(2026, 11, 24, 11, 5, tzinfo=timezone.utc)
    hasil = PT.jalankan(now, rows, lambda k: None, prioritas=[ll])
    assert hasil["saran"][0]["pair"] == "USD/CAD" and hasil["saran"][0]["metode"] == "LEAD-LAG"
    # Lead-lag menggantikan saran cadangan: hanya pair lead-lag yang diberi saran
    assert [s["pair"] for s in hasil["saran"]] == ["USD/CAD"]
    aktif = json.loads((tmp_path / "p.json").read_text(encoding="utf-8"))["aktif"]
    assert {s["pair"]: s["sumber"] for s in aktif} == {"USD/CAD": PT.SUMBER_LEADLAG}


def test_tanpa_prioritas_tidak_ada_saran_baru(monkeypatch, tmp_path):
    monkeypatch.setattr(C, "PANTAU_AKTIF_PATH", str(tmp_path / "p.json"))
    monkeypatch.setattr(C, "PANTAU_ARSIP_PATH", str(tmp_path / "arsip.jsonl"))
    rows = [_row(f"P{i}/X", 1.0 + i * 0.001, atr=0.001) for i in range(4)]
    now = datetime(2026, 11, 24, 11, 5, tzinfo=timezone.utc)
    assert PT.jalankan(now, rows, lambda k: None)["saran"] == []


def _ll_item(pair):
    return {"pair": pair, "arah": "BUY", "metode": "LEAD-LAG", "entry": 1.0, "sl": 0.99, "tp": 1.015,
            "sl_pip": 100.0, "bar_terakhir": "2026-11-24T10:00:00Z", "mulai": "2026-11-24T11:00:00Z",
            "leader": "GBP/JPY", "lag_menit": 15, "korelasi": 0.7, "n": 60}


def test_saat_ada_entry_analisa_cadangan_mati(monkeypatch, tmp_path):
    monkeypatch.setattr(C, "PANTAU_AKTIF_PATH", str(tmp_path / "p.json"))
    monkeypatch.setattr(C, "PANTAU_ARSIP_PATH", str(tmp_path / "arsip.jsonl"))
    rows = [_row("USD/CAD", 1.0, atr=0.001)]
    now = datetime(2026, 11, 24, 11, 5, tzinfo=timezone.utc)
    hasil = PT.jalankan(now, rows, lambda k: None, prioritas=[_ll_item("USD/CAD")], cadangan_aktif=False)
    assert hasil["saran"] == [] and hasil["cadangan_aktif"] is False


def test_hubungan_tidak_stabil_ditolak():
    # Hubungan hanya ada di paruh terakhir jendela: harus ditolak oleh pemeriksaan dua paruh
    candles = buat_sintetis(ditanam=[])
    lead = [c for _, c in candles["GBP_JPY"]]
    fol = [c for _, c in candles["NZD_JPY"]]
    n = len(lead)
    rng_fol = [fol[i] for i in range(n)]
    for i in range(n):
        if i >= 3 and i >= n - 72 + 36:  # hanya paruh terakhir (lebih baru) yang mengikuti leader
            rng_fol[i] = fol[i - 1] * (lead[i - 3] / lead[i - 4])
    for i, c in enumerate(rng_fol):
        candles["NZD_JPY"][i][1] = c
    end = max(cs[-1][0] for cs in candles.values())
    _, lag_terbaik, _, _ = LL.hitung_backtest(candles, end)
    assert ("GBP_JPY", "NZD_JPY") not in lag_terbaik


def test_store_bergulir_tetap_6_jam():
    assert C.LEADLAG_RETENSI_BARS == C.LEADLAG_WINDOW_BARS == 72
    lama = [[i * 300, 1.0] for i in range(72)]
    baru = [{"t": (72 + i) * 300, "c": 1.0} for i in range(3)]
    hasil = LL._gabung(lama, baru)
    assert len(hasil) == 72 and hasil[0][0] == 3 * 300 and hasil[-1][0] == 74 * 300


def test_discord_hanya_pair_lag_dan_saran():
    import discord_notify as DN
    now = datetime(2026, 11, 24, 11, 5, tzinfo=timezone.utc)
    rows = [_row("EUR/JPY", 147.4, atr=0.05)]
    rows[0]["cadangan"]["h1"]["support"] = {"harga": 147.3, "jarak_atr": 0.2, "sentuhan": 3, "umur_bar": 0}
    lag = [{"leader": "GBP/JPY", "follower": "EUR/JPY", "lag_menit": 15, "korelasi": 0.85, "n": 68}]
    saran = [_ll_item("EUR/JPY")]
    emb = DN.build_embed(now, "OK", rows, False, {"saran": saran, "tampil": [], "selesai": [], "lag": lag})
    nama = [f["name"] for f in emb["fields"]]
    assert not any("Level cadangan" in n or "Saran cadangan" in n for n in nama)
    teks = " ".join(f["value"] for f in emb["fields"])
    assert "**EUR/JPY** · BUY" in teks and "SL 0.99" in teks and "TP 1.015" in teks
