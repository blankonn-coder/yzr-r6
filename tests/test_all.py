"""Tes skema final: indikator, korelasi, trigger, filter, target, pemantauan, backtest, dan siklus main.

Data uji sintetis berkorelasi; tidak memanggil jaringan. Jalankan: python -m pytest tests/
"""
import math
import random
from datetime import datetime, timezone

import backtest as B
import config as C
import engine as E
import main as M
import pantauan as PT

# ---------------- data uji ----------------
START = 1767225600  # 2026-01-01T00:00Z (kelipatan 4 jam)


def synthetic(n, seed=1):
    rnd = random.Random(seed)
    beta = {"EUR_USD": 1.0, "EUR_JPY": 0.7, "EUR_GBP": 0.5, "GBP_USD": -0.6, "USD_JPY": -0.4}
    base = {"EUR_USD": 1.1, "EUR_JPY": 174.0, "EUR_GBP": 0.87, "GBP_USD": 1.3, "USD_JPY": 150.0}
    raw = {p: [] for p in C.PAIRS}
    price = dict(base)
    for j in range(n):
        f = rnd.gauss(0, 1)
        for p in C.PAIRS:
            v = 0.0006
            o = price[p]
            c = o * math.exp(beta[p] * f * v * 0.8 + rnd.gauss(0, v * 0.6))
            hi, lo = max(o, c) * (1 + abs(rnd.gauss(0, v * 0.3))), min(o, c) * (1 - abs(rnd.gauss(0, v * 0.3)))
            raw[p].append({"t": START + 900 * j, "o": o, "h": hi, "l": lo, "c": c})
            price[p] = c
    return raw

# ---------------- engine ----------------
def _prep(n=800, seed=11):
    raw = synthetic(n, seed)
    return E.build(raw, B.resample(raw[C.PEMICU], 14400))


def test_ema_dan_atr_warmup():
    e = E.ema([float(x) for x in range(1, 30)], 5)
    assert e[:4] == [None] * 4 and e[4] == 3.0
    cs = [{"h": 2.0, "l": 1.0, "c": 1.5}] * 30
    a = E.atr(cs, 14)
    assert a[13] is None and abs(a[14] - 1.0) < 1e-9


def test_korelasi_prefix_sama_dengan_perhitungan_langsung():
    """Korelasi O(1) dengan prefix sum harus sama dengan Pearson langsung pada jendela yang sama."""
    prep = _prep()
    e = prep["p"][C.PEMICU]["lr"]
    for pair in C.KONFIRMASI:
        lr = prep["p"][pair]["lr"]
        for i in (600, 650, 799):
            for w in C.CORR_WIN:
                fast = E.corr(prep, pair, i, w)
                slow = E.pearson(e[i - w + 1:i + 1], lr[i - w + 1:i + 1])
                assert (fast is None) == (slow is None)
                if fast is not None:
                    assert abs(fast - slow) < 1e-9


def test_korelasi_jendela_belum_cukup_none():
    prep = _prep()
    assert E.corr(prep, "EUR_JPY", 100, 500) is None


def test_quantile_dan_threshold():
    assert E.quantile([1, 2, 3, 4, 5], 0.5) == 3
    assert abs(E.quantile([1, 2, 3, 4], 0.7) - 3.1) < 1e-9
    assert E.thresholds([0.1] * 10) == (C.SKOR_WARMUP, C.SKOR_WARMUP, False)
    tb, ts, aktif = E.thresholds([i / 1000 for i in range(C.SKOR_MIN_SAMPEL)])
    assert aktif and tb > ts


def test_sl_dibatasi_10_sampai_15_pip():
    prep = {"p": {C.TARGET: {"c": [174.0], "atr": [0.0001]}}}
    lv = E.entry_levels(prep, 0, 1)
    assert lv["sl_pip"] == 10.0 and lv["sl"] < lv["entry"] < lv["tp"]
    prep["p"][C.TARGET]["atr"] = [2.0]          # 200 pip -> dibatasi 15
    lv = E.entry_levels(prep, 0, -1)
    assert lv["sl_pip"] == 15.0 and lv["sl"] > lv["entry"] > lv["tp"]


def test_konfirmasi_target_aligned_dan_divergent(monkeypatch):
    prep = {"p": {C.TARGET: {"c": [174.0, 174.1, 174.2], "ema": [None, 174.0, 174.05], "atr": [None] * 3},
                  "USD_JPY": {"lr": [0.0, 0.001, -0.001]}, "GBP_USD": {"lr": [0.0, 0.001, -0.001]}}}
    assert E.target_check(prep, 2, 1)[0] is False          # USD/JPY turun -> BUY ditolak
    prep["p"]["USD_JPY"]["lr"][2] = 0.002
    ok, det = E.target_check(prep, 2, 1)
    assert ok and det["logika"] == "aligned"
    monkeypatch.setitem(C.TARGET_RULES, C.TARGET, ("GBP_USD", -1))   # divergent
    prep["p"]["GBP_USD"]["lr"][2] = 0.002                  # GBP/USD naik searah trigger -> BUY ditolak
    assert E.target_check(prep, 2, 1)[0] is False
    prep["p"]["GBP_USD"]["lr"][2] = -0.002
    ok, det = E.target_check(prep, 2, 1)
    assert ok and det["logika"] == "divergent"


def test_h4_dan_sinkron():
    prep = _prep()
    assert prep["sinkron"] is True and len(prep["t"]) == 800
    assert all(v in (None, -1, 0, 1) for v in prep["h4"])


def test_trigger_warmup_tanpa_sinyal():
    d, det = E.trigger(_prep(120, 7), 50)
    assert d == 0 and det.get("alasan")


def test_analisa_struktur_keputusan():
    prep = _prep()
    res, skor = E.analyze(prep, len(prep["t"]) - 1, [], True)
    assert res["decision"] in {"NO_SIGNAL", "NO_TRADE", "BUY", "SELL"}
    if res["decision"] == "NO_SIGNAL":
        assert skor is None
    if res["label"].startswith("ENTRY"):
        assert res["alasan"] == [] and res["entry"] is not None


def test_berita_tidak_tersedia_menahan_entry(monkeypatch):
    prep = _prep()
    monkeypatch.setattr(E, "trigger", lambda p, i: (1, {}))
    monkeypatch.setattr(E, "weights", lambda p, i: {"pairs": {}, "rata_c50": 0.5, "kolaps": False, "ok": True})
    monkeypatch.setattr(E, "score", lambda wd, p, i: 0.5)
    monkeypatch.setattr(E, "target_check", lambda *a: (True, {}))
    res, _ = E.analyze(prep, len(prep["t"]) - 1, [], None)     # regime asli: kalender gagal -> ditahan
    assert any("kalender" in a for a in res["alasan"])
    assert not res["label"].startswith("ENTRY")


def test_jalur_entry_terbentuk(monkeypatch):
    prep = _prep()
    monkeypatch.setattr(E, "trigger", lambda p, i: (1, {}))
    monkeypatch.setattr(E, "weights", lambda p, i: {"pairs": {}, "rata_c50": 0.5, "kolaps": False, "ok": True})
    monkeypatch.setattr(E, "score", lambda wd, p, i: 0.5)
    monkeypatch.setattr(E, "regime", lambda *a: (True, []))
    monkeypatch.setattr(E, "target_check", lambda *a: (True, {}))
    res, skor = E.analyze(prep, len(prep["t"]) - 1, [], True)
    assert res["label"] == "ENTRY LONG" and res["decision"] == "BUY"
    assert res["sl"] < res["entry"] < res["tp"] and res["alasan"] == [] and skor == 0.5

# ---------------- pemantauan ----------------
BAR = "2026-11-24T10:00:00Z"
AWAL = C.to_epoch("2026-11-24T10:15:00Z")


def _now(iso):
    return datetime.fromisoformat(iso.replace("Z", "+00:00")).replace(tzinfo=timezone.utc)


def _m15(awal, specs):
    return [{"t": awal + 900 * i, "o": c, "h": h, "l": l, "c": c} for i, (h, l, c) in enumerate(specs)]


def _entry_buy(entry=174.00, sl=173.90, tp=174.10):
    row = {"pair": "EUR/JPY", "label": "ENTRY LONG", "decision": "BUY", "metode": "X",
           "entry": entry, "sl": sl, "tp": tp, "bar_terakhir": BAR}
    return PT.buat_entry(_now("2026-11-24T10:20:00Z"), [row])[0]


def test_entry_dicatat():
    e = _entry_buy()
    assert e["sumber"] == "ENTRY" and e["arah"] == "BUY" and e["sl_pip"] == 10.0


def test_tp_kena_titik_2_dan_mfe_mae():
    m15 = _m15(AWAL, [(174.05, 173.99, 174.04), (174.12, 173.98, 174.11)])
    out = PT.perbarui(_now("2026-11-24T10:35:00Z"), [_entry_buy()], lambda k: m15)
    e = out["selesai"][0]
    assert out["aktif"] == [] and e["hasil"] == "TP kena" and e["menit_kena"] == 30
    assert e["pip"] == 10.0 and e["mfe"] == 12.0 and e["mae"] == -2.0


def test_sl_konservatif_jika_satu_candle():
    m15 = _m15(AWAL, [(174.12, 173.85, 174.00)])
    e = PT.perbarui(_now("2026-11-24T10:30:00Z"), [_entry_buy()], lambda k: m15)["tampil"][0]
    assert e["hasil"] == "SL kena" and e["pip"] == -10.0 and e["menit_kena"] == 15


def test_titik_15_sampai_60_dan_evaluasi():
    m15 = _m15(AWAL, [(174.02, 173.98, 174.01), (174.03, 173.99, 174.02),
                      (174.04, 174.00, 174.03), (174.05, 174.01, 174.04)])
    out = PT.perbarui(_now("2026-11-24T11:20:00Z"), [_entry_buy()], lambda k: m15)
    t = out["tampil"][0]
    assert out["aktif"] == [] and t["hasil"] == "Selesai 60 menit"
    assert set(t["titik"]) == {"15", "30", "45", "60"} and t["titik"]["15"] == 1.0


def test_berjalan_abaikan_candle_sebelum_awal():
    m15 = _m15(AWAL - 900, [(174.50, 173.50, 173.60)]) + _m15(AWAL, [(174.02, 173.99, 174.01)])
    out = PT.perbarui(_now("2026-11-24T10:35:00Z"), [_entry_buy()], lambda k: m15)
    t = out["tampil"][0]
    assert t["status"] == "AKTIF" and t["hasil"] == "BERJALAN" and set(t["titik"]) == {"15"}


def test_tanpa_m15_menunggu_lalu_tidak_lengkap():
    s = _entry_buy()
    assert PT.perbarui(_now("2026-11-24T10:30:00Z"), [s], lambda k: None)["tampil"][0]["hasil"] == "Menunggu data M15"
    out = PT.perbarui(_now("2026-11-24T11:55:00Z"), [s], lambda k: None)   # dibuat 10:20, umur 95 menit
    assert out["selesai"][0]["hasil"] == "Data M15 tidak lengkap"


def test_tambah_tidak_menduplikasi(tmp_path, monkeypatch):
    monkeypatch.setattr(C, "PANTAU_AKTIF", str(tmp_path / "aktif.json"))
    row = {"pair": "EUR/JPY", "label": "ENTRY LONG", "decision": "BUY", "metode": "X",
           "entry": 174.0, "sl": 173.9, "tp": 174.1, "bar_terakhir": BAR}
    assert len(PT.tambah(_now("2026-11-24T10:20:00Z"), [row])) == 1
    assert PT.tambah(_now("2026-11-24T10:25:00Z"), [row]) == []
    assert len(PT.aktif_saat_ini()) == 1


def test_perbarui_state_arsipkan(tmp_path, monkeypatch):
    monkeypatch.setattr(C, "PANTAU_AKTIF", str(tmp_path / "aktif.json"))
    monkeypatch.setattr(C, "PANTAU_ARSIP", str(tmp_path / "arsip.jsonl"))
    C.save_json(C.PANTAU_AKTIF, {"aktif": [_entry_buy()]})
    PT.perbarui_state(_now("2026-11-24T10:30:00Z"), lambda k: _m15(AWAL, [(174.12, 173.99, 174.11)]))
    assert PT.aktif_saat_ini() == []
    assert (tmp_path / "arsip.jsonl").read_text(encoding="utf-8").count("\n") == 1

# ---------------- backtest dan main ----------------
def test_metrik_dan_drawdown():
    m = B.metrik([{"R": 1.0}, {"R": -1.0}, {"R": -1.0}, {"R": 2.0}], 96 * 30)
    assert m["n"] == 4 and m["wr"] == 50.0 and m["pf"] == 1.5
    assert m["dd_R"] == 2.0 and m["total_R"] == 1.0 and m["exp_R"] == 0.25


def test_resample_hanya_bar_lengkap():
    raw = synthetic(40, 5)[C.PEMICU]              # 2 bar H4 lengkap + 8 bar parsial
    assert len(B.resample(raw, 14400)) == 2


def test_backtest_berjalan_pada_data_sintetis():
    raw = synthetic(1500, 13)
    prep = E.build(raw, B.resample(raw[C.PEMICU], 14400))
    trades = B.run(prep)
    ev = B.evaluasi(trades, len(prep["t"]))
    assert {"in_sample", "out_of_sample", "walk_forward", "kriteria"} <= ev.keys()
    assert all(t["hasil"] in {"TP", "SL", "BELUM SELESAI"} for t in trades)


def test_validate_menangkap_ohlc_rusak():
    ok = {"t": 1, "o": 1.0, "h": 1.1, "l": 0.9, "c": 1.0}
    bad = {"t": 2, "o": 1.0, "h": 0.5, "l": 0.9, "c": 1.0}
    assert M.validate([ok]) == []
    assert "OHLC tidak logis" in M.validate([ok, bad])


def test_news_clean():
    now = C.utc_now()
    assert M.news_clean(None, now) is None
    assert M.news_clean([now.timestamp() + 600], now) is False
    assert M.news_clean([now.timestamp() + 3600], now) is True


def test_main_siklus_penuh(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    raw = synthetic(800, 11)
    prep = E.build(raw, B.resample(raw[C.PEMICU], 14400))
    h4 = B.resample(raw[C.PEMICU], 14400)
    monkeypatch.setattr(M, "fetch_all", lambda: (raw, h4, [], None, None))
    monkeypatch.setattr(M, "market_open", lambda now: True)
    monkeypatch.delenv("DISCORD_WEBHOOK_URL", raising=False)
    assert M.main() == 0
    assert (tmp_path / C.REPORT_MD).read_text(encoding="utf-8").startswith("# Laporan Run Skema Final")
    assert (tmp_path / C.SIGNAL_LOG).read_text(encoding="utf-8").count("\n") == 1
    assert (tmp_path / C.REPORT_JSON).exists()


def test_main_data_invalid_tidak_entry(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(M, "fetch_all", lambda: (None, None, None, None, "tes gagal"))
    monkeypatch.setattr(M, "market_open", lambda now: True)
    assert M.main() == 1
    assert "DATA INVALID" in (tmp_path / C.REPORT_MD).read_text(encoding="utf-8")


def test_persentil_atr_sliding_sama_dengan_brute_force():
    """Sliding window persentil harus sama dengan perhitungan langsung."""
    rnd = random.Random(3)
    atr_s = [None] * 5 + [rnd.uniform(0.0001, 0.002) for _ in range(400)]
    fast = E.persentil_atr(atr_s, 200)
    for i in range(len(atr_s)):
        win = [v for v in atr_s[max(0, i - 199):i + 1] if v is not None]
        if i < 5 + 199:
            assert fast[i] is None
        else:
            slow = 100.0 * sum(v <= atr_s[i] for v in win) / len(win)
            assert abs(fast[i] - slow) < 1e-9


def test_trigger_pakai_ema20_saat_volatilitas_tinggi():
    prep = _prep()
    p = prep["p"][C.PEMICU]
    i = len(prep["t"]) - 1
    p["pct"][i] = 90.0                       # volatilitas tinggi -> EMA 20
    p["ema_cepat"][i] = p["c"][i] - 1.0      # close di atas EMA20 -> BUY
    p["ema"][i] = p["c"][i] + 1.0            # EMA50 justru di atas close: tidak boleh dipakai
    k, d = p["k"], p["d"]
    k[i], d[i], k[i - 1], d[i - 1] = 30.0, 20.0, 10.0, 15.0   # cross up dari bawah 20
    p["atr"][i] = 0.01                       # di atas median ATR
    arah, det = E.trigger(prep, i)
    assert arah == 1 and det["ema_len"] == C.EMA_TRIGGER_CEPAT
    p["pct"][i] = 40.0                       # volatilitas rendah -> EMA 50, dan close di bawah EMA50
    arah, det = E.trigger(prep, i)
    assert arah == 0 and det["alasan"]
