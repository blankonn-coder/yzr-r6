import unittest

import numpy as np
import pandas as pd

from src import indicators as I
from tests.helpers import ohlc_acak


class TestIndikatorNilai(unittest.TestCase):
    def test_sma_dan_ema_sederhana(self):
        s = pd.Series([1.0, 2.0, 3.0, 4.0, 5.0])
        self.assertEqual(I.sma(s, 3).iloc[-1], 4.0)
        self.assertAlmostEqual(I.ema(s, 3).iloc[-1], 4.0625)

    def test_atr_konstan(self):
        df = pd.DataFrame({"open": [1.0] * 30, "high": [1.1] * 30, "low": [0.9] * 30, "close": [1.0] * 30})
        self.assertAlmostEqual(I.atr(df, 14).iloc[-1], 0.2, places=6)

    def test_rsi_naik_terus_mendekati_100(self):
        s = pd.Series(np.arange(1.0, 60.0))
        self.assertGreater(I.rsi(s, 14).iloc[-1], 95)

    def test_stoch_pada_puncak(self):
        df = ohlc_acak(60)
        df.loc[df.index[-1], "close"] = df["high"].max()
        k = I.stoch(df)["k"]
        self.assertTrue(np.isfinite(k.iloc[-1]))

    def test_hurst_random_walk_sekitar_0_5(self):
        rng = np.random.default_rng(7)
        close = pd.Series(1.0 + np.cumsum(rng.normal(0, 0.001, 3000)))
        h = I.hurst(close, 100).dropna()
        self.assertGreater(h.mean(), 0.35)
        self.assertLess(h.mean(), 0.65)

    def test_fisher_nan_di_awal_saja(self):
        f = I.fisher(ohlc_acak(60), 9)
        self.assertTrue(f.iloc[:8].isna().all())
        self.assertTrue(f.iloc[20:].notna().all())


class TestTanpaLookAhead(unittest.TestCase):
    """Nilai indikator di bar k harus sama jika data hanya sampai bar k."""

    def test_semua_indikator_kausal(self):
        df = ohlc_acak(400)
        penuh = I.build(df)
        for k in (150, 250, 399):
            potong = I.build(df.iloc[: k + 1])
            for kol in penuh.columns:
                a = penuh[kol].iloc[k]
                b = potong[kol].iloc[k]
                if pd.isna(a) and pd.isna(b):
                    continue
                self.assertAlmostEqual(a, b, places=9, msg=f"{kol} bar {k}")


if __name__ == "__main__":
    unittest.main()
