import unittest
from datetime import datetime, timezone
from unittest import mock

import numpy as np
import pandas as pd

from src.scanner import live
from tests.helpers import ohlc_acak

SEKARANG = datetime(2026, 11, 24, 10, 0, tzinfo=timezone.utc)


def _rank(**kw):
    base = {"pair": "EUR_USD", "tf": "H1", "regime": "TRENDING KUAT", "metode": "A", "arah": "LONG",
            "bintang": 4, "skor": 85.0, "status": "PRIORITAS"}
    base.update(kw)
    return base


class TestKeputusan(unittest.TestCase):
    def test_tanpa_ranking_no_trade(self):
        h1 = ohlc_acak(600, seed=3)
        h4 = h1.iloc[::4].reset_index(drop=True)
        r = live.evaluasi("EUR_USD", h1, h4, [], SEKARANG)
        self.assertEqual(r["label"], "NO TRADE")
        self.assertIn("tidak ada metode PRIORITAS", r["alasan"][0])

    def test_regime_tidak_cocok_no_trade(self):
        h1 = ohlc_acak(600, seed=3)
        h4 = h1.iloc[::4].reset_index(drop=True)
        rk = [_rank(regime="RANGING")]
        with mock.patch.object(live, "cek_news", return_value=(False, True)):
            r = live.evaluasi("EUR_USD", h1, h4, rk, SEKARANG)
        if r["regime"] != "RANGING":
            self.assertEqual(r["label"], "NO TRADE")

    def test_spread_tidak_terverifikasi_jadi_watchlist(self):
        # memaksa sinyal: metode A dengan sinyal palsu
        h1 = ohlc_acak(600, seed=3)
        h4 = h1.iloc[::4].reset_index(drop=True)
        fake = (1, 0.001, "uji")
        rk = [_rank(regime=live.classify(live.build(h1))["regime"].iloc[-1])]
        with mock.patch.object(live, "_sinyal_metode", return_value=fake), \
             mock.patch.object(live, "cek_news", return_value=(False, True)):
            r = live.evaluasi("EUR_USD", h1, h4, rk, SEKARANG)
        self.assertEqual(r["label"], "WATCHLIST")
        self.assertIn("spread belum", " ".join(r["alasan"]))
        self.assertAlmostEqual(r["rencana"]["sl"], round(r["rencana"]["harga_acuan"] - 0.001, 5), places=5)

    def test_news_memblokir(self):
        h1 = ohlc_acak(600, seed=3)
        h4 = h1.iloc[::4].reset_index(drop=True)
        rk = [_rank(regime=live.classify(live.build(h1))["regime"].iloc[-1])]
        with mock.patch.object(live, "_sinyal_metode", return_value=(1, 0.001, "uji")), \
             mock.patch.object(live, "cek_news", return_value=(True, True)):
            r = live.evaluasi("EUR_USD", h1, h4, rk, SEKARANG)
        self.assertEqual(r["label"], "WATCHLIST")
        self.assertIn("news", " ".join(r["alasan"]))

    def test_kalender_gagal_tidak_entry(self):
        h1 = ohlc_acak(600, seed=3)
        h4 = h1.iloc[::4].reset_index(drop=True)
        rk = [_rank(regime=live.classify(live.build(h1))["regime"].iloc[-1])]
        with mock.patch.object(live, "_sinyal_metode", return_value=(1, 0.001, "uji")), \
             mock.patch.object(live, "cek_news", return_value=(False, False)):
            r = live.evaluasi("EUR_USD", h1, h4, rk, SEKARANG)
        self.assertNotIn(r["label"], ("ENTRY LONG", "ENTRY SHORT"))

    def test_data_gagal_data_invalid(self):
        with mock.patch.object(live, "ambil_data", return_value=(None, None, "gagal ambil data: x")), \
             mock.patch.object(live, "muat_ranking", return_value=[]):
            laporan = live.jalankan(["EUR_USD"])
        self.assertEqual(laporan["hasil"][0]["label"], "DATA INVALID")


if __name__ == "__main__":
    unittest.main()
