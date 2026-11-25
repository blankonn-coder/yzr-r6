# Laporan Scanner Adaptive Forex

- Waktu eksekusi: 2026-11-25T22:30:34Z
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
| USD/JPY | **SELL** | LEAD-LAG: GBP/NZD memimpin 20 mnt, korelasi -0.67, n 32 | 159.1435 | 159.25001 | 158.98374 | 10.7 pip |
| EUR/GBP | **SELL** | LEAD-LAG: GBP/AUD memimpin 10 mnt, korelasi 0.65, n 36 | 0.83684 | 0.83717 | 0.83634 | 3.3 pip |

## Lead-lag (backtest 6 jam, BUKAN sinyal)
- Status: dianalisa
- Pair gagal diambil (M5): tidak ada
- Backtest jendela 360 menit, diperbarui 2026-11-25T22:30:34Z, pasangan lolos 25.

Pasangan lolos (10 teratas, urut |korelasi|):

| Leader | Follower | Lag (menit) | Korelasi | Korelasi lag 0 | n |
|---|---|---|---|---|---|
| NZD/USD | EUR/JPY | 5 | 0.768 | 0.563 | 40 |
| GBP/NZD | USD/JPY | 20 | -0.673 | -0.444 | 32 |
| EUR/GBP | USD/JPY | 10 | -0.647 | -0.298 | 34 |
| GBP/AUD | EUR/GBP | 10 | 0.645 | 0.283 | 36 |
| GBP/NZD | USD/CHF | 25 | -0.642 | -0.246 | 30 |
| GBP/CAD | EUR/GBP | 10 | 0.638 | 0.135 | 36 |
| GBP/CHF | AUD/CAD | 15 | 0.618 | 0.459 | 32 |
| GBP/JPY | EUR/CHF | 25 | -0.599 | 0.354 | 30 |
| EUR/USD | EUR/CHF | 20 | 0.593 | 0.246 | 32 |
| EUR/JPY | EUR/CHF | 20 | 0.574 | 0.448 | 32 |

Kandidat (follower yang tertinggal, urut skor):

| Follower | Arah | Leader | Lag (menit) | z leader | Skor |
|---|---|---|---|---|---|
| EUR/JPY | SELL | NZD/USD | 5 | -0.3 | 0.768 |
| USD/JPY | SELL | GBP/NZD | 20 | 0.01 | 0.673 |
| EUR/GBP | SELL | GBP/AUD | 10 | -0.02 | 0.645 |
| EUR/CHF | SELL | EUR/USD | 20 | -0.21 | 0.593 |
| EUR/USD | BUY | EUR/AUD | 10 | 0.02 | 0.566 |
| NZD/USD | BUY | USD/CHF | 20 | -0.08 | 0.544 |
| GBP/USD | BUY | GBP/AUD | 20 | 0.06 | 0.538 |

## Pemantauan 15 menit (entry dan analisa cadangan)
Nilai di kolom 15m-60m = pip dari entry pada close candle M15 ke-1 sampai ke-4. Jika SL dan TP kena di candle yang sama, dihitung SL. Analisa cadangan BUKAN sinyal.
| Sumber | Pair | Arah | Entry | SL | TP | 15m | 30m | 45m | 60m | Hasil | Pip sekarang | Umur |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LEAD-LAG (analisa cadangan, bukan sinyal) | EUR/USD | BUY | 1.09745 | 1.09682 | 1.0984 | +0.6 | +1.5 | +1.9 | +0.8 | Selesai 60 menit | PROFIT 0.8 pip | 60 mnt |
| LEAD-LAG (analisa cadangan, bukan sinyal) | USD/CHF | SELL | 0.83095 | 0.8317 | 0.82981 | +0.4 | +1.0 | +1.5 | - | BERJALAN | PROFIT 1.5 pip | 45 mnt |
| LEAD-LAG (analisa cadangan, bukan sinyal) | AUD/USD | BUY | 0.66275 | 0.66204 | 0.66382 | -1.4 | -1.7 | - | - | BERJALAN | LOSS 1.7 pip | 30 mnt |
| LEAD-LAG (analisa cadangan, bukan sinyal) | EUR/CAD | SELL | 1.56021 | 1.56098 | 1.55907 | +1.7 | +3.1 | - | - | BERJALAN | PROFIT 3.1 pip | 30 mnt |
| LEAD-LAG (analisa cadangan, bukan sinyal) | EUR/JPY | BUY | 174.63 | 174.50731 | 174.81403 | +7.6 | - | - | - | BERJALAN | PROFIT 7.6 pip | 15 mnt |

## Evaluasi 1 jam (entry dan analisa cadangan)
Dibuat setelah 60 menit atau saat SL/TP kena. MFE = gerak terbaik, MAE = gerak terburuk, dalam pip.
| Sumber | Pair | Arah | 15m | 30m | 45m | 60m | Hasil | Pip akhir | MFE (pip) | MAE (pip) | Ditutup (UTC) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| LEAD-LAG (analisa cadangan, bukan sinyal) | EUR/USD | BUY | +0.6 | +1.5 | +1.9 | +0.8 | Selesai 60 menit | PROFIT 0.8 pip | 2.2 | -0.3 | 2026-11-25T22:30:34Z |

## Level analisa cadangan (BUKAN sinyal, tanpa statistik)
Level S/R terdekat untuk konteks scalping. Tidak mengubah label atau keputusan apa pun.
- **EUR/USD** (NO TRADE)
  - H1: resistance 1.09897 (1.13 ATR, 31 bar sentuh) · support 1.09609 (1.26 ATR, 30 bar sentuh)
  - M15: resistance 1.09803 (0.91 ATR, 5 bar sentuh) · support 1.09746 (0.12 ATR, 17 bar sentuh)
- **GBP/USD** (NO TRADE)
  - H1: resistance 1.31401 (1.39 ATR, 12 bar sentuh) · support 1.3094 (1.36 ATR, 29 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 1.31144 (0.05 ATR, 44 bar sentuh)
- **USD/JPY** (NO TRADE)
  - H1: resistance 159.20814 (0.3 ATR, 69 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance 159.20613 (0.68 ATR, 66 bar sentuh) · support tidak ada dalam jarak
- **USD/CHF** (NO TRADE)
  - H1: resistance 0.83234 (1.0 ATR, 4 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance tidak ada dalam jarak · support 0.83078 (0.04 ATR, 21 bar sentuh)
- **AUD/USD** (NO TRADE)
  - H1: resistance 0.66298 (0.16 ATR, 38 bar sentuh) · support 0.661 (1.24 ATR, 8 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support tidak ada dalam jarak
- **USD/CAD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 1.41948 (1.29 ATR, 1 bar sentuh)
  - M15: resistance 1.42179 (0.55 ATR, 4 bar sentuh) · support tidak ada dalam jarak
- **NZD/USD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 0.54865 (0.02 ATR, 33 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 0.54857 (0.04 ATR, 19 bar sentuh)
- **EUR/GBP** (NO TRADE)
  - H1: resistance 0.83698 (0.28 ATR, 33 bar sentuh) · support 0.83661 (0.27 ATR, 41 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support tidak ada dalam jarak
- **EUR/JPY** (NO TRADE)
  - H1: resistance 174.70071 (0.23 ATR, 37 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance 174.7595 (0.48 ATR, 12 bar sentuh) · support tidak ada dalam jarak
- **EUR/CHF** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support tidak ada dalam jarak
  - M15: resistance 0.91204 (0.23 ATR, 14 bar sentuh) · support tidak ada dalam jarak
- **EUR/AUD** (NO TRADE)
  - H1: resistance 1.65908 (0.94 ATR, 4 bar sentuh) · support 1.65579 (0.06 ATR, 21 bar sentuh)
  - M15: resistance 1.65674 (0.31 ATR, 11 bar sentuh) · support 1.65538 (0.69 ATR, 7 bar sentuh)
- **EUR/CAD** (NO TRADE)
  - H1: resistance 1.5612 (0.65 ATR, 3 bar sentuh) · support 1.56019 (0.02 ATR, 4 bar sentuh)
  - M15: resistance 1.56023 (0.43 ATR, 8 bar sentuh) · support tidak ada dalam jarak
- **EUR/NZD** (NO TRADE)
  - H1: resistance 2.0011 (0.14 ATR, 59 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance 2.00169 (0.57 ATR, 55 bar sentuh) · support tidak ada dalam jarak
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

