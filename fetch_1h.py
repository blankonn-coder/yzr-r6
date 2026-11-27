"""Ambil data 1 jam (730 hari) dari Yahoo untuk bot peringatan. Dipanggil oleh .github/workflows/peringatan.yml.
Hasil: data/1h/<PAIR>_1h.csv dengan kolom time,open,high,low,close."""
import os
import pandas as pd
import yfinance as yf

PAIRS = ["AUDUSD", "EURAUD", "EURCAD", "EURGBP", "EURJPY", "EURNZD", "EURUSD",
         "GBPUSD", "NZDUSD", "USDCAD", "USDCHF", "USDJPY"]
OUT = "data/1h"


def main():
    os.makedirs(OUT, exist_ok=True)
    for p in PAIRS:
        t = yf.download(p + "=X", period="730d", interval="1h",
                        progress=False, auto_adjust=False)
        if t is None or t.empty:
            print(p, "kosong, dilewati")
            continue
        t.columns = [c[0].lower() if isinstance(c, tuple) else c.lower() for c in t.columns]
        t = t[["open", "high", "low", "close"]].dropna()
        t.index = pd.to_datetime(t.index, utc=True)
        t.index.name = "time"
        t.to_csv(f"{OUT}/{p}_1h.csv")
        print(p, len(t), t.index.max())


if __name__ == "__main__":
    main()
