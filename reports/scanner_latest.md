# Laporan Scanner Adaptive Forex

- Waktu eksekusi: 2026-11-26T21:15:22Z
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
| EUR/USD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.09692 | — | 168/180 | 2026-11-26T20:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| GBP/USD | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.31062 | — | 168/180 | 2026-11-26T20:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |
| USD/JPY | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 159.2835 | — | 168/180 | 2026-11-26T20:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |
| USD/CHF | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.83437 | — | 168/180 | 2026-11-26T20:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| AUD/USD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.66351 | — | 168/180 | 2026-11-26T20:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| USD/CAD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.42485 | — | 168/180 | 2026-11-26T20:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| NZD/USD | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.54716 | — | 168/180 | 2026-11-26T20:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |
| EUR/GBP | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.83698 | — | 168/180 | 2026-11-26T20:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| EUR/JPY | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 174.7215 | — | 168/180 | 2026-11-26T20:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |
| EUR/CHF | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.91524 | — | 168/180 | 2026-11-26T20:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| EUR/AUD | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.65325 | — | 168/180 | 2026-11-26T20:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |
| EUR/CAD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.56278 | — | 168/180 | 2026-11-26T20:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| EUR/NZD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 2.00481 | — | 168/180 | 2026-11-26T20:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| XAU/USD | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 3568.3995 | — | 168/180 | 2026-11-26T18:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |
| XAU/AUD | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 5380.9635 | — | 168/180 | 2026-11-26T18:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |

## Saran analisa cadangan (BUKAN sinyal, tidak divalidasi backtest)
Dari lead-lag, maks 3 pair: leader bergerak, follower tertinggal 5-60 menit. BUY/SELL mengikuti arah leader. SL 0.5 ATR H1, TP 1.5R. Tanpa cek spread, news, atau batas risiko §9. Tidak mengubah label.
Tidak ada saran (tidak ada level H1 dalam jarak 1.0 ATR, dan tidak ada kandidat lead-lag).

## Lead-lag (backtest 6 jam, BUKAN sinyal)
- Status: dianalisa
- Pair gagal diambil (M5): tidak ada
- Backtest jendela 360 menit, diperbarui 2026-11-26T21:15:22Z, pasangan lolos 1.

Pasangan lolos (10 teratas, urut |korelasi|):

| Leader | Follower | Lag (menit) | Korelasi | Korelasi lag 0 | n |
|---|---|---|---|---|---|
| AUD/CHF | XAU/USD | 15 | -0.516 | -0.243 | 46 |

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
  - H1: resistance tidak ada dalam jarak · support 1.09611 (0.95 ATR, 32 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support tidak ada dalam jarak
- **GBP/USD** (NO TRADE)
  - H1: resistance 1.31215 (1.35 ATR, 22 bar sentuh) · support 1.31042 (0.19 ATR, 50 bar sentuh)
  - M15: resistance 1.31094 (0.89 ATR, 45 bar sentuh) · support 1.31047 (0.43 ATR, 38 bar sentuh)
- **USD/JPY** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 159.15019 (1.28 ATR, 46 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 159.283 (0.02 ATR, 71 bar sentuh)
- **USD/CHF** (NO TRADE)
  - H1: resistance 0.83478 (0.46 ATR, 10 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance 0.83455 (0.45 ATR, 15 bar sentuh) · support 0.83425 (0.86 ATR, 36 bar sentuh)
- **AUD/USD** (NO TRADE)
  - H1: resistance 0.66378 (0.35 ATR, 40 bar sentuh) · support 0.66264 (1.13 ATR, 39 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 0.66332 (0.96 ATR, 31 bar sentuh)
- **USD/CAD** (NO TRADE)
  - H1: resistance 1.42515 (0.32 ATR, 4 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance 1.42497 (0.48 ATR, 14 bar sentuh) · support 1.42463 (0.55 ATR, 24 bar sentuh)
- **NZD/USD** (NO TRADE)
  - H1: resistance 0.5475 (0.59 ATR, 26 bar sentuh) · support 0.54698 (0.31 ATR, 25 bar sentuh)
  - M15: resistance 0.54734 (0.87 ATR, 13 bar sentuh) · support tidak ada dalam jarak
- **EUR/GBP** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 0.83665 (0.75 ATR, 46 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support tidak ada dalam jarak
- **EUR/JPY** (NO TRADE)
  - H1: resistance 174.83527 (0.78 ATR, 42 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance 174.7225 (0.03 ATR, 37 bar sentuh) · support 174.69575 (0.7 ATR, 27 bar sentuh)
- **EUR/CHF** (NO TRADE)
  - H1: resistance 0.91579 (0.73 ATR, 14 bar sentuh) · support 0.91477 (0.63 ATR, 8 bar sentuh)
  - M15: resistance 0.91544 (0.66 ATR, 28 bar sentuh) · support 0.91526 (0.2 ATR, 39 bar sentuh)
- **EUR/AUD** (NO TRADE)
  - H1: resistance 1.65586 (1.32 ATR, 22 bar sentuh) · support 1.65297 (0.14 ATR, 28 bar sentuh)
  - M15: resistance 1.65357 (0.61 ATR, 21 bar sentuh) · support 1.65326 (0.04 ATR, 19 bar sentuh)
- **EUR/CAD** (NO TRADE)
  - H1: resistance 1.56427 (1.34 ATR, 6 bar sentuh) · support 1.56217 (0.55 ATR, 16 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 1.56273 (0.01 ATR, 35 bar sentuh)
- **EUR/NZD** (NO TRADE)
  - H1: resistance 2.00674 (1.16 ATR, 17 bar sentuh) · support 2.0034 (0.85 ATR, 36 bar sentuh)
  - M15: resistance 2.00496 (0.42 ATR, 49 bar sentuh) · support 2.00426 (0.9 ATR, 29 bar sentuh)
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

