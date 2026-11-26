# Laporan Scanner Adaptive Forex

- Waktu eksekusi: 2026-11-26T11:30:32Z
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
| EUR/USD | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.09736 | — | 168/180 | 2026-11-26T10:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |
| GBP/USD | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.31113 | — | 168/180 | 2026-11-26T10:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |
| USD/JPY | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 159.2875 | — | 168/180 | 2026-11-26T10:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| USD/CHF | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.83313 | — | 168/180 | 2026-11-26T10:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| AUD/USD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.66297 | — | 168/180 | 2026-11-26T10:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| USD/CAD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.42258 | — | 168/180 | 2026-11-26T10:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| NZD/USD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.54795 | — | 168/180 | 2026-11-26T10:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| EUR/GBP | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.83696 | — | 168/180 | 2026-11-26T10:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| EUR/JPY | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 174.7985 | — | 168/180 | 2026-11-26T10:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |
| EUR/CHF | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.91426 | — | 168/180 | 2026-11-26T10:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| EUR/AUD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.65522 | — | 168/180 | 2026-11-26T10:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| EUR/CAD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.5609 | — | 168/180 | 2026-11-26T10:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| EUR/NZD | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 2.00264 | — | 168/180 | 2026-11-26T10:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |
| XAU/USD | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 3555.6725 | — | 168/180 | 2026-11-26T10:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |
| XAU/AUD | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 5363.535 | — | 168/180 | 2026-11-26T10:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |

## Saran analisa cadangan (BUKAN sinyal, tidak divalidasi backtest)
Dari lead-lag, maks 3 pair: leader bergerak, follower tertinggal 5-60 menit. BUY/SELL mengikuti arah leader. SL 0.5 ATR H1, TP 1.5R. Tanpa cek spread, news, atau batas risiko §9. Tidak mengubah label.
| Pair | Arah | Dasar | Entry | SL | TP | Risiko SL |
|---|---|---|---|---|---|---|
| EUR/USD | **SELL** | LEAD-LAG: CAD/JPY memimpin 40 mnt, korelasi 0.52, n 63 | 1.09702 | 1.09753 | 1.09626 | 5.1 pip |

## Lead-lag (backtest 6 jam, BUKAN sinyal)
- Status: dianalisa
- Pair gagal diambil (M5): tidak ada
- Backtest jendela 360 menit, diperbarui 2026-11-26T11:30:32Z, pasangan lolos 1.

Pasangan lolos (10 teratas, urut |korelasi|):

| Leader | Follower | Lag (menit) | Korelasi | Korelasi lag 0 | n |
|---|---|---|---|---|---|
| CAD/JPY | EUR/USD | 40 | 0.525 | 0.145 | 63 |

Kandidat (follower yang tertinggal, urut skor):

| Follower | Arah | Leader | Lag (menit) | z leader | Skor |
|---|---|---|---|---|---|
| EUR/USD | SELL | CAD/JPY | 40 | -0.35 | 0.525 |

## Pemantauan 15 menit (entry dan analisa cadangan)
Nilai di kolom 15m-60m = pip dari entry pada close candle M15 ke-1 sampai ke-4. Jika SL dan TP kena di candle yang sama, dihitung SL. Analisa cadangan BUKAN sinyal.
| Sumber | Pair | Arah | Entry | SL | TP | 15m | 30m | 45m | 60m | Hasil | Pip sekarang | Umur |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LEAD-LAG (analisa cadangan, bukan sinyal) | EUR/USD | SELL | 1.09726 | 1.09777 | 1.09649 | -3.3 | -1.0 | +0.0 | +2.4 | Selesai 60 menit | PROFIT 2.4 pip | 60 mnt |

## Evaluasi 1 jam (entry dan analisa cadangan)
Dibuat setelah 60 menit atau saat SL/TP kena. MFE = gerak terbaik, MAE = gerak terburuk, dalam pip.
| Sumber | Pair | Arah | 15m | 30m | 45m | 60m | Hasil | Pip akhir | MFE (pip) | MAE (pip) | Ditutup (UTC) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| LEAD-LAG (analisa cadangan, bukan sinyal) | EUR/USD | SELL | -3.3 | -1.0 | +0.0 | +2.4 | Selesai 60 menit | PROFIT 2.4 pip | 3.9 | -4.3 | 2026-11-26T11:30:32Z |

## Level analisa cadangan (BUKAN sinyal, tanpa statistik)
Level S/R terdekat untuk konteks scalping. Tidak mengubah label atau keputusan apa pun.
- **EUR/USD** (NO TRADE)
  - H1: resistance 1.09819 (0.82 ATR, 37 bar sentuh) · support 1.09606 (1.28 ATR, 31 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 1.09652 (0.91 ATR, 48 bar sentuh)
- **GBP/USD** (NO TRADE)
  - H1: resistance 1.31245 (1.04 ATR, 14 bar sentuh) · support 1.31042 (0.56 ATR, 41 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 1.30972 (0.24 ATR, 20 bar sentuh)
- **USD/JPY** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 159.19443 (0.59 ATR, 66 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 159.25914 (0.57 ATR, 72 bar sentuh)
- **USD/CHF** (NO TRADE)
  - H1: resistance 0.8344 (1.13 ATR, 6 bar sentuh) · support 0.83183 (1.15 ATR, 13 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support tidak ada dalam jarak
- **AUD/USD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 0.66293 (0.04 ATR, 44 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 0.66288 (0.16 ATR, 34 bar sentuh)
- **USD/CAD** (NO TRADE)
  - H1: resistance 1.4228 (0.19 ATR, 8 bar sentuh) · support 1.42176 (0.76 ATR, 11 bar sentuh)
  - M15: resistance 1.42335 (0.32 ATR, 15 bar sentuh) · support tidak ada dalam jarak
- **NZD/USD** (NO TRADE)
  - H1: resistance 0.54868 (1.02 ATR, 39 bar sentuh) · support 0.5476 (0.49 ATR, 25 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 0.54756 (0.72 ATR, 16 bar sentuh)
- **EUR/GBP** (NO TRADE)
  - H1: resistance 0.83767 (1.36 ATR, 40 bar sentuh) · support 0.83626 (1.37 ATR, 36 bar sentuh)
  - M15: resistance 0.83777 (0.88 ATR, 12 bar sentuh) · support tidak ada dalam jarak
- **EUR/JPY** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 174.65113 (0.71 ATR, 39 bar sentuh)
  - M15: resistance 174.8075 (0.63 ATR, 13 bar sentuh) · support tidak ada dalam jarak
- **EUR/CHF** (NO TRADE)
  - H1: resistance 0.91569 (1.44 ATR, 8 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance 0.91574 (0.72 ATR, 21 bar sentuh) · support 0.91501 (0.54 ATR, 9 bar sentuh)
- **EUR/AUD** (NO TRADE)
  - H1: resistance 1.65585 (0.22 ATR, 24 bar sentuh) · support 1.65267 (0.87 ATR, 28 bar sentuh)
  - M15: resistance 1.65571 (0.78 ATR, 22 bar sentuh) · support tidak ada dalam jarak
- **EUR/CAD** (NO TRADE)
  - H1: resistance 1.5612 (0.23 ATR, 6 bar sentuh) · support 1.56036 (0.42 ATR, 9 bar sentuh)
  - M15: resistance 1.56167 (0.96 ATR, 14 bar sentuh) · support tidak ada dalam jarak
- **EUR/NZD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 2.00082 (0.84 ATR, 54 bar sentuh)
  - M15: resistance 2.00324 (0.58 ATR, 29 bar sentuh) · support tidak ada dalam jarak
- **XAU/USD** (NO TRADE)
  - H1: resistance 3592.15665 (1.45 ATR, 18 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance 3568.8385 (0.26 ATR, 48 bar sentuh) · support tidak ada dalam jarak
- **XAU/AUD** (NO TRADE)
  - H1: resistance 5382.61517 (0.55 ATR, 37 bar sentuh) · support 5342.81517 (0.59 ATR, 29 bar sentuh)
  - M15: resistance 5388.9505 (0.71 ATR, 36 bar sentuh) · support tidak ada dalam jarak

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

