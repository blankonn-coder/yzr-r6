import unittest

import numpy as np
import pandas as pd

from src.backtest.engine import simulate
from src.backtest.metrics import ringkas
from src.backtest.ranking import skor, bintang, kelayakan

PIP = 0.0001


def bar(o, h, l, c, n):
    return pd.DataFrame({"open": [o] * 0 + list(o) if False else o, "high": h, "low": l, "close": c})


def frame(rows):
    """rows: list of (open, high, low, close)."""
    a = np.array(rows, dtype=float)
    return pd.DataFrame({"open": a[:, 0], "high": a[:, 1], "low": a[:, 2], "close": a[:, 3]})


def sinyal(n, arah_di, dist=0.0010):
    d = np.zeros(n, dtype=int)
    s = np.full(n, np.nan)
    for i, x in arah_di.items():
        d[i] = x
        s[i] = dist
    return pd.DataFrame({"direction": d, "sl_dist": s})


def ind_kosong(n):
    cols = ["fisher9", "ema50", "ma200", "macd_hist", "stoch_k", "bb_upper", "bb_lower", "atr14"]
    return pd.DataFrame({c: np.full(n, np.nan) for c in cols})


class TestEngine(unittest.TestCase):
    def setUp(self):
        self.pip = PIP

    def test_masuk_di_open_bar_berikutnya_dengan_ask_dan_tp(self):
        # sinyal LONG di bar 0; entry di ask open bar 1 = 1.1000; SL 10 pip; TP 1.5R = 15 pip (metode A)
        ask = frame([(1.1000, 1.1002, 1.0998, 1.1000), (1.1000, 1.1020, 1.0995, 1.1015), (1.1015, 1.1016, 1.1014, 1.1015)])
        bid = ask.copy()
        bid[["open", "high", "low", "close"]] = bid[["open", "high", "low", "close"]] - 0.0002
        mid = bid.copy()
        sig = sinyal(3, {0: 1})
        tr, _ = simulate("A", sig, bid, ask, mid, ind_kosong(3), self.pip, slip_pip=0.0)
        self.assertEqual(len(tr), 1)
        t = tr[0]
        self.assertEqual(t["entry_i"], 1)
        self.assertAlmostEqual(t["entry"], 1.1000)
        self.assertAlmostEqual(t["sl"], 1.0990)
        self.assertAlmostEqual(t["tp"], 1.1015)
        self.assertEqual(t["reason"], "TP")
        self.assertAlmostEqual(t["r"], 1.5, places=6)
        self.assertAlmostEqual(t["pips"], 15.0, places=4)

    def test_sl_dan_tp_pada_bar_sama_sl_didahulukan(self):
        ask = frame([(1.1000, 1.1002, 1.0998, 1.1000), (1.1000, 1.1020, 1.0980, 1.1000), (1.1000, 1.1000, 1.1000, 1.1000)])
        bid = ask.copy()
        sig = sinyal(3, {0: 1})
        tr, _ = simulate("A", sig, bid, ask, bid, ind_kosong(3), self.pip, slip_pip=0.0)
        self.assertEqual(tr[0]["reason"], "SL")
        self.assertAlmostEqual(tr[0]["r"], -1.0, places=6)

    def test_gap_melewati_sl_keluar_di_open(self):
        # entry 1.1000 di open bar 1 (tidak tersentuh SL), bar 2 gap turun ke 1.0950 melewati SL 1.0990
        ask = frame([(1.1000, 1.1002, 1.0998, 1.1000), (1.1000, 1.1002, 1.0999, 1.1000), (1.0950, 1.0960, 1.0940, 1.0955)])
        bid = ask.copy()
        sig = sinyal(3, {0: 1})
        tr, _ = simulate("A", sig, bid, ask, bid, ind_kosong(3), self.pip, slip_pip=0.0)
        self.assertEqual(tr[0]["reason"], "SL")
        self.assertAlmostEqual(tr[0]["exit"], 1.0950)
        self.assertLess(tr[0]["r"], -1.0)

    def test_short_masuk_di_bid_dan_keluar_di_ask(self):
        ask = frame([(1.1000, 1.1002, 1.0998, 1.1000), (1.1000, 1.1002, 1.0980, 1.0985), (1.0985, 1.0986, 1.0984, 1.0985)])
        bid = ask.copy()
        bid[["open", "high", "low", "close"]] = bid[["open", "high", "low", "close"]] - 0.0002
        sig = sinyal(3, {0: -1})
        tr, _ = simulate("A", sig, bid, ask, bid, ind_kosong(3), self.pip, slip_pip=0.0)
        self.assertEqual(tr[0]["dir"], -1)
        self.assertAlmostEqual(tr[0]["entry"], 1.0998)
        self.assertEqual(tr[0]["reason"], "TP")

    def test_cooldown_memblokir_sinyal_berikutnya(self):
        # trade pertama kena SL di bar 1 -> cooldown metode A = 2 bar: cool_until = 3
        ask = frame([(1.1, 1.1, 1.1, 1.1)] * 8)
        ask.loc[1, ["open", "high", "low", "close"]] = [1.1, 1.1, 1.0980, 1.0985]  # SL
        ask.loc[4, "high"] = 1.1020  # trade kedua kena TP agar tertutup
        bid = ask.copy()
        sig = sinyal(8, {0: 1, 2: 1, 3: 1})
        tr, _ = simulate("A", sig, bid, ask, bid, ind_kosong(8), self.pip, slip_pip=0.0)
        self.assertEqual([t["entry_i"] for t in tr], [1, 4])

    def test_entry_ok_false_menahan_entry(self):
        ask = frame([(1.1, 1.1, 1.1, 1.1)] * 4)
        sig = sinyal(4, {0: 1})
        ok = np.array([True, False, True, True])
        tr, _ = simulate("A", sig, ask, ask, ask, ind_kosong(4), self.pip, slip_pip=0.0, entry_ok=ok)
        self.assertEqual(tr, [])

    def test_posisi_terbuka_di_akhir_dihitung(self):
        ask = frame([(1.1, 1.1001, 1.0999, 1.1)] * 3)
        sig = sinyal(3, {0: 1})
        tr, terbuka = simulate("A", sig, ask, ask, ask, ind_kosong(3), self.pip, slip_pip=0.0)
        self.assertEqual(tr, [])
        self.assertEqual(terbuka, 1)


class TestMetrik(unittest.TestCase):
    def test_pf_expectancy_dd(self):
        m = ringkas([1.5, -1.0, 1.5, -1.0])
        self.assertAlmostEqual(m["pf"], 1.5)
        self.assertAlmostEqual(m["expectancy_r"], 0.25)
        self.assertAlmostEqual(m["win_rate"], 0.5)
        self.assertAlmostEqual(m["max_dd_r"], 1.0)
        self.assertEqual(m["max_loss_beruntun"], 1)

    def test_tanpa_trade(self):
        m = ringkas([])
        self.assertEqual(m["trade"], 0)
        self.assertIsNone(m["pf"])

    def test_stabilitas_fold(self):
        m = ringkas([1.0, -0.5, 1.0, 1.0], fold=[0, 1, 2, 3], n_folds=4)
        self.assertEqual(m["fold_profit"], 3)
        self.assertAlmostEqual(m["stabilitas"], 0.75)


class TestRanking(unittest.TestCase):
    def test_kelayakan_dan_provisional(self):
        m = ringkas([1.5] * 10 + [-1.0] * 5, fold=[0] * 15, n_folds=4)
        ok, alasan = kelayakan(m)
        self.assertFalse(ok)
        self.assertIn("sampel kurang", alasan)
        b, status = bintang(skor(m), m["trade"], ok)
        self.assertEqual(b, 0)
        self.assertIn("PROVISIONAL", status)

    def test_pf_rendah_tidak_prioritas(self):
        r = [0.5, -1.0] * 40  # PF 0.5, sampel cukup
        m = ringkas(r, fold=[i % 4 for i in range(80)], n_folds=4)
        ok, alasan = kelayakan(m)
        self.assertFalse(ok)
        self.assertIn("PF <= 1", alasan)

    def test_bintang_dari_skor(self):
        self.assertEqual(bintang(95, 120, True)[0], 5)
        self.assertEqual(bintang(85, 120, True)[0], 4)
        self.assertEqual(bintang(72, 120, True)[0], 3)
        self.assertEqual(bintang(65, 120, True)[0], 2)


if __name__ == "__main__":
    unittest.main()
