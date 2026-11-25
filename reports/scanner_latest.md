# Laporan Scanner Adaptive Forex

- Waktu eksekusi: 2026-11-25T00:30:35Z
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
| EUR/USD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.0962 | — | 168/180 | 2026-11-24T23:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| GBP/USD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.31112 | — | 168/180 | 2026-11-24T23:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| USD/JPY | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 159.263 | — | 168/180 | 2026-11-24T23:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |
| USD/CHF | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.83583 | — | 168/180 | 2026-11-24T23:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| AUD/USD | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.66336 | — | 168/180 | 2026-11-24T23:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |
| USD/CAD | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.42735 | — | 168/180 | 2026-11-24T23:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| NZD/USD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.54766 | — | 168/180 | 2026-11-24T23:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| EUR/GBP | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.83606 | — | 168/180 | 2026-11-24T23:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |
| EUR/JPY | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 174.5805 | — | 168/180 | 2026-11-24T23:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| EUR/CHF | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.91622 | — | 168/180 | 2026-11-24T23:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| EUR/AUD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.65253 | — | 168/180 | 2026-11-24T23:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| EUR/CAD | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.56465 | — | 168/180 | 2026-11-24T23:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| EUR/NZD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 2.00165 | — | 168/180 | 2026-11-24T23:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| XAU/USD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 3551.1915 | — | 168/180 | 2026-11-24T23:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| XAU/AUD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 5353.5595 | — | 168/180 | 2026-11-24T23:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |

## Saran analisa cadangan (BUKAN sinyal, tidak divalidasi backtest)
Dari lead-lag, maks 3 pair: leader bergerak, follower tertinggal 5-60 menit. BUY/SELL mengikuti arah leader. SL 0.5 ATR H1, TP 1.5R. Tanpa cek spread, news, atau batas risiko §9. Tidak mengubah label.
| Pair | Arah | Dasar | Entry | SL | TP | Risiko SL |
|---|---|---|---|---|---|---|
| GBP/USD | **BUY** | LEAD-LAG: EUR/GBP memimpin 50 mnt, korelasi 0.56, n 60 | 1.3108 | 1.31021 | 1.3117 | 5.9 pip |

## Lead-lag (backtest 6 jam, BUKAN sinyal)
- Status: dianalisa
- Pair gagal diambil (M5): tidak ada
- Backtest jendela 360 menit, diperbarui 2026-11-25T00:30:35Z, pasangan lolos 3.

Pasangan lolos (10 teratas, urut |korelasi|):

| Leader | Follower | Lag (menit) | Korelasi | Korelasi lag 0 | n |
|---|---|---|---|---|---|
| EUR/GBP | GBP/USD | 50 | 0.557 | -0.171 | 60 |
| EUR/GBP | NZD/CHF | 25 | 0.517 | -0.269 | 65 |
| GBP/CHF | EUR/CAD | 35 | -0.51 | -0.032 | 61 |

Kandidat (follower yang tertinggal, urut skor):

| Follower | Arah | Leader | Lag (menit) | z leader | Skor |
|---|---|---|---|---|---|
| EUR/CAD | BUY | GBP/CHF | 35 | -1.48 | 0.756 |
| GBP/USD | BUY | EUR/GBP | 50 | 0.55 | 0.557 |

## Pemantauan 15 menit (entry dan analisa cadangan)
Nilai di kolom 15m-60m = pip dari entry pada close candle M15 ke-1 sampai ke-4. Jika SL dan TP kena di candle yang sama, dihitung SL. Analisa cadangan BUKAN sinyal.
| Sumber | Pair | Arah | Entry | SL | TP | 15m | 30m | 45m | 60m | Hasil | Pip sekarang | Umur |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LEAD-LAG (analisa cadangan, bukan sinyal) | USD/JPY | SELL | 159.2825 | 159.36194 | 159.16334 | +1.9 | +11.3 | -3.1 | - | BERJALAN | LOSS 3.1 pip | 45 mnt |
| LEAD-LAG (analisa cadangan, bukan sinyal) | EUR/NZD | SELL | 2.00165 | 2.0027 | 2.00007 | -1.1 | +6.3 | - | - | BERJALAN | PROFIT 6.3 pip | 30 mnt |
| LEAD-LAG (analisa cadangan, bukan sinyal) | EUR/CAD | BUY | 1.56439 | 1.56368 | 1.56546 | -5.8 | - | - | - | BERJALAN | LOSS 5.8 pip | 15 mnt |
| LEAD-LAG (analisa cadangan, bukan sinyal) | EUR/JPY | SELL | 174.5165 | 174.61571 | 174.36768 | - | - | - | - | SL kena | LOSS 9.9 pip | 15 mnt |

## Evaluasi 1 jam (entry dan analisa cadangan)
Dibuat setelah 60 menit atau saat SL/TP kena. MFE = gerak terbaik, MAE = gerak terburuk, dalam pip.
| Sumber | Pair | Arah | 15m | 30m | 45m | 60m | Hasil | Pip akhir | MFE (pip) | MAE (pip) | Ditutup (UTC) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| LEAD-LAG (analisa cadangan, bukan sinyal) | EUR/JPY | SELL | - | - | - | - | SL kena · menit 15 | LOSS 9.9 pip | 0.6 | -10.0 | 2026-11-25T00:30:35Z |

## Level analisa cadangan (BUKAN sinyal, tanpa statistik)
Level S/R terdekat untuk konteks scalping. Tidak mengubah label atau keputusan apa pun.
- **EUR/USD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 1.09603 (0.17 ATR, 22 bar sentuh)
  - M15: resistance 1.09625 (0.83 ATR, 22 bar sentuh) · support tidak ada dalam jarak
- **GBP/USD** (NO TRADE)
  - H1: resistance 1.31116 (0.04 ATR, 31 bar sentuh) · support 1.31042 (0.59 ATR, 29 bar sentuh)
  - M15: resistance 1.31092 (0.27 ATR, 27 bar sentuh) · support 1.31052 (0.64 ATR, 22 bar sentuh)
- **USD/JPY** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 159.16314 (0.64 ATR, 38 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 159.25653 (0.86 ATR, 51 bar sentuh)
- **USD/CHF** (NO TRADE)
  - H1: resistance 0.83669 (0.88 ATR, 3 bar sentuh) · support 0.835 (0.85 ATR, 5 bar sentuh)
  - M15: resistance 0.83598 (0.45 ATR, 12 bar sentuh) · support 0.83553 (0.77 ATR, 25 bar sentuh)
- **AUD/USD** (NO TRADE)
  - H1: resistance 0.6634 (0.04 ATR, 29 bar sentuh) · support 0.66205 (1.27 ATR, 20 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 0.66317 (0.54 ATR, 43 bar sentuh)
- **USD/CAD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 1.42697 (0.3 ATR, 10 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 1.42668 (0.48 ATR, 10 bar sentuh)
- **NZD/USD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 0.54756 (0.14 ATR, 19 bar sentuh)
  - M15: resistance 0.54769 (0.04 ATR, 27 bar sentuh) · support 0.54744 (0.88 ATR, 20 bar sentuh)
- **EUR/GBP** (NO TRADE)
  - H1: resistance 0.83661 (1.26 ATR, 31 bar sentuh) · support 0.83592 (0.31 ATR, 11 bar sentuh)
  - M15: resistance 0.83615 (0.55 ATR, 37 bar sentuh) · support tidak ada dalam jarak
- **EUR/JPY** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 174.51236 (0.34 ATR, 25 bar sentuh)
  - M15: resistance 174.6015 (0.1 ATR, 43 bar sentuh) · support tidak ada dalam jarak
- **EUR/CHF** (NO TRADE)
  - H1: resistance 0.91743 (1.48 ATR, 9 bar sentuh) · support 0.91569 (0.64 ATR, 3 bar sentuh)
  - M15: resistance 0.91607 (0.19 ATR, 17 bar sentuh) · support 0.91583 (0.73 ATR, 9 bar sentuh)
- **EUR/AUD** (NO TRADE)
  - H1: resistance 1.65267 (0.06 ATR, 19 bar sentuh) · support 1.65045 (0.91 ATR, 20 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 1.65129 (0.9 ATR, 50 bar sentuh)
- **EUR/CAD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 1.56437 (0.2 ATR, 7 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support tidak ada dalam jarak
- **EUR/NZD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 2.00084 (0.39 ATR, 51 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support tidak ada dalam jarak
- **XAU/USD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 3546.6735 (0.24 ATR, 12 bar sentuh)
  - M15: resistance 3546.6735 (0.45 ATR, 5 bar sentuh) · support tidak ada dalam jarak
- **XAU/AUD** (NO TRADE)
  - H1: resistance 5377.382 (0.95 ATR, 15 bar sentuh) · support 5341.0465 (0.5 ATR, 15 bar sentuh)
  - M15: resistance 5341.0465 (0.06 ATR, 4 bar sentuh) · support tidak ada dalam jarak

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

