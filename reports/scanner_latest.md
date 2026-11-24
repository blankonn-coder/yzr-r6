# Laporan Scanner Adaptive Forex

- Waktu eksekusi: 2026-11-24T22:30:35Z
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
| EUR/USD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.09657 | — | 168/180 | 2026-11-24T21:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| GBP/USD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.3115 | — | 168/180 | 2026-11-24T21:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| USD/JPY | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 159.2595 | — | 168/180 | 2026-11-24T21:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |
| USD/CHF | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.83564 | — | 168/180 | 2026-11-24T21:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| AUD/USD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.66405 | — | 168/180 | 2026-11-24T21:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| USD/CAD | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.42697 | — | 168/180 | 2026-11-24T21:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| NZD/USD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.54827 | — | 168/180 | 2026-11-24T21:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| EUR/GBP | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.8361 | — | 168/180 | 2026-11-24T21:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| EUR/JPY | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 174.6335 | — | 168/180 | 2026-11-24T21:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| EUR/CHF | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.91625 | — | 168/180 | 2026-11-24T21:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| EUR/AUD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.65131 | — | 168/180 | 2026-11-24T21:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| EUR/CAD | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.56459 | — | 168/180 | 2026-11-24T21:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| EUR/NZD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.99991 | — | 168/180 | 2026-11-24T21:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| XAU/USD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 3553.1065 | — | 168/180 | 2026-11-24T20:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| XAU/AUD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 5349.697 | — | 168/180 | 2026-11-24T20:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |

## Saran analisa cadangan (BUKAN sinyal, tidak divalidasi backtest)
Dari lead-lag, maks 3 pair: leader bergerak, follower tertinggal 5-60 menit. BUY/SELL mengikuti arah leader. SL 0.5 ATR H1, TP 1.5R. Tanpa cek spread, news, atau batas risiko §9. Tidak mengubah label.
| Pair | Arah | Dasar | Entry | SL | TP | Risiko SL |
|---|---|---|---|---|---|---|
| USD/CAD | **SELL** | LEAD-LAG: AUD/JPY memimpin 20 mnt, korelasi -0.53, n 67 | 1.42702 | 1.42769 | 1.42602 | 6.7 pip |

## Lead-lag (backtest 6 jam, BUKAN sinyal)
- Status: dianalisa
- Pair gagal diambil (M5): tidak ada
- Backtest jendela 360 menit, diperbarui 2026-11-24T22:30:35Z, pasangan lolos 2.

Pasangan lolos (10 teratas, urut |korelasi|):

| Leader | Follower | Lag (menit) | Korelasi | Korelasi lag 0 | n |
|---|---|---|---|---|---|
| AUD/JPY | USD/CAD | 20 | -0.534 | -0.49 | 67 |
| XAU/USD | NZD/CAD | 20 | -0.521 | 0.176 | 65 |

Kandidat (follower yang tertinggal, urut skor):

| Follower | Arah | Leader | Lag (menit) | z leader | Skor |
|---|---|---|---|---|---|
| USD/CAD | SELL | AUD/JPY | 20 | 0.2 | 0.534 |

## Pemantauan 15 menit (entry dan analisa cadangan)
Nilai di kolom 15m-60m = pip dari entry pada close candle M15 ke-1 sampai ke-4. Jika SL dan TP kena di candle yang sama, dihitung SL. Analisa cadangan BUKAN sinyal.
| Sumber | Pair | Arah | Entry | SL | TP | 15m | 30m | 45m | 60m | Hasil | Pip sekarang | Umur |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LEAD-LAG (analisa cadangan, bukan sinyal) | EUR/JPY | SELL | 174.6205 | 174.73324 | 174.45138 | -1.3 | +2.4 | -5.5 | - | BERJALAN | LOSS 5.5 pip | 45 mnt |

## Evaluasi 1 jam (entry dan analisa cadangan)
Dibuat setelah 60 menit atau saat SL/TP kena. MFE = gerak terbaik, MAE = gerak terburuk, dalam pip.
Belum ada evaluasi yang selesai di run ini.

## Level analisa cadangan (BUKAN sinyal, tanpa statistik)
Level S/R terdekat untuk konteks scalping. Tidak mengubah label atau keputusan apa pun.
- **EUR/USD** (NO TRADE)
  - H1: resistance 1.09682 (0.23 ATR, 49 bar sentuh) · support 1.09589 (0.61 ATR, 16 bar sentuh)
  - M15: resistance 1.09639 (0.03 ATR, 25 bar sentuh) · support tidak ada dalam jarak
- **GBP/USD** (NO TRADE)
  - H1: resistance 1.31282 (1.03 ATR, 9 bar sentuh) · support 1.31042 (0.83 ATR, 29 bar sentuh)
  - M15: resistance 1.31164 (0.86 ATR, 27 bar sentuh) · support tidak ada dalam jarak
- **USD/JPY** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 159.25344 (0.04 ATR, 59 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 159.28717 (0.33 ATR, 40 bar sentuh)
- **USD/CHF** (NO TRADE)
  - H1: resistance 0.83669 (1.0 ATR, 3 bar sentuh) · support 0.8344 (1.16 ATR, 1 bar sentuh)
  - M15: resistance 0.83591 (0.06 ATR, 11 bar sentuh) · support 0.83553 (0.91 ATR, 21 bar sentuh)
- **AUD/USD** (NO TRADE)
  - H1: resistance 0.66545 (1.27 ATR, 17 bar sentuh) · support 0.66332 (0.67 ATR, 30 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support tidak ada dalam jarak
- **USD/CAD** (NO TRADE)
  - H1: resistance 1.42701 (0.03 ATR, 12 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance 1.42742 (0.72 ATR, 6 bar sentuh) · support 1.42659 (0.77 ATR, 8 bar sentuh)
- **NZD/USD** (NO TRADE)
  - H1: resistance 0.54932 (1.37 ATR, 54 bar sentuh) · support 0.54756 (0.94 ATR, 18 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 0.54811 (0.23 ATR, 12 bar sentuh)
- **EUR/GBP** (NO TRADE)
  - H1: resistance 0.83661 (1.09 ATR, 31 bar sentuh) · support 0.83601 (0.19 ATR, 16 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support tidak ada dalam jarak
- **EUR/JPY** (NO TRADE)
  - H1: resistance 174.88706 (1.2 ATR, 34 bar sentuh) · support 174.505 (0.61 ATR, 24 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 174.651 (0.36 ATR, 21 bar sentuh)
- **EUR/CHF** (NO TRADE)
  - H1: resistance 0.91743 (1.32 ATR, 10 bar sentuh) · support 0.91556 (0.78 ATR, 1 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support tidak ada dalam jarak
- **EUR/AUD** (NO TRADE)
  - H1: resistance 1.65267 (0.55 ATR, 18 bar sentuh) · support 1.65045 (0.34 ATR, 20 bar sentuh)
  - M15: resistance 1.65177 (0.62 ATR, 31 bar sentuh) · support tidak ada dalam jarak
- **EUR/CAD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 1.56439 (0.13 ATR, 5 bar sentuh)
  - M15: resistance 1.56477 (0.24 ATR, 22 bar sentuh) · support tidak ada dalam jarak
- **EUR/NZD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 1.99917 (0.33 ATR, 52 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 1.99965 (0.69 ATR, 25 bar sentuh)
- **XAU/USD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support tidak ada dalam jarak
  - M15: resistance 3561.31917 (0.99 ATR, 12 bar sentuh) · support 3552.7495 (0.07 ATR, 9 bar sentuh)
- **XAU/AUD** (NO TRADE)
  - H1: resistance 5377.382 (1.07 ATR, 14 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance tidak ada dalam jarak · support 5348.606 (0.2 ATR, 10 bar sentuh)

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

