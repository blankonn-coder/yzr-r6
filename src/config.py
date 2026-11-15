"""Konfigurasi bot screening forex (Skema v6.0)."""
import json
import os
from datetime import datetime, timezone

# ---- Sumber data: biquote (publik, tanpa API key) ----
BIQUOTE_HOST = "https://biquote.io"
CANDLE_COUNT = 200

# ---- 27 pair. Sesuaikan dengan daftar pair Finex Anda ----
PAIRS = [
    "EUR_USD", "GBP_USD", "USD_JPY", "USD_CHF", "AUD_USD", "USD_CAD", "NZD_USD",
    "EUR_GBP", "EUR_JPY", "EUR_CHF", "EUR_AUD", "EUR_CAD", "EUR_NZD",
    "GBP_JPY", "GBP_CHF", "GBP_AUD", "GBP_CAD", "GBP_NZD",
    "AUD_JPY", "AUD_CHF", "AUD_CAD", "AUD_NZD",
    "NZD_JPY", "NZD_CHF", "NZD_CAD", "CAD_JPY", "CAD_CHF",
]

TF_GRAN = {"5m": "5m", "15m": "15m", "30m": "30m", "1h": "1h", "4h": "4h"}  # interval biquote

# ---- Support & Resistance ----
SR_TFS = ["5m", "15m", "30m"]
SR_LOOKBACK = 5
SR_MIN_TOUCH = 2
SR_TOL_PCT = 0.15
SR_MAX_AGE = 48
SR_WEIGHTS = {"5m": 30, "15m": 25, "30m": 15}

# ---- RSI ----
RSI_TFS = ["5m", "15m", "30m"]
RSI_PERIOD = 14
RSI_OVERSOLD = 30
RSI_OVERBOUGHT = 70
RSI_WEIGHTS = {"5m": 10, "15m": 10, "30m": 10}

# ---- Filter tren ----
TREND_TFS = ["1h", "4h"]
EMA_PERIOD = 50

# ---- Keputusan ----
THRESHOLD = 45
MIN_DIFF = 10

# ---- Pemantauan & waktu ----
MONITOR_MINUTES = 60
LATE_MINUTES = 5

# ---- Database ----
RETENSI_HARI = 30
MIN_RETENSI_HARI = 7

# ---- Path ----
DB_PATH = "database/signal_history.json"
MONITOR_PATH = "state/monitoring_state.json"
CALIB_PATH = "state/calibration_state.json"
REPORT_PATH = "reports/latest_report.md"


def utc_now():
    return datetime.now(timezone.utc)


def fmt(dt):
    return dt.strftime("%Y-%m-%dT%H:%M:%SZ")


def parse(s):
    return datetime.strptime(s, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)


def disp(pair):
    return pair.replace("_", "/")


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


def pip_size(pair):
    """Ukuran 1 pip: pair JPY = 0.01, selain JPY = 0.0001."""
    return 0.01 if "JPY" in pair.upper() else 0.0001


def gerak(pair, awal, kini, keputusan=""):
    """Pergerakan searah sinyal: + = menguntungkan, - = merugikan.
    BUY: harga naik = +. SELL: harga turun = +. Tanpa keputusan: arah harga apa adanya."""
    tanda = -1 if keputusan == "SELL" else 1
    pip = (kini - awal) / pip_size(pair) * tanda
    pct = (kini - awal) / awal * 100 * tanda
    return pip, pct
