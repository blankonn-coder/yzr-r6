import unittest

from src.resample import resample_ohlc
from tests.helpers import m1_sintetis


class TestResample(unittest.TestCase):
    def test_h1_jumlah_dan_bar_lengkap(self):
        m1 = m1_sintetis(n_menit=60 * 10)  # 10 jam penuh
        h1 = resample_ohlc(m1, "H1")
        self.assertEqual(len(h1), 10)
        self.assertEqual(str(h1["time"].iloc[0]), "2026-10-01 00:00:00+00:00")

    def test_bar_tidak_lengkap_dibuang(self):
        m1 = m1_sintetis(n_menit=60 * 3 + 30)  # 3 jam + 30 menit: jam ke-4 belum selesai
        h1 = resample_ohlc(m1, "H1")
        self.assertEqual(len(h1), 3)

    def test_ohlc_benar(self):
        m1 = m1_sintetis(n_menit=60)
        h1 = resample_ohlc(m1, "H1")
        self.assertAlmostEqual(h1["open"].iloc[0], m1["open"].iloc[0])
        self.assertAlmostEqual(h1["close"].iloc[0], m1["close"].iloc[-1])
        self.assertAlmostEqual(h1["high"].iloc[0], m1["high"].max())
        self.assertAlmostEqual(h1["low"].iloc[0], m1["low"].min())


if __name__ == "__main__":
    unittest.main()
