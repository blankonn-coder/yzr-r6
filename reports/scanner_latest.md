# Laporan Scanner Adaptive Forex

- Waktu eksekusi: 2026-11-25T01:30:34Z
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
| EUR/USD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.09616 | — | 168/180 | 2026-11-25T00:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| GBP/USD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.31143 | — | 168/180 | 2026-11-25T00:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| USD/JPY | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 159.2385 | — | 168/180 | 2026-11-25T00:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |
| USD/CHF | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.83586 | — | 168/180 | 2026-11-25T00:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| AUD/USD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.66547 | — | 168/180 | 2026-11-25T00:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| USD/CAD | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.42643 | — | 168/180 | 2026-11-25T00:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| NZD/USD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.54799 | — | 168/180 | 2026-11-25T00:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| EUR/GBP | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.83588 | — | 168/180 | 2026-11-25T00:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |
| EUR/JPY | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 174.5565 | — | 168/180 | 2026-11-25T00:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| EUR/CHF | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.91626 | — | 168/180 | 2026-11-25T00:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| EUR/AUD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.64718 | — | 168/180 | 2026-11-25T00:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| EUR/CAD | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.5636 | — | 168/180 | 2026-11-25T00:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| EUR/NZD | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 2.00034 | — | 168/180 | 2026-11-25T00:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |
| XAU/USD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 3548.8455 | — | 168/180 | 2026-11-25T00:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| XAU/AUD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 5332.7015 | — | 168/180 | 2026-11-25T00:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |

## Saran analisa cadangan (BUKAN sinyal, tidak divalidasi backtest)
Dari lead-lag, maks 3 pair: leader bergerak, follower tertinggal 5-60 menit. BUY/SELL mengikuti arah leader. SL 0.5 ATR H1, TP 1.5R. Tanpa cek spread, news, atau batas risiko §9. Tidak mengubah label.
| Pair | Arah | Dasar | Entry | SL | TP | Risiko SL |
|---|---|---|---|---|---|---|
| XAU/AUD | **BUY** | LEAD-LAG: USD/JPY memimpin 40 mnt, korelasi -0.54, n 51 | 5333.3955 | 5320.20694 | 5353.17834 | 131.9 pip |
| EUR/JPY | **SELL** | LEAD-LAG: XAU/AUD memimpin 35 mnt, korelasi 0.53, n 50 | 174.5325 | 174.63016 | 174.38601 | 9.8 pip |

## Lead-lag (backtest 6 jam, BUKAN sinyal)
- Status: dianalisa
- Pair gagal diambil (M5): tidak ada
- Backtest jendela 360 menit, diperbarui 2026-11-25T01:30:34Z, pasangan lolos 7.

Pasangan lolos (10 teratas, urut |korelasi|):

| Leader | Follower | Lag (menit) | Korelasi | Korelasi lag 0 | n |
|---|---|---|---|---|---|
| USD/JPY | XAU/AUD | 40 | -0.541 | -0.028 | 51 |
| XAU/AUD | EUR/JPY | 35 | 0.528 | 0.002 | 50 |
| USD/JPY | XAU/USD | 40 | -0.516 | -0.159 | 51 |
| EUR/NZD | AUD/JPY | 45 | 0.515 | -0.463 | 61 |
| NZD/CAD | GBP/JPY | 45 | -0.511 | 0.202 | 62 |
| EUR/CAD | EUR/GBP | 35 | 0.502 | 0.315 | 61 |
| GBP/AUD | NZD/CHF | 40 | -0.501 | -0.455 | 63 |

Kandidat (follower yang tertinggal, urut skor):

| Follower | Arah | Leader | Lag (menit) | z leader | Skor |
|---|---|---|---|---|---|
| XAU/AUD | BUY | USD/JPY | 40 | -0.59 | 0.541 |
| EUR/JPY | SELL | XAU/AUD | 35 | -1.09 | 0.528 |
| XAU/USD | BUY | USD/JPY | 40 | -0.59 | 0.516 |
| EUR/GBP | BUY | EUR/CAD | 35 | 0.08 | 0.502 |

## Pemantauan 15 menit (entry dan analisa cadangan)
Nilai di kolom 15m-60m = pip dari entry pada close candle M15 ke-1 sampai ke-4. Jika SL dan TP kena di candle yang sama, dihitung SL. Analisa cadangan BUKAN sinyal.
| Sumber | Pair | Arah | Entry | SL | TP | 15m | 30m | 45m | 60m | Hasil | Pip sekarang | Umur |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LEAD-LAG (analisa cadangan, bukan sinyal) | GBP/USD | BUY | 1.3108 | 1.31021 | 1.3117 | -0.1 | +6.3 | +2.3 | -1.2 | Selesai 60 menit | LOSS 1.2 pip | 60 mnt |
| LEAD-LAG (analisa cadangan, bukan sinyal) | NZD/USD | BUY | 0.54776 | 0.5474 | 0.5483 | +2.3 | +0.1 | - | - | SL kena | LOSS 3.6 pip | 45 mnt |
| LEAD-LAG (analisa cadangan, bukan sinyal) | EUR/CHF | SELL | 0.91626 | 0.91667 | 0.91564 | -0.4 | -0.8 | - | - | BERJALAN | LOSS 0.8 pip | 30 mnt |
| LEAD-LAG (analisa cadangan, bukan sinyal) | XAU/AUD | BUY | 5332.7015 | 5319.51294 | 5352.48434 | -60.3 | - | - | - | SL kena | LOSS 131.9 pip | 30 mnt |
| LEAD-LAG (analisa cadangan, bukan sinyal) | XAU/USD | BUY | 3540.3125 | 3530.8978 | 3554.43455 | +16.6 | - | - | - | BERJALAN | PROFIT 16.6 pip | 15 mnt |

## Evaluasi 1 jam (entry dan analisa cadangan)
Dibuat setelah 60 menit atau saat SL/TP kena. MFE = gerak terbaik, MAE = gerak terburuk, dalam pip.
| Sumber | Pair | Arah | 15m | 30m | 45m | 60m | Hasil | Pip akhir | MFE (pip) | MAE (pip) | Ditutup (UTC) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| LEAD-LAG (analisa cadangan, bukan sinyal) | GBP/USD | BUY | -0.1 | +6.3 | +2.3 | -1.2 | Selesai 60 menit | LOSS 1.2 pip | 6.9 | -1.5 | 2026-11-25T01:30:34Z |
| LEAD-LAG (analisa cadangan, bukan sinyal) | NZD/USD | BUY | +2.3 | +0.1 | - | - | SL kena · menit 45 | LOSS 3.6 pip | 3.2 | -5.1 | 2026-11-25T01:30:34Z |
| LEAD-LAG (analisa cadangan, bukan sinyal) | XAU/AUD | BUY | -60.3 | - | - | - | SL kena · menit 30 | LOSS 131.9 pip | 85.6 | -134.4 | 2026-11-25T01:30:34Z |

## Level analisa cadangan (BUKAN sinyal, tanpa statistik)
Level S/R terdekat untuk konteks scalping. Tidak mengubah label atau keputusan apa pun.
- **EUR/USD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 1.09603 (0.13 ATR, 22 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 1.09541 (0.56 ATR, 7 bar sentuh)
- **GBP/USD** (NO TRADE)
  - H1: resistance 1.31242 (0.84 ATR, 12 bar sentuh) · support 1.31116 (0.23 ATR, 32 bar sentuh)
  - M15: resistance 1.31092 (0.53 ATR, 30 bar sentuh) · support 1.31052 (0.33 ATR, 20 bar sentuh)
- **USD/JPY** (NO TRADE)
  - H1: resistance 159.25153 (0.08 ATR, 60 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance tidak ada dalam jarak · support 159.25675 (0.53 ATR, 57 bar sentuh)
- **USD/CHF** (NO TRADE)
  - H1: resistance 0.83669 (0.87 ATR, 3 bar sentuh) · support 0.835 (0.88 ATR, 5 bar sentuh)
  - M15: resistance 0.83669 (0.88 ATR, 7 bar sentuh) · support 0.83598 (0.91 ATR, 16 bar sentuh)
- **AUD/USD** (NO TRADE)
  - H1: resistance 0.66726 (1.49 ATR, 14 bar sentuh) · support 0.66545 (0.02 ATR, 20 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support tidak ada dalam jarak
- **USD/CAD** (NO TRADE)
  - H1: resistance 1.42697 (0.46 ATR, 10 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance 1.42739 (0.55 ATR, 11 bar sentuh) · support 1.42668 (0.91 ATR, 13 bar sentuh)
- **NZD/USD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 0.54756 (0.6 ATR, 20 bar sentuh)
  - M15: resistance 0.54742 (0.19 ATR, 22 bar sentuh) · support 0.54704 (0.93 ATR, 23 bar sentuh)
- **EUR/GBP** (NO TRADE)
  - H1: resistance 0.83592 (0.11 ATR, 12 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance tidak ada dalam jarak · support tidak ada dalam jarak
- **EUR/JPY** (NO TRADE)
  - H1: resistance 174.7524 (1.0 ATR, 33 bar sentuh) · support 174.51236 (0.23 ATR, 26 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 174.51879 (0.18 ATR, 24 bar sentuh)
- **EUR/CHF** (NO TRADE)
  - H1: resistance 0.91665 (0.48 ATR, 5 bar sentuh) · support 0.91569 (0.69 ATR, 4 bar sentuh)
  - M15: resistance 0.91648 (0.49 ATR, 13 bar sentuh) · support 0.91607 (0.94 ATR, 20 bar sentuh)
- **EUR/AUD** (NO TRADE)
  - H1: resistance 1.64955 (0.85 ATR, 19 bar sentuh) · support 1.64587 (0.47 ATR, 34 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 1.64858 (0.83 ATR, 20 bar sentuh)
- **EUR/CAD** (NO TRADE)
  - H1: resistance 1.56437 (0.53 ATR, 8 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance tidak ada dalam jarak · support tidak ada dalam jarak
- **EUR/NZD** (NO TRADE)
  - H1: resistance 2.00084 (0.23 ATR, 52 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance tidak ada dalam jarak · support 2.00144 (0.24 ATR, 39 bar sentuh)
- **XAU/USD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 3546.6735 (0.12 ATR, 13 bar sentuh)
  - M15: resistance 3546.6735 (0.47 ATR, 8 bar sentuh) · support 3539.8395 (0.21 ATR, 3 bar sentuh)
- **XAU/AUD** (NO TRADE)
  - H1: resistance 5341.0465 (0.32 ATR, 16 bar sentuh) · support 5295.08075 (1.43 ATR, 7 bar sentuh)
  - M15: resistance 5341.0465 (0.55 ATR, 6 bar sentuh) · support tidak ada dalam jarak

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

