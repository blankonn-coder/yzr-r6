# Laporan Scanner Adaptive Forex

- Waktu eksekusi: 2026-11-26T20:45:23Z
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
| EUR/USD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.09721 | — | 168/180 | 2026-11-26T19:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| GBP/USD | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.31085 | — | 168/180 | 2026-11-26T19:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |
| USD/JPY | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 159.2695 | — | 168/180 | 2026-11-26T19:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| USD/CHF | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.83413 | — | 168/180 | 2026-11-26T19:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| AUD/USD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.66336 | — | 168/180 | 2026-11-26T19:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| USD/CAD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.42464 | — | 168/180 | 2026-11-26T19:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| NZD/USD | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.54714 | — | 168/180 | 2026-11-26T19:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |
| EUR/GBP | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.83703 | — | 168/180 | 2026-11-26T19:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| EUR/JPY | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 174.7455 | — | 168/180 | 2026-11-26T19:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |
| EUR/CHF | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.91519 | — | 168/180 | 2026-11-26T19:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| EUR/AUD | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.65403 | — | 168/180 | 2026-11-26T19:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |
| EUR/CAD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.56291 | — | 168/180 | 2026-11-26T19:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| EUR/NZD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 2.00541 | — | 168/180 | 2026-11-26T19:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| XAU/USD | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 3568.3995 | — | 168/180 | 2026-11-26T18:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |
| XAU/AUD | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 5380.9635 | — | 168/180 | 2026-11-26T18:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |

## Saran analisa cadangan (BUKAN sinyal, tidak divalidasi backtest)
Dari lead-lag, maks 3 pair: leader bergerak, follower tertinggal 5-60 menit. BUY/SELL mengikuti arah leader. SL 0.5 ATR H1, TP 1.5R. Tanpa cek spread, news, atau batas risiko §9. Tidak mengubah label.
Tidak ada saran (tidak ada level H1 dalam jarak 1.0 ATR, dan tidak ada kandidat lead-lag).

## Lead-lag (backtest 6 jam, BUKAN sinyal)
- Status: dianalisa
- Pair gagal diambil (M5): tidak ada
- Backtest jendela 360 menit, diperbarui 2026-11-26T20:45:23Z, pasangan lolos 1.

Pasangan lolos (10 teratas, urut |korelasi|):

| Leader | Follower | Lag (menit) | Korelasi | Korelasi lag 0 | n |
|---|---|---|---|---|---|
| EUR/CHF | GBP/JPY | 30 | 0.546 | 0.009 | 65 |

Tidak ada kandidat di run ini.

## Pemantauan 15 menit (entry dan analisa cadangan)
Nilai di kolom 15m-60m = pip dari entry pada close candle M15 ke-1 sampai ke-4. Jika SL dan TP kena di candle yang sama, dihitung SL. Analisa cadangan BUKAN sinyal.
| Sumber | Pair | Arah | Entry | SL | TP | 15m | 30m | 45m | 60m | Hasil | Pip sekarang | Umur |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LEAD-LAG (analisa cadangan, bukan sinyal) | GBP/USD | BUY | 1.31085 | 1.31025 | 1.31174 | -1.2 | -0.3 | -0.5 | - | BERJALAN | LOSS 0.5 pip | 45 mnt |

## Evaluasi 1 jam (entry dan analisa cadangan)
Dibuat setelah 60 menit atau saat SL/TP kena. MFE = gerak terbaik, MAE = gerak terburuk, dalam pip.
Belum ada evaluasi yang selesai di run ini.

## Level analisa cadangan (BUKAN sinyal, tanpa statistik)
Level S/R terdekat untuk konteks scalping. Tidak mengubah label atau keputusan apa pun.
- **EUR/USD** (NO TRADE)
  - H1: resistance 1.09824 (1.14 ATR, 34 bar sentuh) · support 1.09611 (1.22 ATR, 32 bar sentuh)
  - M15: resistance 1.09733 (0.95 ATR, 33 bar sentuh) · support tidak ada dalam jarak
- **GBP/USD** (NO TRADE)
  - H1: resistance 1.31215 (1.1 ATR, 24 bar sentuh) · support 1.31042 (0.36 ATR, 50 bar sentuh)
  - M15: resistance 1.31094 (0.37 ATR, 45 bar sentuh) · support 1.31047 (0.91 ATR, 39 bar sentuh)
- **USD/JPY** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 159.15019 (1.09 ATR, 49 bar sentuh)
  - M15: resistance 159.283 (0.57 ATR, 71 bar sentuh) · support 159.24733 (0.83 ATR, 56 bar sentuh)
- **USD/CHF** (NO TRADE)
  - H1: resistance 0.83478 (0.7 ATR, 10 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance 0.83455 (0.94 ATR, 15 bar sentuh) · support 0.83425 (0.28 ATR, 35 bar sentuh)
- **AUD/USD** (NO TRADE)
  - H1: resistance 0.66378 (0.52 ATR, 40 bar sentuh) · support 0.66264 (0.88 ATR, 40 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 0.66332 (0.44 ATR, 33 bar sentuh)
- **USD/CAD** (NO TRADE)
  - H1: resistance 1.42515 (0.53 ATR, 5 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance 1.42497 (0.74 ATR, 12 bar sentuh) · support 1.42463 (0.27 ATR, 22 bar sentuh)
- **NZD/USD** (NO TRADE)
  - H1: resistance 0.54755 (0.67 ATR, 27 bar sentuh) · support 0.54698 (0.27 ATR, 24 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 0.54719 (0.06 ATR, 23 bar sentuh)
- **EUR/GBP** (NO TRADE)
  - H1: resistance 0.83769 (1.41 ATR, 44 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance 0.83713 (0.93 ATR, 25 bar sentuh) · support tidak ada dalam jarak
- **EUR/JPY** (NO TRADE)
  - H1: resistance 174.83527 (0.58 ATR, 43 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance 174.77183 (0.97 ATR, 30 bar sentuh) · support 174.71486 (0.47 ATR, 28 bar sentuh)
- **EUR/CHF** (NO TRADE)
  - H1: resistance 0.91579 (0.74 ATR, 14 bar sentuh) · support 0.91477 (0.54 ATR, 8 bar sentuh)
  - M15: resistance 0.91544 (0.81 ATR, 30 bar sentuh) · support tidak ada dalam jarak
- **EUR/AUD** (NO TRADE)
  - H1: resistance 1.65586 (0.88 ATR, 22 bar sentuh) · support 1.65297 (0.51 ATR, 27 bar sentuh)
  - M15: resistance 1.65386 (0.44 ATR, 27 bar sentuh) · support 1.65357 (0.13 ATR, 19 bar sentuh)
- **EUR/CAD** (NO TRADE)
  - H1: resistance 1.56427 (1.16 ATR, 6 bar sentuh) · support 1.56217 (0.63 ATR, 16 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 1.56273 (0.21 ATR, 33 bar sentuh)
- **EUR/NZD** (NO TRADE)
  - H1: resistance 2.00674 (0.77 ATR, 19 bar sentuh) · support 2.00332 (1.21 ATR, 38 bar sentuh)
  - M15: resistance 2.00496 (0.02 ATR, 47 bar sentuh) · support tidak ada dalam jarak
- **XAU/USD** (NO TRADE)
  - H1: resistance 3586.92868 (0.99 ATR, 23 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance 3569.3091 (0.46 ATR, 65 bar sentuh) · support tidak ada dalam jarak
- **XAU/AUD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 5373.17342 (0.3 ATR, 41 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support tidak ada dalam jarak

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

