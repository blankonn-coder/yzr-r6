# Laporan Scanner Adaptive Forex

- Waktu eksekusi: 2026-11-25T22:45:22Z
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
| EUR/USD | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.0976 | — | 168/180 | 2026-11-25T21:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |
| GBP/USD | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.31168 | — | 168/180 | 2026-11-25T21:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| USD/JPY | MIXED | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 159.144 | — | 168/180 | 2026-11-25T21:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime MIXED belum punya metode prioritas di ranking |
| USD/CHF | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.83091 | — | 168/180 | 2026-11-25T21:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| AUD/USD | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.66275 | — | 168/180 | 2026-11-25T21:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| USD/CAD | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.42151 | — | 168/180 | 2026-11-25T21:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| NZD/USD | MIXED | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.54867 | — | 168/180 | 2026-11-25T21:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime MIXED belum punya metode prioritas di ranking |
| EUR/GBP | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.83679 | — | 168/180 | 2026-11-25T21:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| EUR/JPY | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 174.645 | — | 168/180 | 2026-11-25T21:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |
| EUR/CHF | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.91204 | — | 168/180 | 2026-11-25T21:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| EUR/AUD | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.65599 | — | 168/180 | 2026-11-25T21:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| EUR/CAD | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.56021 | — | 168/180 | 2026-11-25T21:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| EUR/NZD | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 2.00074 | — | 168/180 | 2026-11-25T21:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |
| XAU/USD | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 3574.4535 | — | 168/180 | 2026-11-25T20:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| XAU/AUD | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 5393.032 | — | 168/180 | 2026-11-25T20:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |

## Saran analisa cadangan (BUKAN sinyal, tidak divalidasi backtest)
Dari lead-lag, maks 3 pair: leader bergerak, follower tertinggal 5-60 menit. BUY/SELL mengikuti arah leader. SL 0.5 ATR H1, TP 1.5R. Tanpa cek spread, news, atau batas risiko §9. Tidak mengubah label.
| Pair | Arah | Dasar | Entry | SL | TP | Risiko SL |
|---|---|---|---|---|---|---|
| EUR/CHF | **BUY** | LEAD-LAG: AUD/JPY memimpin 5 mnt, korelasi 0.68, n 38 | 0.91197 | 0.91136 | 0.91288 | 6.1 pip |
| NZD/USD | **BUY** | LEAD-LAG: AUD/CHF memimpin 15 mnt, korelasi 0.66, n 34 | 0.54857 | 0.54812 | 0.54925 | 4.5 pip |
| EUR/USD | **SELL** | LEAD-LAG: AUD/JPY memimpin 15 mnt, korelasi 0.63, n 36 | 1.09771 | 1.09831 | 1.0968 | 6.0 pip |

## Lead-lag (backtest 6 jam, BUKAN sinyal)
- Status: dianalisa
- Pair gagal diambil (M5): tidak ada
- Backtest jendela 360 menit, diperbarui 2026-11-25T22:45:22Z, pasangan lolos 24.

Pasangan lolos (10 teratas, urut |korelasi|):

| Leader | Follower | Lag (menit) | Korelasi | Korelasi lag 0 | n |
|---|---|---|---|---|---|
| AUD/JPY | EUR/CHF | 5 | 0.683 | 0.543 | 38 |
| GBP/CHF | AUD/CAD | 15 | 0.67 | 0.507 | 32 |
| GBP/CHF | NZD/CAD | 15 | 0.665 | 0.347 | 34 |
| AUD/CHF | NZD/USD | 15 | 0.658 | 0.541 | 34 |
| EUR/CHF | AUD/CAD | 15 | 0.651 | 0.503 | 32 |
| AUD/JPY | EUR/USD | 15 | 0.63 | 0.247 | 36 |
| EUR/CHF | NZD/CAD | 15 | 0.628 | 0.403 | 34 |
| AUD/CHF | EUR/USD | 15 | 0.593 | 0.018 | 34 |
| CAD/CHF | CHF/JPY | 15 | 0.591 | -0.091 | 32 |
| GBP/CHF | NZD/USD | 15 | 0.589 | 0.275 | 34 |

Kandidat (follower yang tertinggal, urut skor):

| Follower | Arah | Leader | Lag (menit) | z leader | Skor |
|---|---|---|---|---|---|
| EUR/CHF | BUY | AUD/JPY | 5 | 0.47 | 0.683 |
| NZD/USD | BUY | AUD/CHF | 15 | 0.1 | 0.658 |
| EUR/USD | SELL | AUD/JPY | 15 | -0.02 | 0.63 |
| AUD/USD | BUY | GBP/CHF | 15 | 0.34 | 0.579 |
| GBP/USD | SELL | EUR/AUD | 15 | 0.17 | 0.563 |

## Pemantauan 15 menit (entry dan analisa cadangan)
Nilai di kolom 15m-60m = pip dari entry pada close candle M15 ke-1 sampai ke-4. Jika SL dan TP kena di candle yang sama, dihitung SL. Analisa cadangan BUKAN sinyal.
| Sumber | Pair | Arah | Entry | SL | TP | 15m | 30m | 45m | 60m | Hasil | Pip sekarang | Umur |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LEAD-LAG (analisa cadangan, bukan sinyal) | USD/CHF | SELL | 0.83095 | 0.8317 | 0.82981 | +0.4 | +1.0 | +1.5 | +1.4 | Selesai 60 menit | PROFIT 1.4 pip | 60 mnt |
| LEAD-LAG (analisa cadangan, bukan sinyal) | AUD/USD | BUY | 0.66275 | 0.66204 | 0.66382 | -1.4 | -1.7 | -1.9 | - | BERJALAN | LOSS 1.9 pip | 45 mnt |
| LEAD-LAG (analisa cadangan, bukan sinyal) | EUR/CAD | SELL | 1.56021 | 1.56098 | 1.55907 | +1.7 | +3.1 | +1.6 | - | BERJALAN | PROFIT 1.6 pip | 45 mnt |
| LEAD-LAG (analisa cadangan, bukan sinyal) | EUR/JPY | BUY | 174.63 | 174.50731 | 174.81403 | +7.6 | +8.1 | - | - | BERJALAN | PROFIT 8.1 pip | 30 mnt |
| LEAD-LAG (analisa cadangan, bukan sinyal) | USD/JPY | SELL | 159.1435 | 159.25001 | 158.98374 | +1.9 | - | - | - | BERJALAN | PROFIT 1.9 pip | 15 mnt |
| LEAD-LAG (analisa cadangan, bukan sinyal) | EUR/GBP | SELL | 0.83684 | 0.83717 | 0.83634 | -0.6 | - | - | - | BERJALAN | LOSS 0.6 pip | 15 mnt |

## Evaluasi 1 jam (entry dan analisa cadangan)
Dibuat setelah 60 menit atau saat SL/TP kena. MFE = gerak terbaik, MAE = gerak terburuk, dalam pip.
| Sumber | Pair | Arah | 15m | 30m | 45m | 60m | Hasil | Pip akhir | MFE (pip) | MAE (pip) | Ditutup (UTC) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| LEAD-LAG (analisa cadangan, bukan sinyal) | USD/CHF | SELL | +0.4 | +1.0 | +1.5 | +1.4 | Selesai 60 menit | PROFIT 1.4 pip | 2.3 | -0.6 | 2026-11-25T22:45:22Z |

## Level analisa cadangan (BUKAN sinyal, tanpa statistik)
Level S/R terdekat untuk konteks scalping. Tidak mengubah label atau keputusan apa pun.
- **EUR/USD** (NO TRADE)
  - H1: resistance 1.09897 (1.13 ATR, 31 bar sentuh) · support 1.09609 (1.26 ATR, 30 bar sentuh)
  - M15: resistance 1.09803 (0.6 ATR, 5 bar sentuh) · support 1.09746 (0.48 ATR, 17 bar sentuh)
- **GBP/USD** (NO TRADE)
  - H1: resistance 1.31401 (1.39 ATR, 12 bar sentuh) · support 1.3094 (1.36 ATR, 29 bar sentuh)
  - M15: resistance 1.31164 (0.09 ATR, 33 bar sentuh) · support tidak ada dalam jarak
- **USD/JPY** (NO TRADE)
  - H1: resistance 159.20814 (0.3 ATR, 69 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance 159.1875 (0.71 ATR, 61 bar sentuh) · support tidak ada dalam jarak
- **USD/CHF** (NO TRADE)
  - H1: resistance 0.83234 (1.0 ATR, 4 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance tidak ada dalam jarak · support 0.83078 (0.05 ATR, 22 bar sentuh)
- **AUD/USD** (NO TRADE)
  - H1: resistance 0.66298 (0.16 ATR, 38 bar sentuh) · support 0.661 (1.24 ATR, 8 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support tidak ada dalam jarak
- **USD/CAD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 1.41948 (1.29 ATR, 1 bar sentuh)
  - M15: resistance 1.42179 (0.55 ATR, 3 bar sentuh) · support tidak ada dalam jarak
- **NZD/USD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 0.54865 (0.02 ATR, 33 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 0.54856 (0.02 ATR, 19 bar sentuh)
- **EUR/GBP** (NO TRADE)
  - H1: resistance 0.83698 (0.28 ATR, 33 bar sentuh) · support 0.83661 (0.27 ATR, 41 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support tidak ada dalam jarak
- **EUR/JPY** (NO TRADE)
  - H1: resistance 174.70071 (0.23 ATR, 37 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance 174.7595 (0.45 ATR, 13 bar sentuh) · support tidak ada dalam jarak
- **EUR/CHF** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support tidak ada dalam jarak
  - M15: resistance 0.91204 (0.14 ATR, 15 bar sentuh) · support tidak ada dalam jarak
- **EUR/AUD** (NO TRADE)
  - H1: resistance 1.65908 (0.94 ATR, 4 bar sentuh) · support 1.65579 (0.06 ATR, 21 bar sentuh)
  - M15: resistance 1.65674 (0.24 ATR, 12 bar sentuh) · support 1.65538 (0.82 ATR, 7 bar sentuh)
- **EUR/CAD** (NO TRADE)
  - H1: resistance 1.5612 (0.65 ATR, 3 bar sentuh) · support 1.56019 (0.02 ATR, 4 bar sentuh)
  - M15: resistance 1.56023 (0.25 ATR, 8 bar sentuh) · support tidak ada dalam jarak
- **EUR/NZD** (NO TRADE)
  - H1: resistance 2.0011 (0.14 ATR, 59 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance 2.00168 (0.59 ATR, 53 bar sentuh) · support tidak ada dalam jarak
- **XAU/USD** (NO TRADE)
  - H1: resistance 3608.91558 (1.08 ATR, 19 bar sentuh) · support 3540.21417 (1.08 ATR, 22 bar sentuh)
  - M15: resistance 3588.0315 (0.56 ATR, 6 bar sentuh) · support tidak ada dalam jarak
- **XAU/AUD** (NO TRADE)
  - H1: resistance 5416.917 (0.54 ATR, 9 bar sentuh) · support 5385.4644 (0.17 ATR, 24 bar sentuh)
  - M15: resistance 5411.9015 (0.59 ATR, 6 bar sentuh) · support tidak ada dalam jarak

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

