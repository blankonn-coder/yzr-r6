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
TF_MAIN = "1h"                            # regime, sinyal, entry
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

# ---- §7 Ranking ----
RANK_MIN_SAMPLE = 30
RANK_PF_MIN = 1.0
RANK_EXP_MIN = 0.0
RANK_DD_MAX = 15.0
RANK_PRIORITY_STARS = 3

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
