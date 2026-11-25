# Laporan Scanner Adaptive Forex

- Waktu eksekusi: 2026-11-25T02:00:41Z
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
| EUR/USD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.09584 | — | 168/180 | 2026-11-25T01:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| GBP/USD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.31068 | — | 168/180 | 2026-11-25T01:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| USD/JPY | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 159.2705 | — | 168/180 | 2026-11-25T01:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |
| USD/CHF | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.83591 | — | 168/180 | 2026-11-25T01:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| AUD/USD | VOLATIL/CHOPPY | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.66366 | — | 168/180 | 2026-11-25T01:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime VOLATIL/CHOPPY belum punya metode prioritas di ranking |
| USD/CAD | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.42694 | — | 168/180 | 2026-11-25T01:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| NZD/USD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.54736 | — | 168/180 | 2026-11-25T01:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| EUR/GBP | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.83608 | — | 168/180 | 2026-11-25T01:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| EUR/JPY | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 174.5305 | — | 168/180 | 2026-11-25T01:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| EUR/CHF | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.91602 | — | 168/180 | 2026-11-25T01:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| EUR/AUD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.65121 | — | 168/180 | 2026-11-25T01:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| EUR/CAD | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.56368 | — | 168/180 | 2026-11-25T01:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| EUR/NZD | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 2.00197 | — | 168/180 | 2026-11-25T01:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |
| XAU/USD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 3546.5435 | — | 168/180 | 2026-11-25T01:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| XAU/AUD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 5343.926 | — | 168/180 | 2026-11-25T01:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |

## Saran analisa cadangan (BUKAN sinyal, tidak divalidasi backtest)
Dari lead-lag, maks 3 pair: leader bergerak, follower tertinggal 5-60 menit. BUY/SELL mengikuti arah leader. SL 0.5 ATR H1, TP 1.5R. Tanpa cek spread, news, atau batas risiko §9. Tidak mengubah label.
Tidak ada saran (tidak ada level H1 dalam jarak 1.0 ATR, dan tidak ada kandidat lead-lag).

## Lead-lag (backtest 6 jam, BUKAN sinyal)
- Status: dianalisa
- Pair gagal diambil (M5): tidak ada
- Backtest jendela 360 menit, diperbarui 2026-11-25T02:00:41Z, pasangan lolos 0.

Tidak ada pasangan yang lolos ambang.

Tidak ada kandidat di run ini.

## Pemantauan 15 menit (entry dan analisa cadangan)
Nilai di kolom 15m-60m = pip dari entry pada close candle M15 ke-1 sampai ke-4. Jika SL dan TP kena di candle yang sama, dihitung SL. Analisa cadangan BUKAN sinyal.
| Sumber | Pair | Arah | Entry | SL | TP | 15m | 30m | 45m | 60m | Hasil | Pip sekarang | Umur |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LEAD-LAG (analisa cadangan, bukan sinyal) | EUR/CHF | SELL | 0.91626 | 0.91667 | 0.91564 | -0.4 | -0.8 | +0.5 | +2.4 | Selesai 60 menit | PROFIT 2.4 pip | 60 mnt |
| LEAD-LAG (analisa cadangan, bukan sinyal) | XAU/AUD | BUY | 5333.3955 | 5320.20694 | 5353.17834 | +149.6 | - | - | - | TP kena | PROFIT 197.8 pip | 30 mnt |
| LEAD-LAG (analisa cadangan, bukan sinyal) | EUR/JPY | SELL | 174.5325 | 174.63016 | 174.38601 | -3.7 | +0.2 | - | - | BERJALAN | PROFIT 0.2 pip | 30 mnt |

## Evaluasi 1 jam (entry dan analisa cadangan)
Dibuat setelah 60 menit atau saat SL/TP kena. MFE = gerak terbaik, MAE = gerak terburuk, dalam pip.
| Sumber | Pair | Arah | 15m | 30m | 45m | 60m | Hasil | Pip akhir | MFE (pip) | MAE (pip) | Ditutup (UTC) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| LEAD-LAG (analisa cadangan, bukan sinyal) | EUR/CHF | SELL | -0.4 | -0.8 | +0.5 | +2.4 | Selesai 60 menit | PROFIT 2.4 pip | 3.6 | -1.8 | 2026-11-25T02:00:41Z |
| LEAD-LAG (analisa cadangan, bukan sinyal) | XAU/AUD | BUY | +149.6 | - | - | - | TP kena · menit 30 | PROFIT 197.8 pip | 219.5 | -110.0 | 2026-11-25T02:00:41Z |

## Level analisa cadangan (BUKAN sinyal, tanpa statistik)
Level S/R terdekat untuk konteks scalping. Tidak mengubah label atau keputusan apa pun.
- **EUR/USD** (NO TRADE)
  - H1: resistance 1.09594 (0.1 ATR, 19 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance 1.09588 (0.11 ATR, 17 bar sentuh) · support tidak ada dalam jarak
- **GBP/USD** (NO TRADE)
  - H1: resistance 1.31116 (0.43 ATR, 32 bar sentuh) · support 1.31042 (0.23 ATR, 29 bar sentuh)
  - M15: resistance 1.31092 (0.55 ATR, 29 bar sentuh) · support 1.31051 (0.36 ATR, 21 bar sentuh)
- **USD/JPY** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 159.25153 (0.12 ATR, 61 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 159.254 (0.23 ATR, 57 bar sentuh)
- **USD/CHF** (NO TRADE)
  - H1: resistance 0.83669 (0.82 ATR, 3 bar sentuh) · support 0.835 (0.95 ATR, 5 bar sentuh)
  - M15: resistance 0.83598 (0.16 ATR, 18 bar sentuh) · support tidak ada dalam jarak
- **AUD/USD** (NO TRADE)
  - H1: resistance 0.66545 (1.39 ATR, 21 bar sentuh) · support 0.66295 (0.55 ATR, 32 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 0.66333 (0.49 ATR, 48 bar sentuh)
- **USD/CAD** (NO TRADE)
  - H1: resistance 1.42709 (0.13 ATR, 12 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance 1.42738 (0.92 ATR, 11 bar sentuh) · support 1.42668 (0.52 ATR, 15 bar sentuh)
- **NZD/USD** (NO TRADE)
  - H1: resistance 0.54756 (0.28 ATR, 21 bar sentuh) · support 0.54628 (1.49 ATR, 6 bar sentuh)
  - M15: resistance 0.54742 (0.19 ATR, 24 bar sentuh) · support 0.54704 (0.95 ATR, 23 bar sentuh)
- **EUR/GBP** (NO TRADE)
  - H1: resistance 0.83626 (0.43 ATR, 28 bar sentuh) · support 0.83592 (0.35 ATR, 13 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support tidak ada dalam jarak
- **EUR/JPY** (NO TRADE)
  - H1: resistance 174.7524 (1.16 ATR, 33 bar sentuh) · support 174.51236 (0.1 ATR, 26 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 174.50423 (0.34 ATR, 21 bar sentuh)
- **EUR/CHF** (NO TRADE)
  - H1: resistance 0.91665 (0.8 ATR, 5 bar sentuh) · support 0.91569 (0.41 ATR, 4 bar sentuh)
  - M15: resistance 0.91607 (0.18 ATR, 21 bar sentuh) · support 0.91581 (0.71 ATR, 9 bar sentuh)
- **EUR/AUD** (NO TRADE)
  - H1: resistance 1.65267 (0.49 ATR, 20 bar sentuh) · support 1.64955 (0.56 ATR, 20 bar sentuh)
  - M15: resistance 1.65273 (0.92 ATR, 24 bar sentuh) · support tidak ada dalam jarak
- **EUR/CAD** (NO TRADE)
  - H1: resistance 1.56437 (0.5 ATR, 8 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance tidak ada dalam jarak · support 1.56324 (0.94 ATR, 2 bar sentuh)
- **EUR/NZD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 2.00084 (0.53 ATR, 53 bar sentuh)
  - M15: resistance 2.00243 (0.45 ATR, 54 bar sentuh) · support tidak ada dalam jarak
- **XAU/USD** (NO TRADE)
  - H1: resistance 3546.6735 (0.01 ATR, 14 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance 3546.6735 (0.01 ATR, 10 bar sentuh) · support 3539.8395 (0.62 ATR, 5 bar sentuh)
- **XAU/AUD** (NO TRADE)
  - H1: resistance 5377.10775 (1.23 ATR, 16 bar sentuh) · support 5341.0465 (0.11 ATR, 17 bar sentuh)
  - M15: resistance 5348.606 (0.32 ATR, 17 bar sentuh) · support 5341.0465 (0.19 ATR, 8 bar sentuh)

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

