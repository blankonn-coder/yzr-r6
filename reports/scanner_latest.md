# Laporan Scanner Adaptive Forex

- Waktu eksekusi: 2026-11-26T23:00:45Z
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
| EUR/USD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.09733 | — | 168/180 | 2026-11-26T22:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| GBP/USD | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.3107 | — | 168/180 | 2026-11-26T22:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |
| USD/JPY | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 159.252 | — | 168/180 | 2026-11-26T22:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |
| USD/CHF | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.8343 | — | 168/180 | 2026-11-26T22:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |
| AUD/USD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.66324 | — | 168/180 | 2026-11-26T22:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| USD/CAD | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.42453 | — | 168/180 | 2026-11-26T22:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |
| NZD/USD | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.547 | — | 168/180 | 2026-11-26T22:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |
| EUR/GBP | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.83699 | — | 168/180 | 2026-11-26T22:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| EUR/JPY | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 174.7625 | — | 168/180 | 2026-11-26T22:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |
| EUR/CHF | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.91527 | — | 168/180 | 2026-11-26T22:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| EUR/AUD | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.65427 | — | 168/180 | 2026-11-26T22:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |
| EUR/CAD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.56285 | — | 168/180 | 2026-11-26T22:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| EUR/NZD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 2.00588 | — | 168/180 | 2026-11-26T22:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| XAU/USD | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 3568.3995 | — | 168/180 | 2026-11-26T18:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |
| XAU/AUD | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 5380.9635 | — | 168/180 | 2026-11-26T18:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |

## Saran analisa cadangan (BUKAN sinyal, tidak divalidasi backtest)
Dari lead-lag, maks 3 pair: leader bergerak, follower tertinggal 5-60 menit. BUY/SELL mengikuti arah leader. SL 0.5 ATR H1, TP 1.5R. Tanpa cek spread, news, atau batas risiko §9. Tidak mengubah label.
Tidak ada saran (tidak ada level H1 dalam jarak 1.0 ATR, dan tidak ada kandidat lead-lag).

## Lead-lag (backtest 6 jam, BUKAN sinyal)
- Status: dianalisa
- Pair gagal diambil (M5): tidak ada
- Backtest jendela 360 menit, diperbarui 2026-11-26T23:00:45Z, pasangan lolos 2.

Pasangan lolos (10 teratas, urut |korelasi|):

| Leader | Follower | Lag (menit) | Korelasi | Korelasi lag 0 | n |
|---|---|---|---|---|---|
| GBP/CAD | EUR/CHF | 30 | -0.536 | -0.216 | 64 |
| GBP/CAD | GBP/NZD | 55 | -0.518 | 0.457 | 60 |

Kandidat (follower yang tertinggal, urut skor):

| Follower | Arah | Leader | Lag (menit) | z leader | Skor |
|---|---|---|---|---|---|
| EUR/CHF | SELL | GBP/CAD | 30 | 0.04 | 0.536 |

## Pemantauan 15 menit (entry dan analisa cadangan)
Nilai di kolom 15m-60m = pip dari entry pada close candle M15 ke-1 sampai ke-4. Jika SL dan TP kena di candle yang sama, dihitung SL. Analisa cadangan BUKAN sinyal.
| Sumber | Pair | Arah | Entry | SL | TP | 15m | 30m | 45m | 60m | Hasil | Pip sekarang | Umur |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LEAD-LAG (analisa cadangan, bukan sinyal) | EUR/CHF | SELL | 0.91524 | 0.9156 | 0.91471 | -0.3 | - | - | - | BERJALAN | LOSS 0.3 pip | 15 mnt |

## Evaluasi 1 jam (entry dan analisa cadangan)
Dibuat setelah 60 menit atau saat SL/TP kena. MFE = gerak terbaik, MAE = gerak terburuk, dalam pip.
Belum ada evaluasi yang selesai di run ini.

## Level analisa cadangan (BUKAN sinyal, tanpa statistik)
Level S/R terdekat untuk konteks scalping. Tidak mengubah label atau keputusan apa pun.
- **EUR/USD** (NO TRADE)
  - H1: resistance 1.09818 (1.07 ATR, 37 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance 1.09748 (0.62 ATR, 34 bar sentuh) · support 1.09718 (0.65 ATR, 46 bar sentuh)
- **GBP/USD** (NO TRADE)
  - H1: resistance 1.31215 (1.44 ATR, 20 bar sentuh) · support 1.31042 (0.28 ATR, 52 bar sentuh)
  - M15: resistance 1.31093 (0.88 ATR, 42 bar sentuh) · support 1.31049 (0.81 ATR, 35 bar sentuh)
- **USD/JPY** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 159.15019 (1.09 ATR, 45 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 159.24656 (0.29 ATR, 48 bar sentuh)
- **USD/CHF** (NO TRADE)
  - H1: resistance 0.83478 (0.59 ATR, 9 bar sentuh) · support 0.83398 (0.4 ATR, 14 bar sentuh)
  - M15: resistance 0.83448 (0.88 ATR, 23 bar sentuh) · support 0.83425 (0.3 ATR, 40 bar sentuh)
- **AUD/USD** (NO TRADE)
  - H1: resistance 0.66378 (0.78 ATR, 39 bar sentuh) · support 0.66264 (0.85 ATR, 38 bar sentuh)
  - M15: resistance 0.66332 (0.53 ATR, 34 bar sentuh) · support 0.66308 (0.98 ATR, 36 bar sentuh)
- **USD/CAD** (NO TRADE)
  - H1: resistance 1.42506 (0.62 ATR, 8 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance 1.42463 (0.38 ATR, 25 bar sentuh) · support 1.42443 (0.42 ATR, 20 bar sentuh)
- **NZD/USD** (NO TRADE)
  - H1: resistance 0.5475 (0.98 ATR, 25 bar sentuh) · support 0.54697 (0.06 ATR, 25 bar sentuh)
  - M15: resistance 0.547 (0.02 ATR, 12 bar sentuh) · support tidak ada dalam jarak
- **EUR/GBP** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 0.83665 (0.85 ATR, 46 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 0.8369 (0.76 ATR, 33 bar sentuh)
- **EUR/JPY** (NO TRADE)
  - H1: resistance 174.82362 (0.45 ATR, 41 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance tidak ada dalam jarak · support 174.73729 (0.74 ATR, 37 bar sentuh)
- **EUR/CHF** (NO TRADE)
  - H1: resistance 0.91579 (0.77 ATR, 14 bar sentuh) · support 0.91484 (0.64 ATR, 7 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 0.91521 (0.38 ATR, 45 bar sentuh)
- **EUR/AUD** (NO TRADE)
  - H1: resistance 1.65586 (0.88 ATR, 22 bar sentuh) · support 1.65297 (0.72 ATR, 30 bar sentuh)
  - M15: resistance 1.65428 (0.01 ATR, 43 bar sentuh) · support tidak ada dalam jarak
- **EUR/CAD** (NO TRADE)
  - H1: resistance 1.56411 (1.24 ATR, 7 bar sentuh) · support 1.56217 (0.67 ATR, 16 bar sentuh)
  - M15: resistance 1.56314 (0.97 ATR, 26 bar sentuh) · support 1.5627 (0.51 ATR, 40 bar sentuh)
- **EUR/NZD** (NO TRADE)
  - H1: resistance 2.00655 (0.44 ATR, 19 bar sentuh) · support 2.00425 (1.06 ATR, 36 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 2.00575 (0.28 ATR, 26 bar sentuh)
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

