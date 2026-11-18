"""Konfigurasi bot screening forex (Skema SMC Scalping 30 Menit v7.0)."""
import json
import os
from datetime import datetime, timezone

# ---- Sumber data: biquote (publik, tanpa API key) ----
BIQUOTE_HOST = "https://biquote.io"
CANDLE_COUNT = 200

# ---- 14 pair. Sesuaikan dengan daftar pair Finex Anda ----
PAIRS = [
    "EUR_USD", "GBP_USD", "USD_JPY", "USD_CHF", "AUD_USD", "USD_CAD", "NZD_USD",
    "EUR_GBP", "EUR_JPY", "EUR_CHF", "EUR_AUD", "EUR_CAD", "EUR_NZD",
    "XAU_USD",
]

# Timeframe yang dipakai strategi: D1 (trend utama), H4 (konfirmasi bias),
# H1 (liquidity, OB/FVG), M5 (entry). "1d" diasumsikan didukung biquote, verifikasi saat uji.
TF_GRAN = {"5m": "5m", "1h": "1h", "4h": "4h", "1d": "1d"}

# ---- Struktur pasar & likuiditas ----
SWING_LB = 2          # jumlah candle kiri/kanan untuk swing high/low (pivot)
SWEEP_BARS = 8        # sweep harus terjadi dalam N candle H1 terakhir
ZONE_BARS = 48        # OB/FVG H1 yang dipakai dibatasi N candle terakhir (~2 hari)

# ---- Entry M5 ----
RETEST_BARS = 12      # harga harus menyentuh zona dalam N candle M5 terakhir (~1 jam)
SL_BUFFER_PIPS = 7    # SL di luar zona (strategi: +/- 5-10 pip)
MAX_RISK_PIPS = 30    # jika jarak SL lebih dari ini, setup dibatalkan
RR = 2                # target profit = RR x risiko (RR 1:2)

# ---- Pemantauan & waktu ----
MONITOR_MINUTES = 60  # lama pemantauan pair (menit)
COOLDOWN_MINUTES = 60  # sejak sinyal pertama: sinyal searah di pair yang sama tidak masuk hasil screening (sama dengan lama pemantauan)
LATE_MINUTES = 5

# ---- Database ----
RETENSI_HARI = 30
MIN_RETENSI_HARI = 7

# ---- Path ----
DB_PATH = "database/signal_history.json"
MONITOR_PATH = "state/monitoring_state.json"
COOLDOWN_PATH = "state/cooldown_state.json"
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
    """Ukuran 1 pip: XAU = 0.1, pair JPY = 0.01, selain itu = 0.0001."""
    p = pair.upper()
    if p.startswith("XAU"):
        return 0.1
    return 0.01 if "JPY" in p else 0.0001


def gerak(pair, awal, kini, keputusan=""):
    """Pergerakan searah sinyal: + = menguntungkan, - = merugikan.
    BUY: harga naik = +. SELL: harga turun = +. Tanpa keputusan: arah harga apa adanya."""
    tanda = -1 if keputusan == "SELL" else 1
    pip = (kini - awal) / pip_size(pair) * tanda
    pct = (kini - awal) / awal * 100 * tanda
    return pip, pct
