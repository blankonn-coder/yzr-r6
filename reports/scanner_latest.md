# Laporan Scanner Adaptive Forex

- Waktu eksekusi: 2026-11-25T04:00:39Z
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
| EUR/USD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.09454 | — | 168/180 | 2026-11-25T03:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| GBP/USD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.30913 | — | 168/180 | 2026-11-25T03:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| USD/JPY | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 159.2935 | — | 168/180 | 2026-11-25T03:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |
| USD/CHF | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.83661 | — | 168/180 | 2026-11-25T03:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| AUD/USD | MIXED | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.6606 | — | 168/180 | 2026-11-25T03:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime MIXED belum punya metode prioritas di ranking |
| USD/CAD | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.42759 | — | 168/180 | 2026-11-25T03:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| NZD/USD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.54655 | — | 168/180 | 2026-11-25T03:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| EUR/GBP | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.83608 | — | 168/180 | 2026-11-25T03:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| EUR/JPY | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 174.3535 | — | 168/180 | 2026-11-25T03:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| EUR/CHF | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.91568 | — | 168/180 | 2026-11-25T03:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| EUR/AUD | MIXED | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.65691 | — | 168/180 | 2026-11-25T03:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime MIXED belum punya metode prioritas di ranking |
| EUR/CAD | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.56255 | — | 168/180 | 2026-11-25T03:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| EUR/NZD | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 2.00264 | — | 168/180 | 2026-11-25T03:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |
| XAU/USD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 3548.0845 | — | 168/180 | 2026-11-25T03:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| XAU/AUD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 5371.333 | — | 168/180 | 2026-11-25T03:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |

## Saran analisa cadangan (BUKAN sinyal, tidak divalidasi backtest)
Dari lead-lag, maks 3 pair: leader bergerak, follower tertinggal 5-60 menit. BUY/SELL mengikuti arah leader. SL 0.5 ATR H1, TP 1.5R. Tanpa cek spread, news, atau batas risiko §9. Tidak mengubah label.
Tidak ada saran (tidak ada level H1 dalam jarak 1.0 ATR, dan tidak ada kandidat lead-lag).

## Lead-lag (backtest 6 jam, BUKAN sinyal)
- Status: dianalisa
- Pair gagal diambil (M5): tidak ada
- Backtest jendela 360 menit, diperbarui 2026-11-25T04:00:39Z, pasangan lolos 0.

Tidak ada pasangan yang lolos ambang.

Tidak ada kandidat di run ini.

## Pemantauan 15 menit (entry dan analisa cadangan)
Nilai di kolom 15m-60m = pip dari entry pada close candle M15 ke-1 sampai ke-4. Jika SL dan TP kena di candle yang sama, dihitung SL. Analisa cadangan BUKAN sinyal.
| Sumber | Pair | Arah | Entry | SL | TP | 15m | 30m | 45m | 60m | Hasil | Pip sekarang | Umur |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LEAD-LAG (analisa cadangan, bukan sinyal) | USD/CHF | BUY | 0.83581 | 0.83534 | 0.83653 | +4.6 | +2.9 | +6.8 | - | TP kena | PROFIT 7.2 pip | 60 mnt |
| LEAD-LAG (analisa cadangan, bukan sinyal) | EUR/GBP | BUY | 0.83625 | 0.83603 | 0.83656 | -2.0 | - | - | - | SL kena | LOSS 2.2 pip | 30 mnt |

## Evaluasi 1 jam (entry dan analisa cadangan)
Dibuat setelah 60 menit atau saat SL/TP kena. MFE = gerak terbaik, MAE = gerak terburuk, dalam pip.
| Sumber | Pair | Arah | 15m | 30m | 45m | 60m | Hasil | Pip akhir | MFE (pip) | MAE (pip) | Ditutup (UTC) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| LEAD-LAG (analisa cadangan, bukan sinyal) | USD/CHF | BUY | +4.6 | +2.9 | +6.8 | - | TP kena · menit 60 | PROFIT 7.2 pip | 8.2 | 0.0 | 2026-11-25T04:00:39Z |
| LEAD-LAG (analisa cadangan, bukan sinyal) | EUR/GBP | BUY | -2.0 | - | - | - | SL kena · menit 30 | LOSS 2.2 pip | 0.0 | -2.7 | 2026-11-25T04:00:39Z |

## Level analisa cadangan (BUKAN sinyal, tanpa statistik)
Level S/R terdekat untuk konteks scalping. Tidak mengubah label atau keputusan apa pun.
- **EUR/USD** (NO TRADE)
  - H1: resistance 1.09603 (1.49 ATR, 24 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance 1.09472 (0.41 ATR, 9 bar sentuh) · support tidak ada dalam jarak
- **GBP/USD** (NO TRADE)
  - H1: resistance 1.3094 (0.22 ATR, 22 bar sentuh) · support 1.30783 (1.12 ATR, 7 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 1.309 (0.27 ATR, 7 bar sentuh)
- **USD/JPY** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 159.25376 (0.24 ATR, 64 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support tidak ada dalam jarak
- **USD/CHF** (NO TRADE)
  - H1: resistance 0.83669 (0.1 ATR, 4 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance 0.83669 (0.23 ATR, 8 bar sentuh) · support 0.83647 (0.33 ATR, 11 bar sentuh)
- **AUD/USD** (NO TRADE)
  - H1: resistance 0.661 (0.29 ATR, 7 bar sentuh) · support 0.65977 (0.61 ATR, 1 bar sentuh)
  - M15: resistance 0.66108 (0.71 ATR, 8 bar sentuh) · support tidak ada dalam jarak
- **USD/CAD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 1.42735 (0.2 ATR, 13 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 1.42737 (0.45 ATR, 14 bar sentuh)
- **NZD/USD** (NO TRADE)
  - H1: resistance 0.54756 (1.31 ATR, 22 bar sentuh) · support 0.54628 (0.35 ATR, 6 bar sentuh)
  - M15: resistance 0.54668 (0.34 ATR, 19 bar sentuh) · support 0.54626 (0.77 ATR, 5 bar sentuh)
- **EUR/GBP** (NO TRADE)
  - H1: resistance 0.83626 (0.43 ATR, 28 bar sentuh) · support 0.83589 (0.47 ATR, 12 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support tidak ada dalam jarak
- **EUR/JPY** (NO TRADE)
  - H1: resistance 174.51236 (0.8 ATR, 28 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance tidak ada dalam jarak · support 174.28117 (0.82 ATR, 14 bar sentuh)
- **EUR/CHF** (NO TRADE)
  - H1: resistance 0.91569 (0.01 ATR, 6 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance 0.91581 (0.44 ATR, 15 bar sentuh) · support tidak ada dalam jarak
- **EUR/AUD** (NO TRADE)
  - H1: resistance 1.65908 (0.7 ATR, 1 bar sentuh) · support 1.65579 (0.36 ATR, 17 bar sentuh)
  - M15: resistance 1.65743 (0.31 ATR, 2 bar sentuh) · support tidak ada dalam jarak
- **EUR/CAD** (NO TRADE)
  - H1: resistance 1.56452 (1.44 ATR, 10 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance 1.56285 (0.61 ATR, 3 bar sentuh) · support tidak ada dalam jarak
- **EUR/NZD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 2.00084 (0.77 ATR, 55 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 2.00256 (0.06 ATR, 60 bar sentuh)
- **XAU/USD** (NO TRADE)
  - H1: resistance 3569.0095 (1.07 ATR, 19 bar sentuh) · support 3546.6735 (0.07 ATR, 16 bar sentuh)
  - M15: resistance 3549.00917 (0.09 ATR, 19 bar sentuh) · support 3539.8395 (0.76 ATR, 5 bar sentuh)
- **XAU/AUD** (NO TRADE)
  - H1: resistance 5377.10775 (0.21 ATR, 18 bar sentuh) · support 5341.0465 (1.08 ATR, 18 bar sentuh)
  - M15: resistance 5376.8335 (0.38 ATR, 16 bar sentuh) · support 5364.74483 (0.45 ATR, 18 bar sentuh)

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

