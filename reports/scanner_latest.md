# Laporan Scanner Adaptive Forex

- Waktu eksekusi: 2026-11-25T21:15:24Z
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
| USD/CAD | **SELL** | LEAD-LAG: GBP/JPY memimpin 50 mnt, korelasi 0.53, n 22 | 1.4217 | 1.42253 | 1.42047 | 8.2 pip |

## Lead-lag (backtest 6 jam, BUKAN sinyal)
- Status: dianalisa
- Pair gagal diambil (M5): tidak ada
- Backtest jendela 360 menit, diperbarui 2026-11-25T21:15:24Z, pasangan lolos 16.

Pasangan lolos (10 teratas, urut |korelasi|):

| Leader | Follower | Lag (menit) | Korelasi | Korelasi lag 0 | n |
|---|---|---|---|---|---|
| GBP/NZD | GBP/JPY | 30 | 0.725 | -0.426 | 30 |
| GBP/AUD | EUR/JPY | 30 | 0.618 | -0.374 | 30 |
| NZD/USD | AUD/CAD | 50 | 0.576 | 0.566 | 22 |
| GBP/AUD | GBP/JPY | 30 | 0.574 | -0.466 | 30 |
| GBP/JPY | GBP/CAD | 50 | 0.568 | 0.289 | 22 |
| CAD/JPY | GBP/CAD | 50 | 0.561 | -0.5 | 22 |
| NZD/JPY | GBP/CAD | 50 | 0.543 | -0.005 | 22 |
| GBP/JPY | USD/CAD | 50 | 0.534 | -0.324 | 22 |
| GBP/CHF | EUR/NZD | 20 | 0.533 | -0.141 | 34 |
| GBP/CHF | EUR/AUD | 20 | 0.531 | -0.33 | 34 |

Kandidat (follower yang tertinggal, urut skor):

| Follower | Arah | Leader | Lag (menit) | z leader | Skor |
|---|---|---|---|---|---|
| EUR/GBP | BUY | USD/CAD | 50 | 1.24 | 0.648 |
| EUR/JPY | SELL | GBP/AUD | 30 | -0.37 | 0.618 |
| USD/CAD | SELL | GBP/JPY | 50 | -0.62 | 0.534 |
| EUR/NZD | SELL | GBP/CHF | 20 | -0.08 | 0.533 |
| EUR/AUD | SELL | GBP/CHF | 20 | -0.08 | 0.531 |
| AUD/USD | BUY | USD/JPY | 20 | -0.05 | 0.52 |

## Pemantauan 15 menit (entry dan analisa cadangan)
Nilai di kolom 15m-60m = pip dari entry pada close candle M15 ke-1 sampai ke-4. Jika SL dan TP kena di candle yang sama, dihitung SL. Analisa cadangan BUKAN sinyal.
| Sumber | Pair | Arah | Entry | SL | TP | 15m | 30m | 45m | 60m | Hasil | Pip sekarang | Umur |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LEAD-LAG (analisa cadangan, bukan sinyal) | EUR/CAD | SELL | 1.55934 | 1.56015 | 1.55812 | -1.4 | +2.9 | -4.0 | - | SL kena | LOSS 8.1 pip | 60 mnt |
| LEAD-LAG (analisa cadangan, bukan sinyal) | NZD/USD | BUY | 0.54905 | 0.54855 | 0.54981 | -1.4 | -2.5 | -3.5 | - | BERJALAN | LOSS 3.5 pip | 45 mnt |
| LEAD-LAG (analisa cadangan, bukan sinyal) | USD/CAD | BUY | 1.4203 | 1.41945 | 1.42157 | +0.3 | +7.8 | - | - | TP kena | PROFIT 12.7 pip | 45 mnt |
| LEAD-LAG (analisa cadangan, bukan sinyal) | EUR/JPY | SELL | 174.7655 | 174.89878 | 174.56559 | +0.0 | +2.3 | - | - | BERJALAN | PROFIT 2.3 pip | 30 mnt |
| LEAD-LAG (analisa cadangan, bukan sinyal) | XAU/AUD | BUY | 5388.6845 | 5367.43126 | 5420.56436 | +43.5 | +3.8 | - | - | BERJALAN | PROFIT 3.8 pip | 30 mnt |
| LEAD-LAG (analisa cadangan, bukan sinyal) | EUR/GBP | SELL | 0.83661 | 0.83696 | 0.83609 | -0.8 | - | - | - | BERJALAN | LOSS 0.8 pip | 15 mnt |
| LEAD-LAG (analisa cadangan, bukan sinyal) | EUR/AUD | BUY | 1.65599 | 1.65425 | 1.6586 | -2.7 | - | - | - | BERJALAN | LOSS 2.7 pip | 15 mnt |

## Evaluasi 1 jam (entry dan analisa cadangan)
Dibuat setelah 60 menit atau saat SL/TP kena. MFE = gerak terbaik, MAE = gerak terburuk, dalam pip.
| Sumber | Pair | Arah | 15m | 30m | 45m | 60m | Hasil | Pip akhir | MFE (pip) | MAE (pip) | Ditutup (UTC) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| LEAD-LAG (analisa cadangan, bukan sinyal) | EUR/CAD | SELL | -1.4 | +2.9 | -4.0 | - | SL kena · menit 60 | LOSS 8.1 pip | 5.8 | -11.9 | 2026-11-25T21:15:24Z |
| LEAD-LAG (analisa cadangan, bukan sinyal) | USD/CAD | BUY | +0.3 | +7.8 | - | - | TP kena · menit 45 | PROFIT 12.7 pip | 14.9 | -2.1 | 2026-11-25T21:15:24Z |

## Level analisa cadangan (BUKAN sinyal, tanpa statistik)
Level S/R terdekat untuk konteks scalping. Tidak mengubah label atau keputusan apa pun.
- **EUR/USD** (NO TRADE)
  - H1: resistance 1.09901 (1.12 ATR, 31 bar sentuh) · support 1.09609 (1.17 ATR, 32 bar sentuh)
  - M15: resistance 1.09748 (0.03 ATR, 12 bar sentuh) · support tidak ada dalam jarak
- **GBP/USD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 1.3094 (1.46 ATR, 31 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 1.31153 (0.19 ATR, 41 bar sentuh)
- **USD/JPY** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 159.20814 (0.1 ATR, 68 bar sentuh)
  - M15: resistance 159.23395 (0.06 ATR, 75 bar sentuh) · support tidak ada dalam jarak
- **USD/CHF** (NO TRADE)
  - H1: resistance 0.83234 (0.91 ATR, 5 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance 0.83159 (0.69 ATR, 12 bar sentuh) · support 0.83072 (0.37 ATR, 16 bar sentuh)
- **AUD/USD** (NO TRADE)
  - H1: resistance 0.66443 (1.09 ATR, 29 bar sentuh) · support 0.661 (1.18 ATR, 8 bar sentuh)
  - M15: resistance 0.66323 (0.54 ATR, 46 bar sentuh) · support tidak ada dalam jarak
- **USD/CAD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support tidak ada dalam jarak
  - M15: resistance 1.42229 (0.59 ATR, 4 bar sentuh) · support tidak ada dalam jarak
- **NZD/USD** (NO TRADE)
  - H1: resistance 0.54924 (0.46 ATR, 60 bar sentuh) · support 0.54756 (1.29 ATR, 23 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 0.54857 (0.26 ATR, 20 bar sentuh)
- **EUR/GBP** (NO TRADE)
  - H1: resistance 0.83698 (0.52 ATR, 34 bar sentuh) · support 0.83594 (0.97 ATR, 25 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 0.83651 (0.47 ATR, 52 bar sentuh)
- **EUR/JPY** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 174.69318 (0.28 ATR, 37 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support tidak ada dalam jarak
- **EUR/CHF** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support tidak ada dalam jarak
  - M15: resistance 0.91231 (0.42 ATR, 9 bar sentuh) · support 0.91178 (0.31 ATR, 7 bar sentuh)
- **EUR/AUD** (NO TRADE)
  - H1: resistance 1.65908 (0.89 ATR, 5 bar sentuh) · support 1.65579 (0.06 ATR, 20 bar sentuh)
  - M15: resistance 1.65708 (0.73 ATR, 9 bar sentuh) · support 1.65543 (0.16 ATR, 9 bar sentuh)
- **EUR/CAD** (NO TRADE)
  - H1: resistance 1.56019 (0.28 ATR, 3 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance tidak ada dalam jarak · support 1.56019 (0.05 ATR, 4 bar sentuh)
- **EUR/NZD** (NO TRADE)
  - H1: resistance 2.0011 (0.35 ATR, 59 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance tidak ada dalam jarak · support tidak ada dalam jarak
- **XAU/USD** (NO TRADE)
  - H1: resistance 3608.91558 (1.08 ATR, 19 bar sentuh) · support 3540.21417 (1.08 ATR, 22 bar sentuh)
  - M15: resistance 3588.0315 (0.81 ATR, 5 bar sentuh) · support tidak ada dalam jarak
- **XAU/AUD** (NO TRADE)
  - H1: resistance 5416.917 (0.54 ATR, 9 bar sentuh) · support 5385.4644 (0.17 ATR, 24 bar sentuh)
  - M15: resistance 5411.9015 (0.88 ATR, 5 bar sentuh) · support 5367.32342 (0.84 ATR, 44 bar sentuh)

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

