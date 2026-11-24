"""Konfigurasi Adaptive Forex Scanner (Skema FINAL BERSIH v2).

Nilai dari spesifikasi ditulis apa adanya. Nilai yang TIDAK ada di spesifikasi
diberi komentar ASUMSI dan perlu dikonfirmasi.
"""
import json
import os
from datetime import datetime, timezone

# ---- §1 Sumber data ----
BIQUOTE_HOST = "https://biquote.io"
BIQUOTE_CALENDAR_PATH = "/api/calendar"  # ASUMSI: belum diverifikasi ke dokumentasi biquote
SPREAD_TERSEDIA = False                   # ubah True setelah OANDA tersambung (§1, §10)
# Timeframe utama (regime, sinyal, entry): H1 sesuai spesifikasi §2. M15 hanya untuk analisa cadangan.
TF_MAIN = "1h"
TF_MAIN_SEC = 3600
TF_BIAS = "4h"                            # bias EMA50 vs EMA200
H1_COUNT = 500                            # warm-up EMA200 + persentil 100 + Hurst 100 (ASUMSI batas API)
H4_COUNT = 300

# ---- §2 Pair (15 pair) ----
PAIRS = [
    "EUR_USD", "GBP_USD", "USD_JPY", "USD_CHF", "AUD_USD", "USD_CAD", "NZD_USD",
    "EUR_GBP", "EUR_JPY", "EUR_CHF", "EUR_AUD", "EUR_CAD", "EUR_NZD",
    "XAU_USD", "XAU_AUD",
]

# ---- Periode indikator (ASUMSI periode standar; spesifikasi tidak menyebutkannya) ----
ATR_PERIOD = 14
EMA_FAST, EMA_SLOW = 50, 200
MA_PERIOD = 200
ADX_PERIOD = 14
MACD_FAST, MACD_SLOW, MACD_SIG = 12, 26, 9
STOCH_K, STOCH_SMOOTH, STOCH_D = 14, 3, 3
BB_PERIOD, BB_MULT = 20, 2.0
FISHER_PERIOD = 10
PCT_LOOKBACK = 100          # §4: lookback persentil 100 candle
HURST_LOOKBACK = 100        # §4: R/S pada 100 return
HURST_CHUNKS = (10, 20, 50)  # §4: potongan 10, 20, 50

# ---- §4 Regime (H1) ----
REG_ADX_STRONG = 25
REG_HURST_STRONG = 0.5
REG_ATRPCT_STRONG = 50
REG_ADX_WEAK_MIN = 20
REG_HURST_WEAK_MIN = 0.45
REG_ATRPCT_CHOP = 80
BB_SQUEEZE_PCT = 20

# ---- §6 Simulasi backtest ----
SLIP_PIPS = 0.3
SPREAD_MAX_PIPS_EURUSD = 2
SPREAD_MAX_PIPS_DEFAULT = 3       # XAU: 3 pip = 0.3 USD (§6b)
SPREAD_MEDIAN_MULT = 1.5
SPREAD_MEDIAN_BARS = 20
NEWS_WINDOW_MIN = 30
N_FOLDS = 4

# ---- Analisa cadangan (BUKAN sinyal, hanya saat NO TRADE / WATCHLIST) ----
CADANGAN_ENABLED = True
CADANGAN_H1_MAX_ATR = 1.5     # level H1 ditampilkan jika jaraknya maksimal 1,5 ATR
CADANGAN_M15_MAX_ATR = 1.0    # level M15 ditampilkan jika jaraknya maksimal 1 ATR
TF_CADANGAN = "15m"           # ASUMSI: interval M15 biquote belum diverifikasi
M15_COUNT = 300
CADANGAN_SNAPSHOT_PATH = "database/analisa_cadangan.jsonl"
CADANGAN_OUTCOME_PATH = "database/analisa_cadangan_hasil.jsonl"
CADANGAN_OUTCOME_BARS = (1, 4, 12)

# ---- Saran analisa cadangan (BUKAN sinyal, tidak divalidasi backtest, tidak mengubah label) ----
CADANGAN_SARAN_N = 3              # jumlah pair saran per run
CADANGAN_TAMPIL_MAKS = 3          # maks pair level cadangan yang tampil di Discord (urut jarak terdekat)
CADANGAN_SARAN_MAX_ATR = 1.0      # hanya level H1 dengan jarak maksimal 1 ATR dari harga
CADANGAN_SARAN_SL_ATR = 0.5       # SL = level dikurangi/ditambah 0,5 ATR H1 (sisi seberang harga)
CADANGAN_SARAN_TP_R = 1.5         # TP = entry ± 1,5 R (R = jarak entry ke SL)
# ---- Pemantauan entry dan saran cadangan ----
PANTAU_TITIK_MENIT = 15           # titik cek tiap 15 menit (close candle M15)
PANTAU_TOTAL_MENIT = 60           # setelah 60 menit dibuat evaluasi 1 jam
PANTAU_TIMEOUT_MENIT = 90         # jika candle M15 belum lengkap sampai 90 menit, evaluasi ditutup
PANTAU_AKTIF_PATH = "state/pemantauan_aktif.json"
PANTAU_ARSIP_PATH = "database/pemantauan.jsonl"

# ---- Lead-lag (analisa cadangan, BUKAN sinyal) ----
# Pair leader memicu follower yang merespons lebih lambat (5-60 menit). Data M5 dari biquote.
LEADLAG_ENABLED = True
TF_LEADLAG = "5m"                    # ASUMSI: interval M5 biquote belum diverifikasi. Jika gagal, pair dilewati.
TF_LEADLAG_SEC = 300
LEADLAG_FETCH_COUNT = 100            # bar M5 per pair per run (3 bar baru masuk, 3 terlama keluar)
LEADLAG_WINDOW_BARS = 72             # jendela backtest 6 jam = 72 bar M5
LEADLAG_LAGS = tuple(range(1, 13))   # lag 5..60 menit (1..12 bar M5)
LEADLAG_MIN_SAMPLE = 20              # sampel minimal per lag
LEADLAG_MIN_CORR = 0.5               # |korelasi| minimal di lag terbaik
LEADLAG_TRIGGER_Z = 1.0              # leader sudah bergerak >= 1 sigma (dinormalkan ke k bar) dalam lag
LEADLAG_FOLLOW_MAX_Z = 0.3           # follower belum bergerak lebih dari 0,3 sigma searah
# Store bergulir: hanya jendela terakhir yang disimpan. Tiap update 15 menit, 3 bar terlama dibuang
# dan 3 bar baru masuk, sehingga ukuran file tetap (tidak membengkak).
LEADLAG_RETENSI_BARS = LEADLAG_WINDOW_BARS
LEADLAG_SARAN_N = 3                  # saran lead-lag per run, terpisah dari saran analisa cadangan (CADANGAN_SARAN_N)
LEADLAG_STABIL_MIN_CORR = 0.3        # korelasi di tiap paruh jendela (3 jam) harus searah dan >= ini
LEADLAG_PATH = "database/leadlag_backtest.json"
LEADLAG_PAIRS = [
    "GBP_JPY", "GBP_CHF", "GBP_AUD", "GBP_CAD", "GBP_NZD",
    "AUD_JPY", "AUD_CHF", "AUD_CAD", "AUD_NZD",
    "CAD_JPY", "CAD_CHF", "CHF_JPY", "NZD_JPY", "NZD_CAD", "NZD_CHF",
]
# Semua pair yang dipakai lead-lag (leader dan follower). Follower hanya dari PAIRS (scanner).
LEADLAG_UNIVERSE = LEADLAG_PAIRS + [p for p in PAIRS if p not in LEADLAG_PAIRS]

# ---- §7 Ranking ----
RANK_MIN_SAMPLE = 30
RANK_PF_MIN = 1.0
RANK_EXP_MIN = 0.0
RANK_DD_MAX = 15.0
# KEPUTUSAN: semua bintang (1-5) boleh dipakai. Bintang dan statistik sel ditampilkan di laporan.
# Penguci (PF > 1, expectancy > 0, DD <= 15R) dan sampel >= 30 tetap berlaku.
RANK_PRIORITY_STARS = 1

# ---- Waktu & path ----
NEWS_ARCHIVE_PATH = "database/news_archive.jsonl"
RANKING_HISTORY_PATH = "database/ranking_history.jsonl"
RANKING_MD_PATH = "reports/ranking.md"
SCANNER_MD_PATH = "reports/scanner_latest.md"
SCANNER_JSON_PATH = "scanner/latest.json"
RISK_STATE_PATH = "state/risk_state.json"
DB_PATH = "database/signal_history.json"   # arsip lama, read-only


def utc_now():
    return datetime.now(timezone.utc)


def fmt(dt):
    return dt.strftime("%Y-%m-%dT%H:%M:%SZ")


def to_epoch(v):
    """Epoch detik dari angka (detik/milidetik), string angka, atau string ISO-8601."""
    s = str(v).strip()
    try:
        x = float(s)
    except ValueError:
        return int(datetime.fromisoformat(s.replace("Z", "+00:00")).timestamp())
    return int(x / 1000) if x > 1e11 else int(x)


def disp(pair):
    return pair.replace("_", "/")


def pip_size(pair):
    """1 pip: XAU = 0.1 USD (§6b), pair JPY = 0.01, selain itu = 0.0001."""
    p = pair.upper()
    if p.startswith("XAU"):
        return 0.1
    return 0.01 if "JPY" in p else 0.0001


def spread_max_pips(pair):
    return SPREAD_MAX_PIPS_EURUSD if pair == "EUR_USD" else SPREAD_MAX_PIPS_DEFAULT


def load_json(path, default):
    if os.path.exists(path):
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    return default


def save_json(path, data):
    d = os.path.dirname(path)
    if d:
        os.makedirs(d, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
