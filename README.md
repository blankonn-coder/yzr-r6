# Skema Final: EUR/USD sebagai Pemantik dengan Konfirmasi Multi-Pair

Scanner polling 15 menit. Satu siklus per bar M15 yang sudah tutup. Data dari biquote.

## Struktur repo
```
config.py              parameter skema, path, dan fungsi bantu
engine.py              indikator, persiapan data, trigger, korelasi, filter, target, keputusan
pantauan.py            pemantauan entry (titik 15/30/45/60 menit, evaluasi 1 jam)
main.py                scanner live: data biquote, validasi, analisa, laporan, Discord
backtest.py            backtest §12 (memakai engine yang sama dengan live)
tests/test_all.py      seluruh tes (python -m pytest tests/)
requirements.txt       requests, pytest
.gitignore
.github/workflows/forex_scalper.yml
```
Folder `state/`, `database/`, `reports/`, dan `scanner/` dibuat dan di-commit oleh bot saat run.

## Alur per siklus (`main.py`)
1. Perbarui pemantauan entry yang masih berjalan.
2. Ambil candle M15 (5 pair) dan H4 (EUR/USD) dari biquote, validasi, lalu sejajarkan timestamp.
3. Analisa bar terakhir yang tutup (`engine.analyze`):
   - **Trigger** EUR/USD: close vs EMA50, stochastic cross dari zona 20/80, ATR di atas median 100 bar.
   - **Bobot adaptif**: korelasi rolling 50/200/500 bar, dikombinasikan dan dinormalisasi.
   - **Skor konfirmasi** dibandingkan dengan quantile 70/30 dari riwayat skor.
   - **Filter**: persentil ATR 30–80, tren H4, kalender ±30 menit, dan korelasi rata-rata ≥ 0,2.
   - **Target EUR/JPY**: USD/JPY tidak berlawanan arah trigger, dan EUR/JPY di sisi EMA50 yang sesuai.
4. Jika semua lulus: entry = close M15 EUR/JPY, SL = clamp(1,5 × ATR, 10–15 pip), TP = 10 pip.
5. Catat ke `database/signal_log.jsonl`, `reports/scanner_latest.md`, `scanner/latest.json`, dan Discord.

Label: `ENTRY LONG/SHORT`, `NO TRADE` (trigger ada, alasan dicatat), `NO SIGNAL`, `DATA INVALID`.

## Performa
- Korelasi memakai prefix sum, sehingga setiap jendela O(1). Tidak ada loop ulang per bar.
- Analisa penuh hanya dijalankan saat trigger aktif. Pemeriksaan murah dilakukan dulu.
- Keputusan, skor, level entry, dan trade identik dengan versi berstruktur lebih rumit, diuji bar demi bar pada 3 dataset sintetis (33.837 bar, 338 bar trigger, 16 entry).

## Backtest
```
BACKTEST_CACHE_DIR=/path/cache python backtest.py
```
Cache berisi `{PAIR}_M15.csv` (kolom `time, open, high, low, close`) untuk semua pair. Hasil: `reports/backtest.md`.
- Biaya: spread (EUR/USD 1,5 pip, EUR/JPY 2,0 pip, selain itu 2,0) + slippage 0,5 pip.
- Berita tidak bisa diuji, sehingga hasil cenderung optimistis.
- Tidak ada parameter yang dioptimasi.

## Keputusan dan asumsi (perlu dikonfirmasi)
- **Sumber data biquote**, bukan OANDA. Nama interval `15m`, endpoint kalender, dan batas candle (`M15_COUNT = 700`) belum diverifikasi.
- **Pair konfirmasi** mengikuti pseudocode §13. **Target** EUR/JPY. EUR/GBP tersedia lewat `TARGET_RULES` jika ingin diganti.
- **Rumus skor** tidak mengalikan dengan arah trigger. Dengan rumus spesifikasi, aturan BUY ≥ q70 dan SELL ≤ q30 saling bertentangan.
- **Stochastic "cross dari bawah 20"** dibaca sebagai %K bar sebelumnya < 20 saat cross.
- **Filter korelasi** menghentikan entry seperti filter lain. Spesifikasi juga menyebut "turunkan ke single-pair trigger", yang tidak diimplementasikan.
- **Lead-lag** hanya dicatat sebagai informasi, sesuai pseudocode.
- **Spread** tidak tersedia, sehingga filter spread dilewati.
- **Batas posisi** memakai catatan pemantauan (maks 60 menit), bukan posisi nyata di broker.

## Konfigurasi GitHub
- Secret `DISCORD_WEBHOOK_URL`, variable `DISCORD_NOTIFY_MODE` (`signal` | `always` | `off`).
- Jadwal cron-job.org dikirim ke `repository_dispatch` tiap 15 menit.
