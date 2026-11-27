"""Semua parameter skema final. Nilai dari spesifikasi; yang bukan dari spesifikasi diberi ASUMSI."""
import json
import os
from datetime import datetime, timezone

# Sumber data: biquote (publik). ASUMSI: nama interval, endpoint kalender, dan batas candle belum diverifikasi.
BIQUOTE_HOST = "https://biquote.io"
CALENDAR_PATH = "/api/calendar"
TF, TF_SEC = "15m", 900
TF_H4, TF_H4_SEC = "4h", 14400
M15_COUNT, H4_COUNT = 700, 300          # 500 return (corr_500) + warm-up
SPREAD_TERSEDIA = False                  # biquote tidak memberi spread -> filter spread dilewati (§9.3)

# Pair. Pemicu tunggal EUR/USD. Target = semua pair yang memuat EUR atau USD, KECUALI EUR/CHF.
PEMICU = "EUR_USD"
TARGETS = ["EUR_USD", "EUR_JPY", "EUR_GBP", "EUR_CAD", "EUR_AUD", "EUR_NZD",
           "GBP_USD", "USD_JPY", "USD_CHF", "USD_CAD", "AUD_USD", "NZD_USD"]
KONFIRMASI = [p for p in TARGETS if p != PEMICU]     # pair pembanding untuk korelasi dan skor
PAIRS = list(TARGETS)                                # semua pair yang diambil datanya
# Aturan konfirmasi spesifikasi (§10): pair -> (pair pembanding, +1 aligned / -1 divergent).
TARGET_RULES = {"EUR_JPY": ("USD_JPY", 1), "EUR_GBP": ("GBP_USD", -1)}
# Pair dengan syarat korelasi bertahan (§10D): corr_adapt > CORR_PERSIST_MIN selama CORR_PERSIST_BAR bar.
CORR_PERSIST_PAIRS = ("EUR_CAD", "EUR_AUD")
CORR_PERSIST_BAR, CORR_PERSIST_MIN = 200, 0.3
# Pair di luar spesifikasi (ASUMSI, disetujui): arah = eksposur mata uang. EUR +1, USD -1, lainnya 0.
EKSPOSUR = {"EUR": 1, "USD": -1}
LIKUIDITAS = {"EUR_JPY": 1.0, "GBP_USD": 1.0, "USD_JPY": 1.0, "EUR_GBP": 0.8,
              "EUR_CAD": 0.7, "EUR_AUD": 0.6, "USD_CHF": 0.7,
              "USD_CAD": 0.7, "AUD_USD": 0.8, "NZD_USD": 0.6, "EUR_NZD": 0.6}   # nilai non-spesifikasi: ASUMSI
LIKUIDITAS_DEFAULT = 0.5

# Indikator (§4-5)
EMA_N = 50                              # EMA target (EUR/JPY) dan EMA H4
EMA_TRIGGER_CEPAT = 20                  # EMA trigger saat volatilitas tinggi
EMA_TRIGGER_LAMBAT = 50                 # EMA trigger selain itu
EMA_PCT_SWITCH = 65                     # persentil ATR > 65 -> EMA 20 (adaptif 2 bin)
STOCH_K, STOCH_SMOOTH, STOCH_D = 14, 3, 3
STOCH_OS, STOCH_OB = 20, 80
ATR_N = 14
ATR_MED_N = 100
CORR_WIN = (50, 200, 500)
CORR_BOBOT = (0.5, 0.3, 0.2)

# Lead-lag, bobot, dan skor (§6-8)
LAGS = range(-3, 4)
LEADLAG_WIN = 200                        # ASUMSI
STAB_WIN = 20
KORELASI_MIN = 0.2
SKOR_MIN_SAMPEL = 500
SKOR_Q_BUY, SKOR_Q_SELL = 0.70, 0.30
SKOR_WARMUP = 0.0
SKOR_RIWAYAT_MAKS = 20000                # ASUMSI

# Regime (§9)
ATR_PCT_WIN = 200
ATR_PCT_MIN, ATR_PCT_MAX = 30, 80
NEWS_MENIT = 30

# Eksekusi (§11)
TP_PIP = 10
SL_MIN_PIP, SL_MAX_PIP = 10, 15
SL_ATR_MULT = 1.5
RISIKO_PERSEN = 1.0
MAKS_PER_PAIR, MAKS_TOTAL = 1, 3

# Backtest (§12). Biaya memakai batas atas spesifikasi. Pair lain ASUMSI 2.0 pip.
SPREAD_PIP = {"EUR_USD": 1.5, "EUR_JPY": 2.0}
SPREAD_PIP_DEFAULT = 2.0
SLIPPAGE_PIP = 0.5
IS_FRAC, OOS_FRAC = 0.60, 0.20
WF_BAR = 96 * 90                          # jendela uji 3 bulan (96 bar M15 per hari)
DD_MAKS_PERSEN, TRADE_OOS_MIN = 20.0, 100

# Pemantauan entry (logika tidak berubah)
PANTAU_TITIK_MENIT = 15
PANTAU_TOTAL_MENIT = 60
PANTAU_TIMEOUT_MENIT = 90
PANTAU_AKTIF = "state/pemantauan_aktif.json"
PANTAU_ARSIP = "database/pemantauan.jsonl"

# Keluaran
SKOR_PATH = "state/score_history.json"
CANDLE_PATH = "state/candles.json"       # histori candle tersimpan: tiap run menambah bar baru, dipangkas ke M15_COUNT / H4_COUNT
SIGNAL_LOG = "database/signal_log.jsonl"
REPORT_MD = "reports/scanner_latest.md"
REPORT_JSON = "scanner/latest.json"


def utc_now():
    return datetime.now(timezone.utc)


def fmt(dt):
    return dt.strftime("%Y-%m-%dT%H:%M:%SZ")


def to_epoch(v):
    """Epoch detik dari angka (detik/milidetik) atau string ISO-8601."""
    s = str(v).strip()
    try:
        x = float(s)
    except ValueError:
        return int(datetime.fromisoformat(s.replace("Z", "+00:00")).timestamp())
    return int(x / 1000) if x > 1e11 else int(x)


def disp(pair):
    return pair.replace("_", "/")


def pip_size(pair):
    return 0.01 if "JPY" in pair else 0.0001


def desimal(pair):
    """Jumlah desimal harga: 3 untuk pair JPY, 5 untuk lainnya."""
    return 3 if "JPY" in pair else 5


def spread_pip(pair):
    return SPREAD_PIP.get(pair, SPREAD_PIP_DEFAULT)


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


def append_jsonl(path, records):
    if not records:
        return
    d = os.path.dirname(path)
    if d:
        os.makedirs(d, exist_ok=True)
    with open(path, "a", encoding="utf-8") as f:
        for r in records:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
