# Laporan Scanner Adaptive Forex

- Waktu eksekusi: 2026-11-25T02:30:28Z
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
| EUR/USD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.09584 | — | 168/180 | 2026-11-25T01:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| GBP/USD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.31068 | — | 168/180 | 2026-11-25T01:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| USD/JPY | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 159.2705 | — | 168/180 | 2026-11-25T01:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |
| USD/CHF | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.83591 | — | 168/180 | 2026-11-25T01:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| AUD/USD | VOLATIL/CHOPPY | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.66366 | — | 168/180 | 2026-11-25T01:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime VOLATIL/CHOPPY belum punya metode prioritas di ranking |
| USD/CAD | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.42694 | — | 168/180 | 2026-11-25T01:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| NZD/USD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.54736 | — | 168/180 | 2026-11-25T01:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| EUR/GBP | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.83608 | — | 168/180 | 2026-11-25T01:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| EUR/JPY | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 174.5305 | — | 168/180 | 2026-11-25T01:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| EUR/CHF | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.91602 | — | 168/180 | 2026-11-25T01:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| EUR/AUD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.65121 | — | 168/180 | 2026-11-25T01:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| EUR/CAD | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.56368 | — | 168/180 | 2026-11-25T01:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| EUR/NZD | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 2.00197 | — | 168/180 | 2026-11-25T01:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |
| XAU/USD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 3546.5435 | — | 168/180 | 2026-11-25T01:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| XAU/AUD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 5343.926 | — | 168/180 | 2026-11-25T01:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |

## Saran analisa cadangan (BUKAN sinyal, tidak divalidasi backtest)
Dari lead-lag, maks 3 pair: leader bergerak, follower tertinggal 5-60 menit. BUY/SELL mengikuti arah leader. SL 0.5 ATR H1, TP 1.5R. Tanpa cek spread, news, atau batas risiko §9. Tidak mengubah label.
| Pair | Arah | Dasar | Entry | SL | TP | Risiko SL |
|---|---|---|---|---|---|---|
| EUR/GBP | **SELL** | LEAD-LAG: CAD/JPY memimpin 35 mnt, korelasi -0.51, n 62 | 0.83615 | 0.83637 | 0.83583 | 2.1 pip |

## Lead-lag (backtest 6 jam, BUKAN sinyal)
- Status: dianalisa
- Pair gagal diambil (M5): tidak ada
- Backtest jendela 360 menit, diperbarui 2026-11-25T02:30:28Z, pasangan lolos 1.

Pasangan lolos (10 teratas, urut |korelasi|):

| Leader | Follower | Lag (menit) | Korelasi | Korelasi lag 0 | n |
|---|---|---|---|---|---|
| CAD/JPY | EUR/GBP | 35 | -0.512 | 0.034 | 62 |

Kandidat (follower yang tertinggal, urut skor):

| Follower | Arah | Leader | Lag (menit) | z leader | Skor |
|---|---|---|---|---|---|
| EUR/GBP | SELL | CAD/JPY | 35 | 0.87 | 0.512 |

## Pemantauan 15 menit (entry dan analisa cadangan)
Nilai di kolom 15m-60m = pip dari entry pada close candle M15 ke-1 sampai ke-4. Jika SL dan TP kena di candle yang sama, dihitung SL. Analisa cadangan BUKAN sinyal.
| Sumber | Pair | Arah | Entry | SL | TP | 15m | 30m | 45m | 60m | Hasil | Pip sekarang | Umur |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LEAD-LAG (analisa cadangan, bukan sinyal) | EUR/JPY | SELL | 174.5325 | 174.63016 | 174.38601 | -3.7 | +0.2 | -5.3 | - | SL kena | LOSS 9.8 pip | 60 mnt |

## Evaluasi 1 jam (entry dan analisa cadangan)
Dibuat setelah 60 menit atau saat SL/TP kena. MFE = gerak terbaik, MAE = gerak terburuk, dalam pip.
| Sumber | Pair | Arah | 15m | 30m | 45m | 60m | Hasil | Pip akhir | MFE (pip) | MAE (pip) | Ditutup (UTC) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| LEAD-LAG (analisa cadangan, bukan sinyal) | EUR/JPY | SELL | -3.7 | +0.2 | -5.3 | - | SL kena · menit 60 | LOSS 9.8 pip | 4.8 | -10.1 | 2026-11-25T02:30:28Z |

## Level analisa cadangan (BUKAN sinyal, tanpa statistik)
Level S/R terdekat untuk konteks scalping. Tidak mengubah label atau keputusan apa pun.
- **EUR/USD** (NO TRADE)
  - H1: resistance 1.09594 (0.1 ATR, 19 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance tidak ada dalam jarak · support 1.09615 (0.38 ATR, 28 bar sentuh)
- **GBP/USD** (NO TRADE)
  - H1: resistance 1.31116 (0.43 ATR, 32 bar sentuh) · support 1.31042 (0.23 ATR, 29 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 1.31092 (0.42 ATR, 29 bar sentuh)
- **USD/JPY** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 159.25153 (0.12 ATR, 61 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 159.25877 (0.13 ATR, 58 bar sentuh)
- **USD/CHF** (NO TRADE)
  - H1: resistance 0.83669 (0.82 ATR, 3 bar sentuh) · support 0.835 (0.95 ATR, 5 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 0.83533 (0.54 ATR, 23 bar sentuh)
- **AUD/USD** (NO TRADE)
  - H1: resistance 0.66545 (1.39 ATR, 21 bar sentuh) · support 0.66295 (0.55 ATR, 32 bar sentuh)
  - M15: resistance 0.66334 (0.27 ATR, 49 bar sentuh) · support tidak ada dalam jarak
- **USD/CAD** (NO TRADE)
  - H1: resistance 1.42709 (0.13 ATR, 12 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance 1.42668 (0.77 ATR, 17 bar sentuh) · support 1.4263 (0.02 ATR, 4 bar sentuh)
- **NZD/USD** (NO TRADE)
  - H1: resistance 0.54756 (0.28 ATR, 21 bar sentuh) · support 0.54628 (1.49 ATR, 6 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support tidak ada dalam jarak
- **EUR/GBP** (NO TRADE)
  - H1: resistance 0.83626 (0.43 ATR, 28 bar sentuh) · support 0.83592 (0.35 ATR, 13 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support tidak ada dalam jarak
- **EUR/JPY** (NO TRADE)
  - H1: resistance 174.7524 (1.16 ATR, 33 bar sentuh) · support 174.51236 (0.1 ATR, 26 bar sentuh)
  - M15: resistance 174.66183 (0.68 ATR, 22 bar sentuh) · support tidak ada dalam jarak
- **EUR/CHF** (NO TRADE)
  - H1: resistance 0.91665 (0.8 ATR, 5 bar sentuh) · support 0.91569 (0.41 ATR, 4 bar sentuh)
  - M15: resistance 0.91607 (0.18 ATR, 23 bar sentuh) · support 0.91581 (0.7 ATR, 10 bar sentuh)
- **EUR/AUD** (NO TRADE)
  - H1: resistance 1.65267 (0.49 ATR, 20 bar sentuh) · support 1.64955 (0.56 ATR, 20 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 1.65258 (0.36 ATR, 29 bar sentuh)
- **EUR/CAD** (NO TRADE)
  - H1: resistance 1.56437 (0.5 ATR, 8 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance tidak ada dalam jarak · support 1.56324 (0.94 ATR, 2 bar sentuh)
- **EUR/NZD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 2.00084 (0.53 ATR, 53 bar sentuh)
  - M15: resistance 2.00168 (0.2 ATR, 56 bar sentuh) · support tidak ada dalam jarak
- **XAU/USD** (NO TRADE)
  - H1: resistance 3546.6735 (0.01 ATR, 14 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance 3575.37625 (0.88 ATR, 8 bar sentuh) · support 3562.3043 (0.27 ATR, 19 bar sentuh)
- **XAU/AUD** (NO TRADE)
  - H1: resistance 5377.10775 (1.23 ATR, 16 bar sentuh) · support 5341.0465 (0.11 ATR, 17 bar sentuh)
  - M15: resistance 5389.20275 (0.78 ATR, 9 bar sentuh) · support 5369.07988 (0.48 ATR, 13 bar sentuh)

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

