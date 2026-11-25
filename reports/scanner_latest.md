# Laporan Scanner Adaptive Forex

- Waktu eksekusi: 2026-11-25T20:00:49Z
- Status run: OK, 15 pair dianalisa, 0 data tidak valid
- Ringkasan: ENTRY 0, WATCHLIST 0, NO TRADE 15, DATA INVALID 0
- Timeframe sinyal: 1h (H1), bias 4h
- Ranking: KOSONG (belum ada backtest). Semua pair jadi NO TRADE.
- Kalender: gagal diperiksa (AttributeError), tidak ada ENTRY
- Spread: BELUM terverifikasi (OANDA belum tersambung), jadi tidak ada ENTRY.
- Manajemen risiko §9: BELUM diimplementasi (tidak ada batas 3 trade/pair/hari atau korelasi).
- Celah waktu (gap): H1 di 15 pair, H4 di 15 pair. Biasanya akhir pekan atau libur, diabaikan.

| Pair | Regime | Bias H4 | Label | Status | Mode | Arah | Kekuatan sel (backtest) | Harga (mid) | Entry / SL / TP | Bar H1/H4 | Bar terakhir (UTC) | Catatan |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| EUR/USD | VOLATIL/CHOPPY | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.09792 | — | 168/180 | 2026-11-25T19:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime VOLATIL/CHOPPY belum punya metode prioritas di ranking |
| GBP/USD | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.31217 | — | 168/180 | 2026-11-25T19:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| USD/JPY | VOLATIL/CHOPPY | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 159.2025 | — | 168/180 | 2026-11-25T19:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime VOLATIL/CHOPPY belum punya metode prioritas di ranking |
| USD/CHF | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.83083 | — | 168/180 | 2026-11-25T19:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| AUD/USD | MIXED | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.6627 | — | 168/180 | 2026-11-25T19:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime MIXED belum punya metode prioritas di ranking |
| USD/CAD | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.42046 | — | 168/180 | 2026-11-25T19:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| NZD/USD | VOLATIL/CHOPPY | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.54886 | — | 168/180 | 2026-11-25T19:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime VOLATIL/CHOPPY belum punya metode prioritas di ranking |
| EUR/GBP | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.83673 | — | 168/180 | 2026-11-25T19:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| EUR/JPY | VOLATIL/CHOPPY | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 174.7915 | — | 168/180 | 2026-11-25T19:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime VOLATIL/CHOPPY belum punya metode prioritas di ranking |
| EUR/CHF | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.91222 | — | 168/180 | 2026-11-25T19:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| EUR/AUD | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.65671 | — | 168/180 | 2026-11-25T19:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| EUR/CAD | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.55959 | — | 168/180 | 2026-11-25T19:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| EUR/NZD | VOLATIL/CHOPPY | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 2.00065 | — | 168/180 | 2026-11-25T19:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime VOLATIL/CHOPPY belum punya metode prioritas di ranking |
| XAU/USD | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 3546.4885 | — | 168/180 | 2026-11-25T19:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| XAU/AUD | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 5351.304 | — | 168/180 | 2026-11-25T19:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |

## Saran analisa cadangan (BUKAN sinyal, tidak divalidasi backtest)
Dari lead-lag, maks 3 pair: leader bergerak, follower tertinggal 5-60 menit. BUY/SELL mengikuti arah leader. SL 0.5 ATR H1, TP 1.5R. Tanpa cek spread, news, atau batas risiko §9. Tidak mengubah label.
Tidak ada saran (tidak ada level H1 dalam jarak 1.0 ATR, dan tidak ada kandidat lead-lag).

## Lead-lag (backtest 6 jam, BUKAN sinyal)
- Status: dianalisa
- Pair gagal diambil (M5): tidak ada
- Backtest jendela 360 menit, diperbarui 2026-11-25T20:00:49Z, pasangan lolos 0.

Tidak ada pasangan yang lolos ambang.

Tidak ada kandidat di run ini.

## Pemantauan 15 menit (entry dan analisa cadangan)
Nilai di kolom 15m-60m = pip dari entry pada close candle M15 ke-1 sampai ke-4. Jika SL dan TP kena di candle yang sama, dihitung SL. Analisa cadangan BUKAN sinyal.
Tidak ada entry atau saran yang sedang dipantau.

## Evaluasi 1 jam (entry dan analisa cadangan)
Dibuat setelah 60 menit atau saat SL/TP kena. MFE = gerak terbaik, MAE = gerak terburuk, dalam pip.
Belum ada evaluasi yang selesai di run ini.

## Level analisa cadangan (BUKAN sinyal, tanpa statistik)
Level S/R terdekat untuk konteks scalping. Tidak mengubah label atau keputusan apa pun.
- **EUR/USD** (NO TRADE)
  - H1: resistance 1.09901 (0.82 ATR, 32 bar sentuh) · support 1.09609 (1.38 ATR, 33 bar sentuh)
  - M15: resistance 1.09803 (0.12 ATR, 4 bar sentuh) · support 1.09748 (0.47 ATR, 10 bar sentuh)
- **GBP/USD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support tidak ada dalam jarak
  - M15: resistance tidak ada dalam jarak · support tidak ada dalam jarak
- **USD/JPY** (NO TRADE)
  - H1: resistance 159.22111 (0.08 ATR, 73 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance tidak ada dalam jarak · support 159.19444 (0.05 ATR, 68 bar sentuh)
- **USD/CHF** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 0.82852 (1.46 ATR, 2 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 0.83076 (0.07 ATR, 11 bar sentuh)
- **AUD/USD** (NO TRADE)
  - H1: resistance 0.66443 (1.09 ATR, 29 bar sentuh) · support 0.661 (1.07 ATR, 8 bar sentuh)
  - M15: resistance 0.66322 (0.51 ATR, 45 bar sentuh) · support tidak ada dalam jarak
- **USD/CAD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support tidak ada dalam jarak
  - M15: resistance tidak ada dalam jarak · support tidak ada dalam jarak
- **NZD/USD** (NO TRADE)
  - H1: resistance 0.54932 (0.45 ATR, 60 bar sentuh) · support 0.54756 (1.28 ATR, 23 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 0.5485 (0.54 ATR, 23 bar sentuh)
- **EUR/GBP** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 0.83611 (0.84 ATR, 30 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 0.8365 (0.45 ATR, 56 bar sentuh)
- **EUR/JPY** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 174.69318 (0.37 ATR, 37 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support tidak ada dalam jarak
- **EUR/CHF** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support tidak ada dalam jarak
  - M15: resistance 0.91304 (0.86 ATR, 11 bar sentuh) · support tidak ada dalam jarak
- **EUR/AUD** (NO TRADE)
  - H1: resistance 1.65908 (0.65 ATR, 5 bar sentuh) · support 1.65579 (0.25 ATR, 19 bar sentuh)
  - M15: resistance 1.65743 (0.3 ATR, 8 bar sentuh) · support 1.65528 (0.6 ATR, 8 bar sentuh)
- **EUR/CAD** (NO TRADE)
  - H1: resistance 1.5612 (0.99 ATR, 3 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance 1.56019 (0.54 ATR, 3 bar sentuh) · support 1.55906 (0.48 ATR, 11 bar sentuh)
- **EUR/NZD** (NO TRADE)
  - H1: resistance 2.0011 (0.16 ATR, 60 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance tidak ada dalam jarak · support tidak ada dalam jarak
- **XAU/USD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 3540.21417 (0.2 ATR, 21 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 3545.72055 (0.04 ATR, 27 bar sentuh)
- **XAU/AUD** (NO TRADE)
  - H1: resistance 5385.4644 (0.8 ATR, 22 bar sentuh) · support 5310.43358 (0.96 ATR, 16 bar sentuh)
  - M15: resistance 5367.32342 (0.59 ATR, 43 bar sentuh) · support tidak ada dalam jarak

## Keterangan
- **ENTRY LONG/SHORT**: semua syarat terpenuhi. Entry, SL, dan TP boleh dipakai.
- **WATCHLIST**: metode ada, tetapi BELUM boleh entry. Lihat kolom Status. Tidak ada harga rencana.
  - *Menunggu trigger*: belum ada sinyal dari metode prioritas.
  - *Trigger ada - ditahan*: sinyal sudah muncul, tetapi dihentikan oleh news, kalender, atau spread.
- **NO TRADE**: regime ini belum punya metode prioritas di ranking. Bukan sinyal jual atau beli.
- **DATA INVALID**: candle gagal diambil atau tidak lolos validasi.
- **Mode**: metode entry (FISHER, EMA_TREND, MACD, STOCH_MR, BB_SQUEEZE).
- **Kekuatan sel**: hasil backtest untuk pair + regime + mode + arah ini. ★ = bintang 1 sampai 5 (skor 0-100). n = jumlah trade, PF = profit factor, Exp = rata-rata R per trade, DD = penurunan terbesar dalam R, fold = fold yang untung dari 4, WR = win rate.
- **Harga (mid)**: close candle 1h terakhir yang sudah tutup, rata-rata bid dan ask. Bukan harga live.
- **Bar H1/H4**: jumlah candle 1h dan H4 yang diterima dari biquote. EMA200 H4 butuh minimal 200 bar.
- **Analisa cadangan**: level dari M15 (±1.0 ATR) dan H1 (±1.5 ATR). Sentuhan = jumlah bar yang menyentuh area level.
- **Saran analisa cadangan**: BUKAN sinyal dan BUKAN ENTRY. Hanya kedekatan harga ke level H1, tanpa backtest atau statistik. Pakai hanya sebagai bahan pertimbangan sendiri.

