# Laporan Scanner Adaptive Forex

- Waktu eksekusi: 2026-11-25T23:00:54Z
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
| EUR/CAD | **SELL** | LEAD-LAG: GBP/JPY memimpin 50 mnt, korelasi 0.61, n 30 | 1.56003 | 1.56075 | 1.55895 | 7.2 pip |
| USD/CHF | **SELL** | LEAD-LAG: AUD/CHF memimpin 15 mnt, korelasi -0.57, n 33 | 0.8309 | 0.83156 | 0.8299 | 6.7 pip |

## Lead-lag (backtest 6 jam, BUKAN sinyal)
- Status: dianalisa
- Pair gagal diambil (M5): tidak ada
- Backtest jendela 360 menit, diperbarui 2026-11-25T23:00:54Z, pasangan lolos 35.

Pasangan lolos (10 teratas, urut |korelasi|):

| Leader | Follower | Lag (menit) | Korelasi | Korelasi lag 0 | n |
|---|---|---|---|---|---|
| EUR/GBP | AUD/NZD | 60 | -0.684 | -0.211 | 26 |
| EUR/GBP | EUR/USD | 30 | 0.618 | 0.232 | 32 |
| CHF/JPY | CAD/CHF | 50 | -0.614 | -0.071 | 26 |
| GBP/JPY | EUR/CAD | 50 | 0.611 | -0.022 | 30 |
| AUD/NZD | GBP/JPY | 30 | -0.588 | 0.424 | 32 |
| CHF/JPY | EUR/CAD | 50 | 0.576 | 0.133 | 28 |
| AUD/NZD | EUR/USD | 15 | 0.575 | 0.079 | 35 |
| AUD/CHF | USD/CHF | 15 | -0.57 | 0.534 | 33 |
| CHF/JPY | USD/CAD | 50 | 0.57 | -0.313 | 28 |
| XAU/AUD | GBP/CAD | 25 | -0.563 | 0.013 | 28 |

Kandidat (follower yang tertinggal, urut skor):

| Follower | Arah | Leader | Lag (menit) | z leader | Skor |
|---|---|---|---|---|---|
| EUR/USD | BUY | EUR/GBP | 30 | 0.42 | 0.618 |
| EUR/CAD | SELL | GBP/JPY | 50 | -0.47 | 0.611 |
| USD/CHF | SELL | AUD/CHF | 15 | 0.04 | 0.57 |
| USD/CAD | SELL | CHF/JPY | 50 | -0.16 | 0.57 |
| NZD/USD | SELL | CAD/CHF | 20 | 0.34 | 0.562 |
| USD/JPY | BUY | GBP/CAD | 50 | -0.5 | 0.541 |
| AUD/USD | SELL | CAD/CHF | 20 | 0.34 | 0.532 |
| EUR/AUD | BUY | CHF/JPY | 30 | -0.69 | 0.525 |

## Pemantauan 15 menit (entry dan analisa cadangan)
Nilai di kolom 15m-60m = pip dari entry pada close candle M15 ke-1 sampai ke-4. Jika SL dan TP kena di candle yang sama, dihitung SL. Analisa cadangan BUKAN sinyal.
| Sumber | Pair | Arah | Entry | SL | TP | 15m | 30m | 45m | 60m | Hasil | Pip sekarang | Umur |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LEAD-LAG (analisa cadangan, bukan sinyal) | AUD/USD | BUY | 0.66275 | 0.66204 | 0.66382 | -1.4 | -1.7 | -1.9 | -2.0 | Selesai 60 menit | LOSS 2.0 pip | 60 mnt |
| LEAD-LAG (analisa cadangan, bukan sinyal) | EUR/CAD | SELL | 1.56021 | 1.56098 | 1.55907 | +1.7 | +3.1 | +1.6 | +1.8 | Selesai 60 menit | PROFIT 1.8 pip | 60 mnt |
| LEAD-LAG (analisa cadangan, bukan sinyal) | EUR/JPY | BUY | 174.63 | 174.50731 | 174.81403 | +7.6 | +8.1 | +4.6 | - | BERJALAN | PROFIT 4.6 pip | 46 mnt |
| LEAD-LAG (analisa cadangan, bukan sinyal) | USD/JPY | SELL | 159.1435 | 159.25001 | 158.98374 | +1.9 | +2.7 | - | - | BERJALAN | PROFIT 2.7 pip | 30 mnt |
| LEAD-LAG (analisa cadangan, bukan sinyal) | EUR/GBP | SELL | 0.83684 | 0.83717 | 0.83634 | -0.6 | -0.4 | - | - | BERJALAN | LOSS 0.4 pip | 30 mnt |
| LEAD-LAG (analisa cadangan, bukan sinyal) | EUR/CHF | BUY | 0.91197 | 0.91136 | 0.91288 | +0.2 | - | - | - | BERJALAN | PROFIT 0.2 pip | 16 mnt |
| LEAD-LAG (analisa cadangan, bukan sinyal) | NZD/USD | BUY | 0.54857 | 0.54812 | 0.54925 | +0.1 | - | - | - | BERJALAN | PROFIT 0.1 pip | 16 mnt |
| LEAD-LAG (analisa cadangan, bukan sinyal) | EUR/USD | SELL | 1.09771 | 1.09831 | 1.0968 | +1.3 | - | - | - | BERJALAN | PROFIT 1.3 pip | 16 mnt |

## Evaluasi 1 jam (entry dan analisa cadangan)
Dibuat setelah 60 menit atau saat SL/TP kena. MFE = gerak terbaik, MAE = gerak terburuk, dalam pip.
| Sumber | Pair | Arah | 15m | 30m | 45m | 60m | Hasil | Pip akhir | MFE (pip) | MAE (pip) | Ditutup (UTC) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| LEAD-LAG (analisa cadangan, bukan sinyal) | AUD/USD | BUY | -1.4 | -1.7 | -1.9 | -2.0 | Selesai 60 menit | LOSS 2.0 pip | 0.3 | -2.2 | 2026-11-25T23:00:54Z |
| LEAD-LAG (analisa cadangan, bukan sinyal) | EUR/CAD | SELL | +1.7 | +3.1 | +1.6 | +1.8 | Selesai 60 menit | PROFIT 1.8 pip | 3.3 | 0.1 | 2026-11-25T23:00:54Z |

## Level analisa cadangan (BUKAN sinyal, tanpa statistik)
Level S/R terdekat untuk konteks scalping. Tidak mengubah label atau keputusan apa pun.
- **EUR/USD** (NO TRADE)
  - H1: resistance 1.09897 (1.22 ATR, 30 bar sentuh) · support 1.09609 (1.31 ATR, 30 bar sentuh)
  - M15: resistance 1.09803 (0.89 ATR, 5 bar sentuh) · support 1.09746 (0.24 ATR, 17 bar sentuh)
- **GBP/USD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 1.3094 (1.36 ATR, 29 bar sentuh)
  - M15: resistance 1.31158 (0.04 ATR, 37 bar sentuh) · support tidak ada dalam jarak
- **USD/JPY** (NO TRADE)
  - H1: resistance 159.20919 (0.46 ATR, 70 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance 159.1875 (0.84 ATR, 59 bar sentuh) · support tidak ada dalam jarak
- **USD/CHF** (NO TRADE)
  - H1: resistance 0.83234 (1.08 ATR, 4 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance tidak ada dalam jarak · support 0.83078 (0.23 ATR, 22 bar sentuh)
- **AUD/USD** (NO TRADE)
  - H1: resistance 0.66298 (0.32 ATR, 39 bar sentuh) · support 0.661 (1.16 ATR, 8 bar sentuh)
  - M15: resistance 0.6627 (0.29 ATR, 58 bar sentuh) · support tidak ada dalam jarak
- **USD/CAD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 1.41948 (1.26 ATR, 1 bar sentuh)
  - M15: resistance 1.42179 (0.69 ATR, 3 bar sentuh) · support tidak ada dalam jarak
- **NZD/USD** (NO TRADE)
  - H1: resistance 0.54865 (0.09 ATR, 34 bar sentuh) · support 0.54756 (1.18 ATR, 23 bar sentuh)
  - M15: resistance 0.54891 (0.93 ATR, 13 bar sentuh) · support 0.54839 (0.51 ATR, 20 bar sentuh)
- **EUR/GBP** (NO TRADE)
  - H1: resistance 0.83698 (0.15 ATR, 34 bar sentuh) · support 0.83606 (1.31 ATR, 27 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support tidak ada dalam jarak
- **EUR/JPY** (NO TRADE)
  - H1: resistance 174.70071 (0.1 ATR, 38 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance 174.7595 (0.8 ATR, 13 bar sentuh) · support tidak ada dalam jarak
- **EUR/CHF** (NO TRADE)
  - H1: resistance 0.91231 (0.27 ATR, 6 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance 0.91204 (0.1 ATR, 16 bar sentuh) · support tidak ada dalam jarak
- **EUR/AUD** (NO TRADE)
  - H1: resistance 1.65908 (0.85 ATR, 4 bar sentuh) · support 1.65567 (0.25 ATR, 21 bar sentuh)
  - M15: resistance 1.65674 (0.24 ATR, 13 bar sentuh) · support 1.65538 (0.89 ATR, 7 bar sentuh)
- **EUR/CAD** (NO TRADE)
  - H1: resistance 1.56019 (0.11 ATR, 5 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance 1.56023 (0.3 ATR, 8 bar sentuh) · support tidak ada dalam jarak
- **EUR/NZD** (NO TRADE)
  - H1: resistance 2.00104 (0.03 ATR, 57 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance 2.00168 (0.71 ATR, 52 bar sentuh) · support tidak ada dalam jarak
- **XAU/USD** (NO TRADE)
  - H1: resistance 3608.91558 (0.65 ATR, 18 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance tidak ada dalam jarak · support 3588.0315 (0.04 ATR, 7 bar sentuh)
- **XAU/AUD** (NO TRADE)
  - H1: resistance 5416.917 (0.06 ATR, 10 bar sentuh) · support 5385.4644 (0.67 ATR, 25 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 5411.9015 (0.1 ATR, 7 bar sentuh)

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

