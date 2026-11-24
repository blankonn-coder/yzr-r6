"""Saran analisa cadangan dan pemantauan entry/cadangan (BUKAN sinyal untuk cadangan)."""
from datetime import datetime, timezone

import analisa_cadangan as CD
import config as C
import pantauan as PT


def _lvl(harga, jarak, sentuhan=10):
    return {"harga": harga, "jarak_atr": jarak, "sentuhan": sentuhan, "umur_bar": 0}


def _row(pair, harga, support=None, resistance=None, atr=0.001, label="NO TRADE"):
    return {"pair": pair, "harga": harga, "label": label, "bar_terakhir": "2026-11-24T10:00:00Z",
            "cadangan": {"h1": {"tf": "H1", "atr": atr, "support": support, "resistance": resistance},
                         "m15": None, "m15_tersedia": False}}


def _iso(dt):
    return dt.strftime("%Y-%m-%dT%H:%M:%SZ")


def _now(iso):
    return datetime.fromisoformat(iso.replace("Z", "+00:00")).replace(tzinfo=timezone.utc)


AWAL = C.to_epoch("2026-11-24T11:00:00Z")  # close H1 10:00 = mulai pemantauan


def _m15(awal, specs):
    """specs: (high, low, close) berurutan mulai dari awal, tiap candle 15 menit."""
    return [{"t": awal + 900 * i, "o": c, "h": h, "l": l, "c": c} for i, (h, l, c) in enumerate(specs)]


def _saran_buy():
    s = CD.pilih_saran([_row("USD/CAD", 1.43396, support=_lvl(1.43386, 0.09))])[0]
    return {**s, "sumber": PT.SUMBER_CADANGAN, "titik": {}, "dibuat": "2026-11-24T11:05:00Z"}


def _entry_sell(sl=1.5699, tp=1.56778):
    r = {"pair": "EUR/CAD", "label": "ENTRY SHORT", "arah": "SHORT", "metode": "FISHER", "entry": 1.56905,
         "sl": sl, "tp": tp, "bar_terakhir": "2026-11-24T10:00:00Z"}
    return PT.buat_entry(_now("2026-11-24T11:05:00Z"), [r])[0]


# ---------- saran cadangan ----------

def test_pilih_saran_nearest_level_and_direction():
    rows = [
        _row("USD/CAD", 1.43396, support=_lvl(1.43386, 0.09, 26)),
        _row("EUR/CHF", 0.91922, resistance=_lvl(0.91953, 0.34, 10)),
        _row("EUR/JPY", 174.27, support=_lvl(174.0085, 1.05)),              # di luar 1 ATR
        _row("AUD/USD", 0.66248, support=_lvl(0.66205, 0.38, 20), resistance=_lvl(0.66346, 0.87, 20)),
        _row("EUR/GBP", 0.83718, support=_lvl(0.83698, 0.40, 22)),
        _row("GBP/USD", 1.3, resistance=_lvl(1.3078, 0.53, 7), label="ENTRY LONG"),  # dilewati
    ]
    saran = CD.pilih_saran(rows)
    # CADANGAN_SARAN_N = 3: tiga level terdekat; EUR/GBP (jarak 0,40 ATR) berada di luar tiga teratas
    assert [s["pair"] for s in saran] == ["USD/CAD", "EUR/CHF", "AUD/USD"]
    assert {s["pair"]: s["arah"] for s in saran} == {"USD/CAD": "BUY", "EUR/CHF": "SELL", "AUD/USD": "BUY"}
    assert next(s for s in saran if s["pair"] == "AUD/USD")["level"] == "support"


def test_pilih_saran_max_three_and_exclusion():
    rows = [_row(f"P{i}/X", 1.0 + i * 0.001, support=_lvl(1.0 + i * 0.001 - 0.0001, 0.1 + i * 0.01))
            for i in range(8)]
    saran = CD.pilih_saran(rows)
    assert len(saran) == C.CADANGAN_SARAN_N == 3 and len({s["pair"] for s in saran}) == 3
    saran2 = CD.pilih_saran(rows, dikecualikan={"P0/X"})
    assert "P0/X" not in {s["pair"] for s in saran2}


def test_sl_tp_geometry():
    buy, sell = CD.pilih_saran([_row("USD/CAD", 1.43396, support=_lvl(1.43386, 0.09)),
                                _row("EUR/CHF", 0.91922, resistance=_lvl(0.91953, 0.34))])
    assert buy["sl"] < buy["entry"] < buy["tp"]
    assert sell["tp"] < sell["entry"] < sell["sl"]
    assert abs(buy["sl"] - (1.43386 - 0.0005)) < 1e-9
    assert abs(buy["tp"] - (1.43396 + 1.5 * (1.43396 - buy["sl"]))) < 1e-9
    assert abs(sell["sl"] - (0.91953 + 0.0005)) < 1e-9


def test_pilih_saran_skips_invalid_and_entry():
    rows = [_row("EUR/USD", 1.0, support=_lvl(0.9999, 0.1), label="DATA INVALID"),
            _row("GBP/USD", 1.0, support=_lvl(0.9999, 0.1), label="ENTRY LONG")]
    assert CD.pilih_saran(rows) == []


# ---------- pemantauan ----------

def test_entry_dicatat_dengan_arah_buy_sell():
    e = _entry_sell()
    assert e["sumber"] == PT.SUMBER_ENTRY and e["arah"] == "SELL" and e["metode"] == "FISHER"
    assert e["sl_pip"] == round(abs(1.56905 - 1.5699) / 0.0001, 1)


def test_tp_kena_di_titik_ke_2_dan_mfe_mae():
    s = _saran_buy()  # entry 1.43396, sl 1.43336, tp 1.43486
    m15 = _m15(AWAL, [(1.4345, 1.4339, 1.4344), (1.4349, 1.4343, 1.4348)])
    out = PT.perbarui(_now("2026-11-24T11:35:00Z"), [s], lambda k: m15)
    assert out["aktif"] == []
    e = out["selesai"][0]
    assert e["hasil"] == "TP kena" and e["menit_kena"] == 30 and e["pip"] == 9.0
    assert e["mfe"] == 9.4  # high candle yang kena TP ikut dihitung
    assert e["mae"] == round((1.4339 - 1.43396) / 0.0001, 1)


def test_sl_kena_konservatif_jika_satu_candle():
    s = _saran_buy()
    m15 = _m15(AWAL, [(1.4360, 1.4330, 1.4340)])  # low kena SL, high kena TP: hitung SL
    out = PT.perbarui(_now("2026-11-24T11:20:00Z"), [s], lambda k: m15)
    e = out["tampil"][0]
    assert e["hasil"] == "SL kena" and e["pip"] == -6.0 and e["menit_kena"] == 15


def test_titik_15_30_45_60_terisi_dan_evaluasi_setelah_60_menit():
    s = _saran_buy()
    m15 = _m15(AWAL, [(1.4340, 1.4338, 1.4339), (1.4341, 1.4337, 1.4338),
                      (1.4339, 1.4336, 1.4337), (1.4338, 1.4335, 1.4336)])
    out = PT.perbarui(_now("2026-11-24T12:05:00Z"), [s], lambda k: m15)
    assert out["aktif"] == [] and out["selesai"][0]["hasil"] == "Selesai 60 menit"
    t = out["tampil"][0]
    assert set(t["titik"]) == {"15", "30", "45", "60"}
    assert t["titik"]["15"] == round((1.4339 - 1.43396) / 0.0001, 1)


def test_berjalan_dan_titik_parsial_abaikan_candle_sebelum_awal():
    s = _saran_buy()
    m15 = _m15(AWAL - 900, [(1.4340, 1.4300, 1.4310)]) + _m15(AWAL, [(1.4340, 1.4338, 1.4339)])
    out = PT.perbarui(_now("2026-11-24T11:35:00Z"), [s], lambda k: m15)
    t = out["tampil"][0]
    assert t["status"] == "AKTIF" and t["hasil"] == "BERJALAN"
    assert set(t["titik"]) == {"15"} and len(out["aktif"]) == 1 and out["selesai"] == []


def test_tanpa_m15_menunggu_lalu_data_tidak_lengkap_setelah_90_menit():
    s = _saran_buy()
    out = PT.perbarui(_now("2026-11-24T11:20:00Z"), [s], lambda k: None)
    assert out["tampil"][0]["hasil"] == "Menunggu data M15" and len(out["aktif"]) == 1
    out2 = PT.perbarui(_now("2026-11-24T12:40:00Z"), [s], lambda k: None)  # umur 95 menit
    assert out2["selesai"][0]["hasil"] == "Data M15 tidak lengkap"


def test_jalankan_tidak_menduplikasi_pair_cadangan_yang_masih_dipantau(tmp_path, monkeypatch):
    monkeypatch.setattr(C, "PANTAU_AKTIF_PATH", str(tmp_path / "aktif.json"))
    monkeypatch.setattr(C, "PANTAU_ARSIP_PATH", str(tmp_path / "arsip.jsonl"))
    rows = [_row("USD/CAD", 1.43396, support=_lvl(1.43386, 0.09)),
            _row("EUR/CHF", 0.91922, resistance=_lvl(0.91953, 0.34))]
    # Saran analisa cadangan kini berasal dari lead-lag (prioritas)
    ll = [{"pair": p, "arah": "BUY", "metode": "LEAD-LAG", "entry": 1.0, "sl": 0.99, "tp": 1.015,
           "sl_pip": 100.0, "bar_terakhir": "2026-11-24T10:00:00Z", "mulai": "2026-11-24T11:00:00Z"}
          for p in ("USD/CAD", "EUR/CHF")]
    run1 = PT.jalankan(_now("2026-11-24T11:05:00Z"), rows, lambda k: None, prioritas=ll)
    assert [s["pair"] for s in run1["saran"]] == ["USD/CAD", "EUR/CHF"]
    run2 = PT.jalankan(_now("2026-11-24T11:50:00Z"), rows, lambda k: None, prioritas=ll)  # masih aktif, belum ada candle
    assert run2["saran"] == []
    st = C.load_json(C.PANTAU_AKTIF_PATH, {})
    assert len(st["aktif"]) == 2
