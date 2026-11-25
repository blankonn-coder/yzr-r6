# Laporan Scanner Adaptive Forex

- Waktu eksekusi: 2026-11-25T03:15:22Z
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
| EUR/USD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.0955 | — | 168/180 | 2026-11-25T02:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| GBP/USD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.31025 | — | 168/180 | 2026-11-25T02:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| USD/JPY | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 159.1245 | — | 168/180 | 2026-11-25T02:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |
| USD/CHF | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.83581 | — | 168/180 | 2026-11-25T02:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| AUD/USD | VOLATIL/CHOPPY | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.66126 | — | 168/180 | 2026-11-25T02:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime VOLATIL/CHOPPY belum punya metode prioritas di ranking |
| USD/CAD | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.42677 | — | 168/180 | 2026-11-25T02:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| NZD/USD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.54673 | — | 168/180 | 2026-11-25T02:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| EUR/GBP | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.83612 | — | 168/180 | 2026-11-25T02:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| EUR/JPY | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 174.3205 | — | 168/180 | 2026-11-25T02:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| EUR/CHF | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.91561 | — | 168/180 | 2026-11-25T02:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| EUR/AUD | MIXED | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.65673 | — | 168/180 | 2026-11-25T02:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime MIXED belum punya metode prioritas di ranking |
| EUR/CAD | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.56299 | — | 168/180 | 2026-11-25T02:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| EUR/NZD | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 2.00373 | — | 168/180 | 2026-11-25T02:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |
| XAU/USD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 3550.8995 | — | 168/180 | 2026-11-25T02:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| XAU/AUD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 5369.8365 | — | 168/180 | 2026-11-25T02:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |

## Saran analisa cadangan (BUKAN sinyal, tidak divalidasi backtest)
Dari lead-lag, maks 3 pair: leader bergerak, follower tertinggal 5-60 menit. BUY/SELL mengikuti arah leader. SL 0.5 ATR H1, TP 1.5R. Tanpa cek spread, news, atau batas risiko §9. Tidak mengubah label.
Tidak ada saran (tidak ada level H1 dalam jarak 1.0 ATR, dan tidak ada kandidat lead-lag).

## Lead-lag (backtest 6 jam, BUKAN sinyal)
- Status: dianalisa
- Pair gagal diambil (M5): tidak ada
- Backtest jendela 360 menit, diperbarui 2026-11-25T03:15:22Z, pasangan lolos 2.

Pasangan lolos (10 teratas, urut |korelasi|):

| Leader | Follower | Lag (menit) | Korelasi | Korelasi lag 0 | n |
|---|---|---|---|---|---|
| NZD/USD | USD/CHF | 5 | -0.551 | -0.31 | 68 |
| CAD/JPY | EUR/GBP | 35 | -0.519 | 0.03 | 62 |

Kandidat (follower yang tertinggal, urut skor):

| Follower | Arah | Leader | Lag (menit) | z leader | Skor |
|---|---|---|---|---|---|
| USD/CHF | SELL | NZD/USD | 5 | 0.64 | 0.551 |
| EUR/GBP | BUY | CAD/JPY | 35 | -1.25 | 0.519 |

## Pemantauan 15 menit (entry dan analisa cadangan)
Nilai di kolom 15m-60m = pip dari entry pada close candle M15 ke-1 sampai ke-4. Jika SL dan TP kena di candle yang sama, dihitung SL. Analisa cadangan BUKAN sinyal.
| Sumber | Pair | Arah | Entry | SL | TP | 15m | 30m | 45m | 60m | Hasil | Pip sekarang | Umur |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LEAD-LAG (analisa cadangan, bukan sinyal) | EUR/GBP | SELL | 0.83615 | 0.83637 | 0.83583 | +0.0 | +0.3 | -0.3 | - | BERJALAN | LOSS 0.3 pip | 45 mnt |
| LEAD-LAG (analisa cadangan, bukan sinyal) | USD/CHF | BUY | 0.83581 | 0.83534 | 0.83653 | +4.6 | - | - | - | BERJALAN | PROFIT 4.6 pip | 15 mnt |

## Evaluasi 1 jam (entry dan analisa cadangan)
Dibuat setelah 60 menit atau saat SL/TP kena. MFE = gerak terbaik, MAE = gerak terburuk, dalam pip.
Belum ada evaluasi yang selesai di run ini.

## Level analisa cadangan (BUKAN sinyal, tanpa statistik)
Level S/R terdekat untuk konteks scalping. Tidak mengubah label atau keputusan apa pun.
- **EUR/USD** (NO TRADE)
  - H1: resistance 1.09603 (0.53 ATR, 24 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance tidak ada dalam jarak · support tidak ada dalam jarak
- **GBP/USD** (NO TRADE)
  - H1: resistance 1.31042 (0.15 ATR, 31 bar sentuh) · support 1.3094 (0.73 ATR, 21 bar sentuh)
  - M15: resistance 1.31 (0.35 ATR, 17 bar sentuh) · support tidak ada dalam jarak
- **USD/JPY** (NO TRADE)
  - H1: resistance 159.25153 (0.8 ATR, 62 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance tidak ada dalam jarak · support 159.18129 (0.32 ATR, 45 bar sentuh)
- **USD/CHF** (NO TRADE)
  - H1: resistance 0.83669 (0.92 ATR, 3 bar sentuh) · support 0.835 (0.85 ATR, 6 bar sentuh)
  - M15: resistance 0.83647 (0.5 ATR, 9 bar sentuh) · support 0.83598 (0.74 ATR, 21 bar sentuh)
- **AUD/USD** (NO TRADE)
  - H1: resistance 0.66295 (1.23 ATR, 33 bar sentuh) · support 0.661 (0.19 ATR, 6 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 0.66115 (0.31 ATR, 6 bar sentuh)
- **USD/CAD** (NO TRADE)
  - H1: resistance 1.42709 (0.28 ATR, 12 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance 1.42738 (0.32 ATR, 12 bar sentuh) · support tidak ada dalam jarak
- **NZD/USD** (NO TRADE)
  - H1: resistance 0.54756 (1.04 ATR, 22 bar sentuh) · support 0.54628 (0.57 ATR, 6 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 0.5467 (0.02 ATR, 15 bar sentuh)
- **EUR/GBP** (NO TRADE)
  - H1: resistance 0.83626 (0.35 ATR, 27 bar sentuh) · support 0.83592 (0.46 ATR, 14 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support tidak ada dalam jarak
- **EUR/JPY** (NO TRADE)
  - H1: resistance 174.51236 (0.96 ATR, 28 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance tidak ada dalam jarak · support 174.2865 (0.92 ATR, 16 bar sentuh)
- **EUR/CHF** (NO TRADE)
  - H1: resistance 0.91569 (0.1 ATR, 5 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance 0.91607 (0.63 ATR, 24 bar sentuh) · support 0.91581 (0.25 ATR, 13 bar sentuh)
- **EUR/AUD** (NO TRADE)
  - H1: resistance 1.65908 (0.74 ATR, 1 bar sentuh) · support 1.65579 (0.3 ATR, 16 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support tidak ada dalam jarak
- **EUR/CAD** (NO TRADE)
  - H1: resistance 1.56452 (1.12 ATR, 10 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance 1.56324 (0.23 ATR, 5 bar sentuh) · support tidak ada dalam jarak
- **EUR/NZD** (NO TRADE)
  - H1: resistance 2.00637 (1.13 ATR, 16 bar sentuh) · support 2.00084 (1.23 ATR, 55 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 2.00261 (0.58 ATR, 51 bar sentuh)
- **XAU/USD** (NO TRADE)
  - H1: resistance 3569.0095 (0.91 ATR, 19 bar sentuh) · support 3546.6735 (0.21 ATR, 15 bar sentuh)
  - M15: resistance 3560.71183 (0.25 ATR, 21 bar sentuh) · support 3546.6735 (0.94 ATR, 13 bar sentuh)
- **XAU/AUD** (NO TRADE)
  - H1: resistance 5377.10775 (0.25 ATR, 17 bar sentuh) · support 5341.0465 (1.0 ATR, 18 bar sentuh)
  - M15: resistance 5389.98367 (0.66 ATR, 6 bar sentuh) · support 5376.8335 (0.16 ATR, 13 bar sentuh)

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

