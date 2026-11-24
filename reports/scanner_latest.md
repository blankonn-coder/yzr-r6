# Laporan Scanner Adaptive Forex

- Waktu eksekusi: 2026-11-24T19:45:23Z
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
| EUR/USD | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.09655 | — | 168/180 | 2026-11-24T18:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| GBP/USD | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.31146 | — | 168/180 | 2026-11-24T18:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| USD/JPY | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 159.2865 | — | 168/180 | 2026-11-24T18:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |
| USD/CHF | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.83551 | — | 168/180 | 2026-11-24T18:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| AUD/USD | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.66416 | — | 168/180 | 2026-11-24T18:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |
| USD/CAD | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.42727 | — | 168/180 | 2026-11-24T18:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| NZD/USD | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.54831 | — | 168/180 | 2026-11-24T18:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| EUR/GBP | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.83613 | — | 168/180 | 2026-11-24T18:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |
| EUR/JPY | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 174.6665 | — | 168/180 | 2026-11-24T18:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| EUR/CHF | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.91616 | — | 168/180 | 2026-11-24T18:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| EUR/AUD | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.65099 | — | 168/180 | 2026-11-24T18:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| EUR/CAD | MIXED | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.56493 | — | 168/180 | 2026-11-24T18:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime MIXED belum punya metode prioritas di ranking |
| EUR/NZD | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.99985 | — | 168/180 | 2026-11-24T18:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |
| XAU/USD | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 3555.1005 | — | 168/180 | 2026-11-24T18:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |
| XAU/AUD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 5352.613 | — | 168/180 | 2026-11-24T18:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |

## Saran analisa cadangan (BUKAN sinyal, tidak divalidasi backtest)
Dari lead-lag, maks 3 pair: leader bergerak, follower tertinggal 5-60 menit. BUY/SELL mengikuti arah leader. SL 0.5 ATR H1, TP 1.5R. Tanpa cek spread, news, atau batas risiko §9. Tidak mengubah label.
Tidak ada saran (tidak ada level H1 dalam jarak 1.0 ATR, dan tidak ada kandidat lead-lag).

## Lead-lag (backtest 6 jam, BUKAN sinyal)
- Status: dianalisa
- Pair gagal diambil (M5): tidak ada
- Backtest jendela 360 menit, diperbarui 2026-11-24T19:45:23Z, pasangan lolos 1.

Pasangan lolos (10 teratas, urut |korelasi|):

| Leader | Follower | Lag (menit) | Korelasi | Korelasi lag 0 | n |
|---|---|---|---|---|---|
| CHF/JPY | NZD/CHF | 5 | 0.506 | -0.452 | 70 |

Tidak ada kandidat di run ini.

## Pemantauan 15 menit (entry dan analisa cadangan)
Nilai di kolom 15m-60m = pip dari entry pada close candle M15 ke-1 sampai ke-4. Jika SL dan TP kena di candle yang sama, dihitung SL. Analisa cadangan BUKAN sinyal.
| Sumber | Pair | Arah | Entry | SL | TP | 15m | 30m | 45m | 60m | Hasil | Pip sekarang | Umur |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ANALISA CADANGAN (bukan sinyal) | USD/JPY | BUY | 159.2865 | 159.16528 | 159.46834 | -2.4 | -2.6 | -5.4 | - | BERJALAN | LOSS 5.4 pip | 45 mnt |
| ANALISA CADANGAN (bukan sinyal) | EUR/GBP | BUY | 0.83613 | 0.83575 | 0.8367 | -0.9 | -0.7 | -0.9 | - | BERJALAN | LOSS 0.9 pip | 45 mnt |
| ANALISA CADANGAN (bukan sinyal) | USD/CAD | BUY | 1.42727 | 1.42609 | 1.42904 | -6.6 | -1.6 | -3.6 | - | BERJALAN | LOSS 3.6 pip | 45 mnt |
| ANALISA CADANGAN (bukan sinyal) | EUR/CAD | BUY | 1.56493 | 1.56349 | 1.56708 | -4.0 | -0.9 | -2.8 | - | BERJALAN | LOSS 2.8 pip | 30 mnt |
| ANALISA CADANGAN (bukan sinyal) | EUR/NZD | BUY | 1.99985 | 1.99769 | 2.00309 | -6.3 | -3.9 | -2.8 | - | BERJALAN | LOSS 2.8 pip | 30 mnt |
| ANALISA CADANGAN (bukan sinyal) | EUR/USD | BUY | 1.09655 | 1.09535 | 1.09835 | +2.3 | +0.4 | +0.9 | - | BERJALAN | PROFIT 0.9 pip | 30 mnt |
| ANALISA CADANGAN (bukan sinyal) | EUR/AUD | BUY | 1.65099 | 1.64803 | 1.65543 | -3.9 | -2.6 | -0.7 | - | BERJALAN | LOSS 0.7 pip | 15 mnt |
| ANALISA CADANGAN (bukan sinyal) | EUR/CHF | BUY | 0.91616 | 0.91504 | 0.91784 | -0.6 | +0.5 | +0.1 | - | BERJALAN | PROFIT 0.1 pip | 15 mnt |
| ANALISA CADANGAN (bukan sinyal) | EUR/JPY | BUY | 174.6665 | 174.38202 | 175.09321 | +0.9 | -2.2 | -4.9 | - | BERJALAN | LOSS 4.9 pip | 15 mnt |

## Evaluasi 1 jam (entry dan analisa cadangan)
Dibuat setelah 60 menit atau saat SL/TP kena. MFE = gerak terbaik, MAE = gerak terburuk, dalam pip.
Belum ada evaluasi yang selesai di run ini.

## Level analisa cadangan (BUKAN sinyal, tanpa statistik)
Level S/R terdekat untuk konteks scalping. Tidak mengubah label atau keputusan apa pun.
- **EUR/USD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 1.09599 (0.44 ATR, 22 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 1.09632 (0.53 ATR, 26 bar sentuh)
- **GBP/USD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 1.31042 (0.72 ATR, 30 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 1.31159 (0.13 ATR, 25 bar sentuh)
- **USD/JPY** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 159.25986 (0.14 ATR, 59 bar sentuh)
  - M15: resistance 159.25619 (0.29 ATR, 38 bar sentuh) · support tidak ada dalam jarak
- **USD/CHF** (NO TRADE)
  - H1: resistance 0.83669 (0.98 ATR, 3 bar sentuh) · support 0.8344 (0.9 ATR, 1 bar sentuh)
  - M15: resistance 0.83591 (0.73 ATR, 9 bar sentuh) · support 0.8354 (0.12 ATR, 18 bar sentuh)
- **AUD/USD** (NO TRADE)
  - H1: resistance 0.66553 (1.09 ATR, 21 bar sentuh) · support 0.66284 (1.06 ATR, 29 bar sentuh)
  - M15: resistance 0.66449 (0.46 ATR, 39 bar sentuh) · support tidak ada dalam jarak
- **USD/CAD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 1.42685 (0.27 ATR, 9 bar sentuh)
  - M15: resistance 1.42753 (0.72 ATR, 5 bar sentuh) · support 1.4266 (0.34 ATR, 4 bar sentuh)
- **NZD/USD** (NO TRADE)
  - H1: resistance 0.54933 (1.17 ATR, 55 bar sentuh) · support 0.54756 (0.86 ATR, 18 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support tidak ada dalam jarak
- **EUR/GBP** (NO TRADE)
  - H1: resistance 0.83661 (0.93 ATR, 33 bar sentuh) · support 0.83601 (0.24 ATR, 13 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support tidak ada dalam jarak
- **EUR/JPY** (NO TRADE)
  - H1: resistance 174.903 (0.96 ATR, 33 bar sentuh) · support 174.505 (0.66 ATR, 25 bar sentuh)
  - M15: resistance 174.6385 (0.21 ATR, 22 bar sentuh) · support tidak ada dalam jarak
- **EUR/CHF** (NO TRADE)
  - H1: resistance 0.91743 (1.22 ATR, 11 bar sentuh) · support 0.91556 (0.58 ATR, 1 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support tidak ada dalam jarak
- **EUR/AUD** (NO TRADE)
  - H1: resistance 1.65267 (0.59 ATR, 18 bar sentuh) · support 1.64946 (0.53 ATR, 18 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 1.65034 (0.47 ATR, 21 bar sentuh)
- **EUR/CAD** (NO TRADE)
  - H1: resistance 1.56742 (1.39 ATR, 12 bar sentuh) · support 1.56439 (0.3 ATR, 3 bar sentuh)
  - M15: resistance 1.56544 (0.87 ATR, 22 bar sentuh) · support 1.56439 (0.28 ATR, 8 bar sentuh)
- **EUR/NZD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 1.99896 (0.35 ATR, 50 bar sentuh)
  - M15: resistance 1.99998 (0.37 ATR, 20 bar sentuh) · support 1.99899 (0.51 ATR, 12 bar sentuh)
- **XAU/USD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support tidak ada dalam jarak
  - M15: resistance 3559.9175 (0.09 ATR, 11 bar sentuh) · support 3552.7495 (0.65 ATR, 3 bar sentuh)
- **XAU/AUD** (NO TRADE)
  - H1: resistance 5377.382 (0.89 ATR, 14 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance tidak ada dalam jarak · support 5348.606 (0.76 ATR, 4 bar sentuh)

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

