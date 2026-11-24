"""Tahap 1: unduh dan muat histori Dukascopy (BID dan ASK) untuk backtest.

Sumber ini hanya dipakai untuk backtest. Live tetap memakai biquote.
Data disimpan di DUKA_DIR (diabaikan git). Lihat .gitignore.
"""
from dukascopy_downloader import Downloader, load

DUKA_DIR = "data/dukascopy"


def simbol_unduh(pair):
    """EUR_USD -> EURUSD (format yang diterima downloader)."""
    return pair.replace("_", "")


def kode_muat(pair):
    """EUR_USD -> EUR-USD (nama folder yang dibuat downloader)."""
    return pair.replace("_", "-")


def unduh(pair, start):
    """Unduh M1 BID dan ASK mulai tanggal start (YYYY-MM-DD) sampai data terbaru."""
    dl = Downloader(DUKA_DIR)
    dl.download([simbol_unduh(pair)], tf="m1", start=start, sides="both")


def muat(pair, side, start, end):
    """Muat M1 satu sisi (BID atau ASK) sebagai DataFrame dalam rentang tanggal."""
    return load(DUKA_DIR, kode_muat(pair), "m1", side=side, start=start, end=end)
