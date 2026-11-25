# Laporan Scanner Adaptive Forex

- Waktu eksekusi: 2026-11-25T23:45:24Z
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
| EUR/USD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.09758 | — | 168/180 | 2026-11-25T22:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| GBP/USD | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.31155 | — | 168/180 | 2026-11-25T22:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| USD/JPY | MIXED | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 159.1165 | — | 168/180 | 2026-11-25T22:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime MIXED belum punya metode prioritas di ranking |
| USD/CHF | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.8309 | — | 168/180 | 2026-11-25T22:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| AUD/USD | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.66255 | — | 168/180 | 2026-11-25T22:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| USD/CAD | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.42133 | — | 168/180 | 2026-11-25T22:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| NZD/USD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.54858 | — | 168/180 | 2026-11-25T22:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| EUR/GBP | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.83688 | — | 168/180 | 2026-11-25T22:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| EUR/JPY | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 174.676 | — | 168/180 | 2026-11-25T22:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |
| EUR/CHF | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.91199 | — | 168/180 | 2026-11-25T22:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| EUR/AUD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.65645 | — | 168/180 | 2026-11-25T22:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| EUR/CAD | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.56003 | — | 168/180 | 2026-11-25T22:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| EUR/NZD | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 2.00096 | — | 168/180 | 2026-11-25T22:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |
| XAU/USD | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 3588.7435 | — | 168/180 | 2026-11-25T21:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| XAU/AUD | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 5414.324 | — | 168/180 | 2026-11-25T21:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |

## Saran analisa cadangan (BUKAN sinyal, tidak divalidasi backtest)
Dari lead-lag, maks 3 pair: leader bergerak, follower tertinggal 5-60 menit. BUY/SELL mengikuti arah leader. SL 0.5 ATR H1, TP 1.5R. Tanpa cek spread, news, atau batas risiko §9. Tidak mengubah label.
| Pair | Arah | Dasar | Entry | SL | TP | Risiko SL |
|---|---|---|---|---|---|---|
| EUR/USD | **BUY** | LEAD-LAG: AUD/NZD memimpin 35 mnt, korelasi 0.57, n 40 | 1.0971 | 1.09653 | 1.09795 | 5.7 pip |

## Lead-lag (backtest 6 jam, BUKAN sinyal)
- Status: dianalisa
- Pair gagal diambil (M5): tidak ada
- Backtest jendela 360 menit, diperbarui 2026-11-25T23:45:24Z, pasangan lolos 12.

Pasangan lolos (10 teratas, urut |korelasi|):

| Leader | Follower | Lag (menit) | Korelasi | Korelasi lag 0 | n |
|---|---|---|---|---|---|
| NZD/CAD | XAU/USD | 60 | 0.578 | 0.292 | 24 |
| AUD/NZD | EUR/USD | 35 | 0.57 | -0.078 | 40 |
| EUR/GBP | EUR/USD | 30 | 0.57 | 0.133 | 41 |
| EUR/CHF | XAU/AUD | 60 | 0.567 | 0.082 | 23 |
| NZD/CAD | XAU/AUD | 60 | 0.566 | 0.269 | 24 |
| EUR/CHF | XAU/USD | 60 | 0.533 | 0.086 | 23 |
| GBP/AUD | EUR/USD | 15 | -0.519 | -0.007 | 46 |
| XAU/AUD | GBP/CAD | 25 | -0.514 | 0.166 | 31 |
| AUD/USD | EUR/USD | 15 | 0.512 | 0.397 | 46 |
| AUD/USD | USD/CHF | 15 | -0.51 | -0.267 | 44 |

Kandidat (follower yang tertinggal, urut skor):

| Follower | Arah | Leader | Lag (menit) | z leader | Skor |
|---|---|---|---|---|---|
| EUR/USD | BUY | AUD/NZD | 35 | 2.48 | 1.411 |
| USD/CHF | SELL | AUD/USD | 15 | 0.15 | 0.51 |

## Pemantauan 15 menit (entry dan analisa cadangan)
Nilai di kolom 15m-60m = pip dari entry pada close candle M15 ke-1 sampai ke-4. Jika SL dan TP kena di candle yang sama, dihitung SL. Analisa cadangan BUKAN sinyal.
| Sumber | Pair | Arah | Entry | SL | TP | 15m | 30m | 45m | 60m | Hasil | Pip sekarang | Umur |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LEAD-LAG (analisa cadangan, bukan sinyal) | EUR/CHF | BUY | 0.91197 | 0.91136 | 0.91288 | +0.2 | -1.9 | -1.4 | -0.6 | Selesai 60 menit | LOSS 0.6 pip | 60 mnt |
| LEAD-LAG (analisa cadangan, bukan sinyal) | NZD/USD | BUY | 0.54857 | 0.54812 | 0.54925 | +0.1 | +2.2 | +0.8 | -1.1 | Selesai 60 menit | LOSS 1.1 pip | 60 mnt |
| LEAD-LAG (analisa cadangan, bukan sinyal) | EUR/USD | SELL | 1.09771 | 1.09831 | 1.0968 | +1.3 | +1.5 | +0.8 | +6.1 | Selesai 60 menit | PROFIT 6.1 pip | 60 mnt |
| LEAD-LAG (analisa cadangan, bukan sinyal) | EUR/CAD | SELL | 1.56003 | 1.56075 | 1.55895 | +4.9 | +4.2 | +4.7 | - | BERJALAN | PROFIT 4.7 pip | 45 mnt |
| LEAD-LAG (analisa cadangan, bukan sinyal) | USD/CHF | SELL | 0.8309 | 0.83156 | 0.8299 | +1.7 | +1.4 | -3.5 | - | BERJALAN | LOSS 3.5 pip | 45 mnt |
| LEAD-LAG (analisa cadangan, bukan sinyal) | USD/JPY | BUY | 159.1425 | 159.04108 | 159.29463 | +7.5 | - | - | - | BERJALAN | PROFIT 7.5 pip | 15 mnt |

## Evaluasi 1 jam (entry dan analisa cadangan)
Dibuat setelah 60 menit atau saat SL/TP kena. MFE = gerak terbaik, MAE = gerak terburuk, dalam pip.
| Sumber | Pair | Arah | 15m | 30m | 45m | 60m | Hasil | Pip akhir | MFE (pip) | MAE (pip) | Ditutup (UTC) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| LEAD-LAG (analisa cadangan, bukan sinyal) | EUR/CHF | BUY | +0.2 | -1.9 | -1.4 | -0.6 | Selesai 60 menit | LOSS 0.6 pip | 1.0 | -3.3 | 2026-11-25T23:45:24Z |
| LEAD-LAG (analisa cadangan, bukan sinyal) | NZD/USD | BUY | +0.1 | +2.2 | +0.8 | -1.1 | Selesai 60 menit | LOSS 1.1 pip | 3.6 | -1.1 | 2026-11-25T23:45:24Z |
| LEAD-LAG (analisa cadangan, bukan sinyal) | EUR/USD | SELL | +1.3 | +1.5 | +0.8 | +6.1 | Selesai 60 menit | PROFIT 6.1 pip | 7.4 | -0.2 | 2026-11-25T23:45:24Z |

## Level analisa cadangan (BUKAN sinyal, tanpa statistik)
Level S/R terdekat untuk konteks scalping. Tidak mengubah label atau keputusan apa pun.
- **EUR/USD** (NO TRADE)
  - H1: resistance 1.09897 (1.22 ATR, 30 bar sentuh) · support 1.09609 (1.31 ATR, 30 bar sentuh)
  - M15: resistance 1.09752 (0.88 ATR, 21 bar sentuh) · support tidak ada dalam jarak
- **GBP/USD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 1.3094 (1.36 ATR, 29 bar sentuh)
  - M15: resistance 1.31157 (0.61 ATR, 40 bar sentuh) · support tidak ada dalam jarak
- **USD/JPY** (NO TRADE)
  - H1: resistance 159.20919 (0.46 ATR, 70 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance tidak ada dalam jarak · support 159.18488 (0.4 ATR, 60 bar sentuh)
- **USD/CHF** (NO TRADE)
  - H1: resistance 0.83234 (1.08 ATR, 4 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance 0.83159 (0.66 ATR, 11 bar sentuh) · support 0.83076 (1.0 ATR, 24 bar sentuh)
- **AUD/USD** (NO TRADE)
  - H1: resistance 0.66298 (0.32 ATR, 39 bar sentuh) · support 0.661 (1.16 ATR, 8 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 0.66269 (0.07 ATR, 57 bar sentuh)
- **USD/CAD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 1.41948 (1.26 ATR, 1 bar sentuh)
  - M15: resistance 1.42179 (0.05 ATR, 4 bar sentuh) · support tidak ada dalam jarak
- **NZD/USD** (NO TRADE)
  - H1: resistance 0.54865 (0.09 ATR, 34 bar sentuh) · support 0.54756 (1.18 ATR, 23 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 0.54839 (0.2 ATR, 20 bar sentuh)
- **EUR/GBP** (NO TRADE)
  - H1: resistance 0.83698 (0.15 ATR, 34 bar sentuh) · support 0.83606 (1.31 ATR, 27 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 0.8365 (0.63 ATR, 35 bar sentuh)
- **EUR/JPY** (NO TRADE)
  - H1: resistance 174.70071 (0.1 ATR, 38 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance tidak ada dalam jarak · support tidak ada dalam jarak
- **EUR/CHF** (NO TRADE)
  - H1: resistance 0.91231 (0.27 ATR, 6 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance 0.91198 (0.18 ATR, 16 bar sentuh) · support tidak ada dalam jarak
- **EUR/AUD** (NO TRADE)
  - H1: resistance 1.65908 (0.85 ATR, 4 bar sentuh) · support 1.65567 (0.25 ATR, 21 bar sentuh)
  - M15: resistance 1.65538 (0.08 ATR, 8 bar sentuh) · support tidak ada dalam jarak
- **EUR/CAD** (NO TRADE)
  - H1: resistance 1.56019 (0.11 ATR, 5 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance tidak ada dalam jarak · support tidak ada dalam jarak
- **EUR/NZD** (NO TRADE)
  - H1: resistance 2.00104 (0.03 ATR, 57 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance tidak ada dalam jarak · support tidak ada dalam jarak
- **XAU/USD** (NO TRADE)
  - H1: resistance 3608.91558 (0.65 ATR, 18 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance 3589.041 (0.26 ATR, 7 bar sentuh) · support tidak ada dalam jarak
- **XAU/AUD** (NO TRADE)
  - H1: resistance 5416.917 (0.06 ATR, 10 bar sentuh) · support 5385.4644 (0.67 ATR, 25 bar sentuh)
  - M15: resistance 5414.32925 (0.23 ATR, 7 bar sentuh) · support tidak ada dalam jarak

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

