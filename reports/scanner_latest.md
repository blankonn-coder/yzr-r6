# Laporan Scanner Adaptive Forex

- Waktu eksekusi: 2026-11-25T21:00:45Z
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
| EUR/USD | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.09758 | — | 168/180 | 2026-11-25T20:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |
| GBP/USD | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.31197 | — | 168/180 | 2026-11-25T20:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| USD/JPY | VOLATIL/CHOPPY | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 159.2295 | — | 168/180 | 2026-11-25T20:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime VOLATIL/CHOPPY belum punya metode prioritas di ranking |
| USD/CHF | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.83095 | — | 168/180 | 2026-11-25T20:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| AUD/USD | MIXED | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.66278 | — | 168/180 | 2026-11-25T20:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime MIXED belum punya metode prioritas di ranking |
| USD/CAD | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.42108 | — | 168/180 | 2026-11-25T20:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| NZD/USD | MIXED | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.5488 | — | 168/180 | 2026-11-25T20:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime MIXED belum punya metode prioritas di ranking |
| EUR/GBP | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.83661 | — | 168/180 | 2026-11-25T20:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| EUR/JPY | VOLATIL/CHOPPY | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 174.7655 | — | 168/180 | 2026-11-25T20:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime VOLATIL/CHOPPY belum punya metode prioritas di ranking |
| EUR/CHF | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.91204 | — | 168/180 | 2026-11-25T20:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| EUR/AUD | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.65599 | — | 168/180 | 2026-11-25T20:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| EUR/CAD | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.55974 | — | 168/180 | 2026-11-25T20:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| EUR/NZD | VOLATIL/CHOPPY | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 2.00014 | — | 168/180 | 2026-11-25T20:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime VOLATIL/CHOPPY belum punya metode prioritas di ranking |
| XAU/USD | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 3574.4535 | — | 168/180 | 2026-11-25T20:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| XAU/AUD | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 5393.032 | — | 168/180 | 2026-11-25T20:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |

## Saran analisa cadangan (BUKAN sinyal, tidak divalidasi backtest)
Dari lead-lag, maks 3 pair: leader bergerak, follower tertinggal 5-60 menit. BUY/SELL mengikuti arah leader. SL 0.5 ATR H1, TP 1.5R. Tanpa cek spread, news, atau batas risiko §9. Tidak mengubah label.
| Pair | Arah | Dasar | Entry | SL | TP | Risiko SL |
|---|---|---|---|---|---|---|
| EUR/GBP | **SELL** | LEAD-LAG: GBP/NZD memimpin 50 mnt, korelasi 0.62, n 22 | 0.83661 | 0.83696 | 0.83609 | 3.5 pip |
| EUR/AUD | **BUY** | LEAD-LAG: GBP/CHF memimpin 20 mnt, korelasi 0.53, n 34 | 1.65599 | 1.65425 | 1.6586 | 17.4 pip |

## Lead-lag (backtest 6 jam, BUKAN sinyal)
- Status: dianalisa
- Pair gagal diambil (M5): tidak ada
- Backtest jendela 360 menit, diperbarui 2026-11-25T21:00:45Z, pasangan lolos 15.

Pasangan lolos (10 teratas, urut |korelasi|):

| Leader | Follower | Lag (menit) | Korelasi | Korelasi lag 0 | n |
|---|---|---|---|---|---|
| GBP/NZD | GBP/JPY | 30 | 0.647 | -0.269 | 30 |
| GBP/JPY | USD/CAD | 50 | 0.642 | -0.482 | 22 |
| GBP/NZD | EUR/GBP | 50 | 0.617 | -0.3 | 22 |
| NZD/CAD | GBP/CHF | 30 | -0.598 | 0.129 | 30 |
| NZD/USD | AUD/CAD | 50 | 0.58 | 0.526 | 22 |
| EUR/CAD | GBP/CHF | 20 | 0.539 | 0.086 | 34 |
| GBP/CHF | EUR/AUD | 20 | 0.533 | -0.243 | 34 |
| GBP/CHF | NZD/USD | 30 | 0.53 | 0.042 | 30 |
| EUR/GBP | CAD/CHF | 15 | 0.52 | -0.094 | 36 |
| NZD/CAD | USD/JPY | 30 | -0.519 | -0.039 | 30 |

Kandidat (follower yang tertinggal, urut skor):

| Follower | Arah | Leader | Lag (menit) | z leader | Skor |
|---|---|---|---|---|---|
| USD/CAD | SELL | GBP/JPY | 50 | -0.3 | 0.642 |
| EUR/GBP | SELL | GBP/NZD | 50 | -0.17 | 0.617 |
| EUR/AUD | BUY | GBP/CHF | 20 | 0.17 | 0.533 |
| NZD/USD | BUY | GBP/CHF | 30 | 0.08 | 0.53 |
| USD/JPY | SELL | NZD/CAD | 30 | 0.15 | 0.519 |
| XAU/USD | BUY | CAD/JPY | 25 | -0.46 | 0.508 |

## Pemantauan 15 menit (entry dan analisa cadangan)
Nilai di kolom 15m-60m = pip dari entry pada close candle M15 ke-1 sampai ke-4. Jika SL dan TP kena di candle yang sama, dihitung SL. Analisa cadangan BUKAN sinyal.
| Sumber | Pair | Arah | Entry | SL | TP | 15m | 30m | 45m | 60m | Hasil | Pip sekarang | Umur |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LEAD-LAG (analisa cadangan, bukan sinyal) | EUR/CAD | SELL | 1.55934 | 1.56015 | 1.55812 | -1.4 | +2.9 | -4.0 | - | BERJALAN | LOSS 4.0 pip | 45 mnt |
| LEAD-LAG (analisa cadangan, bukan sinyal) | NZD/USD | BUY | 0.54905 | 0.54855 | 0.54981 | -1.4 | -2.5 | - | - | BERJALAN | LOSS 2.5 pip | 30 mnt |
| LEAD-LAG (analisa cadangan, bukan sinyal) | USD/CAD | BUY | 1.4203 | 1.41945 | 1.42157 | +0.3 | +7.8 | - | - | BERJALAN | PROFIT 7.8 pip | 30 mnt |
| LEAD-LAG (analisa cadangan, bukan sinyal) | EUR/JPY | SELL | 174.7655 | 174.89878 | 174.56559 | +0.0 | - | - | - | BERJALAN | PROFIT 0.0 pip | 15 mnt |
| LEAD-LAG (analisa cadangan, bukan sinyal) | XAU/AUD | BUY | 5388.6845 | 5367.43126 | 5420.56436 | +43.5 | - | - | - | BERJALAN | PROFIT 43.5 pip | 15 mnt |

## Evaluasi 1 jam (entry dan analisa cadangan)
Dibuat setelah 60 menit atau saat SL/TP kena. MFE = gerak terbaik, MAE = gerak terburuk, dalam pip.
Belum ada evaluasi yang selesai di run ini.

## Level analisa cadangan (BUKAN sinyal, tanpa statistik)
Level S/R terdekat untuk konteks scalping. Tidak mengubah label atau keputusan apa pun.
- **EUR/USD** (NO TRADE)
  - H1: resistance 1.09901 (1.12 ATR, 31 bar sentuh) · support 1.09609 (1.17 ATR, 32 bar sentuh)
  - M15: resistance 1.09803 (0.58 ATR, 6 bar sentuh) · support 1.09748 (0.13 ATR, 11 bar sentuh)
- **GBP/USD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 1.3094 (1.46 ATR, 31 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 1.31153 (0.43 ATR, 40 bar sentuh)
- **USD/JPY** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 159.20814 (0.1 ATR, 68 bar sentuh)
  - M15: resistance 159.23395 (0.04 ATR, 75 bar sentuh) · support tidak ada dalam jarak
- **USD/CHF** (NO TRADE)
  - H1: resistance 0.83234 (0.91 ATR, 5 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance 0.83159 (0.73 ATR, 13 bar sentuh) · support 0.8308 (0.18 ATR, 15 bar sentuh)
- **AUD/USD** (NO TRADE)
  - H1: resistance 0.66443 (1.09 ATR, 29 bar sentuh) · support 0.661 (1.18 ATR, 8 bar sentuh)
  - M15: resistance 0.66323 (0.54 ATR, 46 bar sentuh) · support tidak ada dalam jarak
- **USD/CAD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support tidak ada dalam jarak
  - M15: resistance tidak ada dalam jarak · support tidak ada dalam jarak
- **NZD/USD** (NO TRADE)
  - H1: resistance 0.54924 (0.46 ATR, 60 bar sentuh) · support 0.54756 (1.29 ATR, 23 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 0.54857 (0.43 ATR, 19 bar sentuh)
- **EUR/GBP** (NO TRADE)
  - H1: resistance 0.83698 (0.52 ATR, 34 bar sentuh) · support 0.83594 (0.97 ATR, 25 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 0.83651 (0.27 ATR, 53 bar sentuh)
- **EUR/JPY** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 174.69318 (0.28 ATR, 37 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support tidak ada dalam jarak
- **EUR/CHF** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support tidak ada dalam jarak
  - M15: resistance 0.91231 (0.36 ATR, 9 bar sentuh) · support tidak ada dalam jarak
- **EUR/AUD** (NO TRADE)
  - H1: resistance 1.65908 (0.89 ATR, 5 bar sentuh) · support 1.65579 (0.06 ATR, 20 bar sentuh)
  - M15: resistance 1.65743 (0.73 ATR, 5 bar sentuh) · support 1.65543 (0.29 ATR, 8 bar sentuh)
- **EUR/CAD** (NO TRADE)
  - H1: resistance 1.56019 (0.28 ATR, 3 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance 1.56019 (0.46 ATR, 3 bar sentuh) · support 1.55906 (0.69 ATR, 15 bar sentuh)
- **EUR/NZD** (NO TRADE)
  - H1: resistance 2.0011 (0.35 ATR, 59 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance tidak ada dalam jarak · support tidak ada dalam jarak
- **XAU/USD** (NO TRADE)
  - H1: resistance 3608.91558 (1.08 ATR, 19 bar sentuh) · support 3540.21417 (1.08 ATR, 22 bar sentuh)
  - M15: resistance 3588.0315 (0.66 ATR, 5 bar sentuh) · support tidak ada dalam jarak
- **XAU/AUD** (NO TRADE)
  - H1: resistance 5416.917 (0.54 ATR, 9 bar sentuh) · support 5385.4644 (0.17 ATR, 24 bar sentuh)
  - M15: resistance 5411.9015 (0.7 ATR, 5 bar sentuh) · support 5367.32342 (0.96 ATR, 44 bar sentuh)

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

