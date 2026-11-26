# Laporan Scanner Adaptive Forex

- Waktu eksekusi: 2026-11-26T00:15:25Z
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
| EUR/USD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.09702 | — | 168/180 | 2026-11-25T23:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| GBP/USD | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.31109 | — | 168/180 | 2026-11-25T23:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| USD/JPY | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 159.204 | — | 168/180 | 2026-11-25T23:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| USD/CHF | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.83125 | — | 168/180 | 2026-11-25T23:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| AUD/USD | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.66266 | — | 168/180 | 2026-11-25T23:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| USD/CAD | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.42159 | — | 168/180 | 2026-11-25T23:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| NZD/USD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.54846 | — | 168/180 | 2026-11-25T23:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| EUR/GBP | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.83673 | — | 168/180 | 2026-11-25T23:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| EUR/JPY | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 174.6525 | — | 168/180 | 2026-11-25T23:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |
| EUR/CHF | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.91192 | — | 168/180 | 2026-11-25T23:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| EUR/AUD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.65545 | — | 168/180 | 2026-11-25T23:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| EUR/CAD | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.55931 | — | 168/180 | 2026-11-25T23:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| EUR/NZD | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 2.00018 | — | 168/180 | 2026-11-25T23:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |
| XAU/USD | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 3576.5775 | — | 168/180 | 2026-11-25T23:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| XAU/AUD | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 5396.842 | — | 168/180 | 2026-11-25T23:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |

## Saran analisa cadangan (BUKAN sinyal, tidak divalidasi backtest)
Dari lead-lag, maks 3 pair: leader bergerak, follower tertinggal 5-60 menit. BUY/SELL mengikuti arah leader. SL 0.5 ATR H1, TP 1.5R. Tanpa cek spread, news, atau batas risiko §9. Tidak mengubah label.
| Pair | Arah | Dasar | Entry | SL | TP | Risiko SL |
|---|---|---|---|---|---|---|
| GBP/USD | **BUY** | LEAD-LAG: XAU/AUD memimpin 55 mnt, korelasi -0.53, n 31 | 1.31124 | 1.31048 | 1.31239 | 7.6 pip |
| NZD/USD | **SELL** | LEAD-LAG: XAU/USD memimpin 40 mnt, korelasi -0.51, n 34 | 0.54853 | 0.54895 | 0.54791 | 4.2 pip |

## Lead-lag (backtest 6 jam, BUKAN sinyal)
- Status: dianalisa
- Pair gagal diambil (M5): tidak ada
- Backtest jendela 360 menit, diperbarui 2026-11-26T00:15:25Z, pasangan lolos 13.

Pasangan lolos (10 teratas, urut |korelasi|):

| Leader | Follower | Lag (menit) | Korelasi | Korelasi lag 0 | n |
|---|---|---|---|---|---|
| XAU/AUD | AUD/CAD | 55 | 0.546 | 0.314 | 29 |
| XAU/AUD | GBP/USD | 55 | -0.534 | 0.31 | 31 |
| XAU/USD | AUD/CAD | 55 | 0.524 | 0.378 | 29 |
| XAU/AUD | EUR/AUD | 55 | -0.519 | -0.265 | 29 |
| XAU/USD | GBP/USD | 55 | -0.518 | 0.354 | 31 |
| XAU/USD | EUR/AUD | 55 | -0.514 | -0.349 | 29 |
| XAU/AUD | AUD/NZD | 40 | 0.51 | 0.162 | 32 |
| XAU/USD | AUD/NZD | 40 | 0.509 | 0.239 | 32 |
| XAU/AUD | GBP/AUD | 55 | -0.507 | -0.193 | 31 |
| XAU/USD | NZD/USD | 40 | -0.506 | 0.379 | 34 |

Kandidat (follower yang tertinggal, urut skor):

| Follower | Arah | Leader | Lag (menit) | z leader | Skor |
|---|---|---|---|---|---|
| GBP/USD | BUY | XAU/AUD | 55 | -0.01 | 0.534 |
| EUR/AUD | BUY | XAU/AUD | 55 | -0.01 | 0.519 |
| NZD/USD | SELL | XAU/USD | 40 | 0.14 | 0.506 |

## Pemantauan 15 menit (entry dan analisa cadangan)
Nilai di kolom 15m-60m = pip dari entry pada close candle M15 ke-1 sampai ke-4. Jika SL dan TP kena di candle yang sama, dihitung SL. Analisa cadangan BUKAN sinyal.
| Sumber | Pair | Arah | Entry | SL | TP | 15m | 30m | 45m | 60m | Hasil | Pip sekarang | Umur |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LEAD-LAG (analisa cadangan, bukan sinyal) | USD/JPY | BUY | 159.1425 | 159.04108 | 159.29463 | +7.5 | +6.1 | +1.0 | - | BERJALAN | PROFIT 1.0 pip | 45 mnt |
| LEAD-LAG (analisa cadangan, bukan sinyal) | EUR/USD | BUY | 1.0971 | 1.09653 | 1.09795 | -0.8 | +1.0 | - | - | BERJALAN | PROFIT 1.0 pip | 30 mnt |
| LEAD-LAG (analisa cadangan, bukan sinyal) | EUR/AUD | BUY | 1.65545 | 1.65394 | 1.6577 | +4.3 | - | - | - | BERJALAN | PROFIT 4.3 pip | 15 mnt |

## Evaluasi 1 jam (entry dan analisa cadangan)
Dibuat setelah 60 menit atau saat SL/TP kena. MFE = gerak terbaik, MAE = gerak terburuk, dalam pip.
Belum ada evaluasi yang selesai di run ini.

## Level analisa cadangan (BUKAN sinyal, tanpa statistik)
Level S/R terdekat untuk konteks scalping. Tidak mengubah label atau keputusan apa pun.
- **EUR/USD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 1.09609 (0.84 ATR, 29 bar sentuh)
  - M15: resistance 1.09752 (0.68 ATR, 22 bar sentuh) · support tidak ada dalam jarak
- **GBP/USD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 1.3094 (1.11 ATR, 28 bar sentuh)
  - M15: resistance 1.31157 (0.56 ATR, 41 bar sentuh) · support tidak ada dalam jarak
- **USD/JPY** (NO TRADE)
  - H1: resistance 159.20919 (0.03 ATR, 71 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance 159.19011 (0.46 ATR, 64 bar sentuh) · support tidak ada dalam jarak
- **USD/CHF** (NO TRADE)
  - H1: resistance 0.83234 (0.84 ATR, 4 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance 0.83159 (0.58 ATR, 11 bar sentuh) · support tidak ada dalam jarak
- **AUD/USD** (NO TRADE)
  - H1: resistance 0.66298 (0.25 ATR, 40 bar sentuh) · support 0.661 (1.31 ATR, 7 bar sentuh)
  - M15: resistance 0.66269 (0.19 ATR, 55 bar sentuh) · support tidak ada dalam jarak
- **USD/CAD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 1.41948 (1.48 ATR, 1 bar sentuh)
  - M15: resistance 1.42179 (0.27 ATR, 6 bar sentuh) · support tidak ada dalam jarak
- **NZD/USD** (NO TRADE)
  - H1: resistance 0.54865 (0.23 ATR, 35 bar sentuh) · support 0.54756 (1.08 ATR, 23 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 0.54839 (0.43 ATR, 22 bar sentuh)
- **EUR/GBP** (NO TRADE)
  - H1: resistance 0.83698 (0.41 ATR, 35 bar sentuh) · support 0.83606 (1.1 ATR, 27 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support tidak ada dalam jarak
- **EUR/JPY** (NO TRADE)
  - H1: resistance 174.70071 (0.21 ATR, 38 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance tidak ada dalam jarak · support 174.54816 (0.8 ATR, 28 bar sentuh)
- **EUR/CHF** (NO TRADE)
  - H1: resistance 0.91231 (0.36 ATR, 6 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance tidak ada dalam jarak · support 0.91198 (0.34 ATR, 18 bar sentuh)
- **EUR/AUD** (NO TRADE)
  - H1: resistance 1.65567 (0.07 ATR, 22 bar sentuh) · support 1.65267 (0.92 ATR, 21 bar sentuh)
  - M15: resistance 1.65675 (0.79 ATR, 12 bar sentuh) · support 1.65531 (0.51 ATR, 10 bar sentuh)
- **EUR/CAD** (NO TRADE)
  - H1: resistance 1.56064 (0.95 ATR, 3 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance tidak ada dalam jarak · support tidak ada dalam jarak
- **EUR/NZD** (NO TRADE)
  - H1: resistance 2.00104 (0.36 ATR, 57 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance tidak ada dalam jarak · support tidak ada dalam jarak
- **XAU/USD** (NO TRADE)
  - H1: resistance 3608.91558 (1.06 ATR, 18 bar sentuh) · support 3540.21417 (1.19 ATR, 22 bar sentuh)
  - M15: resistance 3589.041 (0.75 ATR, 7 bar sentuh) · support tidak ada dalam jarak
- **XAU/AUD** (NO TRADE)
  - H1: resistance 5416.917 (0.47 ATR, 11 bar sentuh) · support 5385.4644 (0.27 ATR, 25 bar sentuh)
  - M15: resistance 5414.32925 (0.72 ATR, 7 bar sentuh) · support tidak ada dalam jarak

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

