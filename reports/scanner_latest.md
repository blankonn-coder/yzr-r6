# Laporan Scanner Adaptive Forex

- Waktu eksekusi: 2026-11-25T01:00:38Z
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
| EUR/CHF | **SELL** | LEAD-LAG: USD/CHF memimpin 5 mnt, korelasi 0.51, n 68 | 0.91626 | 0.91667 | 0.91564 | 4.1 pip |
| XAU/AUD | **BUY** | LEAD-LAG: USD/JPY memimpin 40 mnt, korelasi -0.64, n 51 | 5332.7015 | 5319.51294 | 5352.48434 | 131.9 pip |

## Lead-lag (backtest 6 jam, BUKAN sinyal)
- Status: dianalisa
- Pair gagal diambil (M5): tidak ada
- Backtest jendela 360 menit, diperbarui 2026-11-25T01:00:38Z, pasangan lolos 6.

Pasangan lolos (10 teratas, urut |korelasi|):

| Leader | Follower | Lag (menit) | Korelasi | Korelasi lag 0 | n |
|---|---|---|---|---|---|
| USD/JPY | XAU/AUD | 40 | -0.639 | -0.08 | 51 |
| USD/JPY | XAU/USD | 40 | -0.554 | -0.213 | 51 |
| GBP/JPY | NZD/USD | 30 | 0.549 | 0.072 | 65 |
| USD/CHF | EUR/CHF | 5 | 0.513 | 0.384 | 68 |
| NZD/CAD | GBP/JPY | 45 | -0.505 | -0.042 | 62 |
| EUR/GBP | GBP/USD | 50 | 0.501 | -0.244 | 60 |

Kandidat (follower yang tertinggal, urut skor):

| Follower | Arah | Leader | Lag (menit) | z leader | Skor |
|---|---|---|---|---|---|
| GBP/USD | SELL | EUR/GBP | 50 | -1.97 | 0.99 |
| EUR/CHF | SELL | USD/CHF | 5 | -1.62 | 0.83 |
| XAU/AUD | BUY | USD/JPY | 40 | -0.06 | 0.639 |
| XAU/USD | BUY | USD/JPY | 40 | -0.06 | 0.554 |
| NZD/USD | BUY | GBP/JPY | 30 | 0.03 | 0.549 |

## Pemantauan 15 menit (entry dan analisa cadangan)
Nilai di kolom 15m-60m = pip dari entry pada close candle M15 ke-1 sampai ke-4. Jika SL dan TP kena di candle yang sama, dihitung SL. Analisa cadangan BUKAN sinyal.
| Sumber | Pair | Arah | Entry | SL | TP | 15m | 30m | 45m | 60m | Hasil | Pip sekarang | Umur |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LEAD-LAG (analisa cadangan, bukan sinyal) | EUR/NZD | SELL | 2.00165 | 2.0027 | 2.00007 | -1.1 | +6.3 | +6.3 | - | TP kena | PROFIT 15.8 pip | 60 mnt |
| LEAD-LAG (analisa cadangan, bukan sinyal) | GBP/USD | BUY | 1.3108 | 1.31021 | 1.3117 | -0.1 | +6.3 | - | - | BERJALAN | PROFIT 6.3 pip | 30 mnt |
| LEAD-LAG (analisa cadangan, bukan sinyal) | NZD/USD | BUY | 0.54776 | 0.5474 | 0.5483 | +2.3 | - | - | - | BERJALAN | PROFIT 2.3 pip | 15 mnt |

## Evaluasi 1 jam (entry dan analisa cadangan)
Dibuat setelah 60 menit atau saat SL/TP kena. MFE = gerak terbaik, MAE = gerak terburuk, dalam pip.
| Sumber | Pair | Arah | 15m | 30m | 45m | 60m | Hasil | Pip akhir | MFE (pip) | MAE (pip) | Ditutup (UTC) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| LEAD-LAG (analisa cadangan, bukan sinyal) | EUR/NZD | SELL | -1.1 | +6.3 | +6.3 | - | TP kena · menit 60 | PROFIT 15.8 pip | 16.5 | -9.2 | 2026-11-25T01:00:38Z |

## Level analisa cadangan (BUKAN sinyal, tanpa statistik)
Level S/R terdekat untuk konteks scalping. Tidak mengubah label atau keputusan apa pun.
- **EUR/USD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 1.09603 (0.13 ATR, 22 bar sentuh)
  - M15: resistance 1.09628 (0.31 ATR, 26 bar sentuh) · support tidak ada dalam jarak
- **GBP/USD** (NO TRADE)
  - H1: resistance 1.31242 (0.84 ATR, 12 bar sentuh) · support 1.31116 (0.23 ATR, 32 bar sentuh)
  - M15: resistance 1.31167 (0.5 ATR, 29 bar sentuh) · support tidak ada dalam jarak
- **USD/JPY** (NO TRADE)
  - H1: resistance 159.25153 (0.08 ATR, 60 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance 159.25141 (0.18 ATR, 53 bar sentuh) · support tidak ada dalam jarak
- **USD/CHF** (NO TRADE)
  - H1: resistance 0.83669 (0.87 ATR, 3 bar sentuh) · support 0.835 (0.88 ATR, 5 bar sentuh)
  - M15: resistance 0.83598 (0.33 ATR, 14 bar sentuh) · support tidak ada dalam jarak
- **AUD/USD** (NO TRADE)
  - H1: resistance 0.66726 (1.49 ATR, 14 bar sentuh) · support 0.66545 (0.02 ATR, 20 bar sentuh)
  - M15: resistance 0.66562 (0.25 ATR, 10 bar sentuh) · support tidak ada dalam jarak
- **USD/CAD** (NO TRADE)
  - H1: resistance 1.42697 (0.46 ATR, 10 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance 1.42668 (0.56 ATR, 12 bar sentuh) · support tidak ada dalam jarak
- **NZD/USD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 0.54756 (0.6 ATR, 20 bar sentuh)
  - M15: resistance 0.54816 (0.55 ATR, 17 bar sentuh) · support 0.54769 (0.97 ATR, 28 bar sentuh)
- **EUR/GBP** (NO TRADE)
  - H1: resistance 0.83592 (0.11 ATR, 12 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance tidak ada dalam jarak · support 0.83571 (0.93 ATR, 1 bar sentuh)
- **EUR/JPY** (NO TRADE)
  - H1: resistance 174.7524 (1.0 ATR, 33 bar sentuh) · support 174.51236 (0.23 ATR, 26 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 174.51879 (0.5 ATR, 23 bar sentuh)
- **EUR/CHF** (NO TRADE)
  - H1: resistance 0.91665 (0.48 ATR, 5 bar sentuh) · support 0.91569 (0.69 ATR, 4 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 0.91607 (0.69 ATR, 19 bar sentuh)
- **EUR/AUD** (NO TRADE)
  - H1: resistance 1.64955 (0.85 ATR, 19 bar sentuh) · support 1.64587 (0.47 ATR, 34 bar sentuh)
  - M15: resistance 1.64858 (0.93 ATR, 16 bar sentuh) · support 1.64681 (0.25 ATR, 36 bar sentuh)
- **EUR/CAD** (NO TRADE)
  - H1: resistance 1.56437 (0.53 ATR, 8 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance tidak ada dalam jarak · support tidak ada dalam jarak
- **EUR/NZD** (NO TRADE)
  - H1: resistance 2.00084 (0.23 ATR, 52 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance tidak ada dalam jarak · support 1.99974 (0.66 ATR, 27 bar sentuh)
- **XAU/USD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 3546.6735 (0.12 ATR, 13 bar sentuh)
  - M15: resistance 3552.7495 (0.42 ATR, 16 bar sentuh) · support 3546.6735 (0.23 ATR, 7 bar sentuh)
- **XAU/AUD** (NO TRADE)
  - H1: resistance 5341.0465 (0.32 ATR, 16 bar sentuh) · support 5295.08075 (1.43 ATR, 7 bar sentuh)
  - M15: resistance 5341.0465 (0.63 ATR, 5 bar sentuh) · support tidak ada dalam jarak

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

