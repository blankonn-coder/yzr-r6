"""Pemeriksaan kualitas data sesuai skema (bagian 3, STEP 3).

Aturan lulus: tidak ada NaN, duplikat, urutan waktu mundur, atau OHLC tidak logis.
Gap dan candle flat hanya dilaporkan, tidak otomatis menolak data.
"""
import pandas as pd

GAP_LAPOR_MENIT = 60          # gap di atas ini dilaporkan
AKHIR_PEKAN_JAM = 48          # gap di atas ini dianggap libur pasar


def check_candles(df):
    hasil = {"baris": int(len(df))}
    if df.empty:
        hasil.update({"lolos": False, "alasan": ["data kosong"]})
        return hasil

    t = pd.to_datetime(df["time"], utc=True)
    hasil["awal"] = str(t.iloc[0])
    hasil["akhir"] = str(t.iloc[-1])
    hasil["duplikat"] = int(t.duplicated().sum())
    selisih = t.diff().dt.total_seconds()
    hasil["waktu_mundur"] = int((selisih < 0).sum())
    hasil["nan"] = int(df[["open", "high", "low", "close"]].isna().any(axis=1).sum())

    mx = df[["open", "close"]].max(axis=1)
    mn = df[["open", "close"]].min(axis=1)
    hasil["ohlc_tidak_logis"] = int(((df["high"] < mx) | (df["low"] > mn)).sum())

    gap = selisih[(selisih > GAP_LAPOR_MENIT * 60) & (selisih <= AKHIR_PEKAN_JAM * 3600)]
    hasil["gap_dilaporkan"] = int(len(gap))
    hasil["gap_terbesar_menit"] = round(float(selisih.max()) / 60, 1) if len(selisih) else 0.0
    if "volume" in df.columns:
        hasil["candle_flat_volume0"] = int((df["volume"] == 0).sum())

    alasan = []
    if hasil["duplikat"]:
        alasan.append("ada duplikat timestamp")
    if hasil["waktu_mundur"]:
        alasan.append("urutan waktu mundur")
    if hasil["nan"]:
        alasan.append("ada nilai kosong")
    if hasil["ohlc_tidak_logis"]:
        alasan.append("ada OHLC tidak logis")
    hasil["lolos"] = not alasan
    hasil["alasan"] = alasan
    return hasil


def check_bid_ask(bid, ask):
    """Bid harus <= ask pada setiap menit yang ada di kedua sisi."""
    gabung = bid[["time", "close"]].merge(ask[["time", "close"]], on="time", suffixes=("_bid", "_ask"))
    terbalik = int((gabung["close_bid"] > gabung["close_ask"]).sum())
    selisih_pip = (gabung["close_ask"] - gabung["close_bid"]).abs() / 0.0001
    return {
        "menit_cocok": int(len(gabung)),
        "bid_lebih_tinggi_dari_ask": terbalik,
        "spread_median_pip": round(float(selisih_pip.median()), 2) if len(gabung) else None,
        "lolos": terbalik == 0 and len(gabung) > 0,
    }
