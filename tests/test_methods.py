import unittest

import pandas as pd

from src import indicators as I
from src.methods import METODE
from src.regime import classify
from src.resample import bias_h4
from tests.helpers import ohlc_acak


def _h4(df):
    # H4 sintetis dari H1: agregasi 4 bar
    g = df.groupby(pd.RangeIndex(len(df)) // 4)
    h4 = pd.DataFrame({
        "time": g["time"].first().values,
        "open": g["open"].first().values,
        "high": g["high"].max().values,
        "low": g["low"].min().values,
        "close": g["close"].last().values,
    })
    return h4


class TestRegime(unittest.TestCase):
    def test_label_dan_belum_siap(self):
        ind = I.build(ohlc_acak(400))
        r = classify(ind)
        self.assertEqual(r["regime"].iloc[0], "BELUM SIAP")
        valid = set(r["regime"].unique())
        self.assertTrue(valid <= {"BELUM SIAP", "TRENDING KUAT", "TRENDING LEMAH", "RANGING",
                                  "VOLATIL/CHOPPY", "MIXED", "TIDAK JELAS"})

    def test_aturan_satu_label(self):
        import pandas as pd
        ind = pd.DataFrame({"adx14": [30.0, 10.0, 22.0], "hurst100": [0.6, 0.4, 0.47],
                            "atr_pct": [60.0, 30.0, 40.0], "bb_width_pct": [50.0, 50.0, 10.0]})
        r = classify(ind)
        self.assertEqual(r["regime"].tolist(), ["TRENDING KUAT", "RANGING", "TRENDING LEMAH"])
        self.assertEqual(r["squeeze"].tolist(), [False, False, True])


class TestMetode(unittest.TestCase):
    def setUp(self):
        self.h1 = ohlc_acak(2000, seed=11)
        self.pip = 0.0001
        self.h4 = bias_h4(_h4(self.h1))

    def test_kolom_dan_arah_valid(self):
        for nama, mod in METODE.items():
            s = mod.signals(self.h1, self.pip, h4_bias=self.h4)
            self.assertEqual(list(s.columns), ["direction", "sl_dist", "reason"], nama)
            self.assertTrue(set(s["direction"].unique()) <= {-1, 0, 1}, nama)
            sinyal = s[s["direction"] != 0]
            self.assertTrue((sinyal["sl_dist"] > 0).all(), nama)

    def test_tanpa_look_ahead(self):
        """Sinyal pada bar k dengan data sampai k harus sama dengan sinyal penuh di bar k."""
        for nama, mod in METODE.items():
            penuh = mod.signals(self.h1, self.pip, h4_bias=self.h4)
            for k in (600, 1200, 1999):
                h1k = self.h1.iloc[: k + 1].reset_index(drop=True)
                h4k = self.h4[self.h4["close_time"] <= h1k["time"].iloc[-1] + pd.Timedelta(hours=1)]
                potong = mod.signals(h1k, self.pip, h4_bias=h4k)
                self.assertEqual(int(penuh["direction"].iloc[k]), int(potong["direction"].iloc[k]), f"{nama} bar {k}")

    def test_sl_dijepit_metode_a_dan_c(self):
        for nama in ("A", "C"):
            s = METODE[nama].signals(self.h1, self.pip, h4_bias=self.h4)
            sl = s["sl_dist"].dropna()
            if len(sl):
                self.assertTrue((sl >= 10 * self.pip - 1e-12).all(), nama)
                self.assertTrue((sl <= 30 * self.pip + 1e-12).all(), nama)


if __name__ == "__main__":
    unittest.main()
