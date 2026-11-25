# Laporan Scanner Adaptive Forex

- Waktu eksekusi: 2026-11-25T08:30:34Z
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
| EUR/USD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.09343 | — | 168/180 | 2026-11-25T07:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| GBP/USD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.30689 | — | 168/180 | 2026-11-25T07:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| USD/JPY | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 159.2235 | — | 168/180 | 2026-11-25T07:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |
| USD/CHF | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.8352 | — | 168/180 | 2026-11-25T07:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| AUD/USD | VOLATIL/CHOPPY | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.65639 | — | 168/180 | 2026-11-25T07:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime VOLATIL/CHOPPY belum punya metode prioritas di ranking |
| USD/CAD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.42938 | — | 168/180 | 2026-11-25T07:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| NZD/USD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.54504 | — | 168/180 | 2026-11-25T07:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| EUR/GBP | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.83669 | — | 168/180 | 2026-11-25T07:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| EUR/JPY | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 174.1005 | — | 168/180 | 2026-11-25T07:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| EUR/CHF | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.91324 | — | 168/180 | 2026-11-25T07:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| EUR/AUD | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.66587 | — | 168/180 | 2026-11-25T07:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| EUR/CAD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.56296 | — | 168/180 | 2026-11-25T07:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| EUR/NZD | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 2.00617 | — | 168/180 | 2026-11-25T07:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |
| XAU/USD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 3523.6035 | — | 168/180 | 2026-11-25T07:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| XAU/AUD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 5368.1025 | — | 168/180 | 2026-11-25T07:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |

## Saran analisa cadangan (BUKAN sinyal, tidak divalidasi backtest)
Dari lead-lag, maks 3 pair: leader bergerak, follower tertinggal 5-60 menit. BUY/SELL mengikuti arah leader. SL 0.5 ATR H1, TP 1.5R. Tanpa cek spread, news, atau batas risiko §9. Tidak mengubah label.
Tidak ada saran (tidak ada level H1 dalam jarak 1.0 ATR, dan tidak ada kandidat lead-lag).

## Lead-lag (backtest 6 jam, BUKAN sinyal)
- Status: dianalisa
- Pair gagal diambil (M5): tidak ada
- Backtest jendela 360 menit, diperbarui 2026-11-25T08:30:34Z, pasangan lolos 0.

Tidak ada pasangan yang lolos ambang.

Tidak ada kandidat di run ini.

## Pemantauan 15 menit (entry dan analisa cadangan)
Nilai di kolom 15m-60m = pip dari entry pada close candle M15 ke-1 sampai ke-4. Jika SL dan TP kena di candle yang sama, dihitung SL. Analisa cadangan BUKAN sinyal.
Tidak ada entry atau saran yang sedang dipantau.

## Evaluasi 1 jam (entry dan analisa cadangan)
Dibuat setelah 60 menit atau saat SL/TP kena. MFE = gerak terbaik, MAE = gerak terburuk, dalam pip.
Belum ada evaluasi yang selesai di run ini.

## Level analisa cadangan (BUKAN sinyal, tanpa statistik)
Level S/R terdekat untuk konteks scalping. Tidak mengubah label atau keputusan apa pun.
- **EUR/USD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 1.09208 (1.42 ATR, 5 bar sentuh)
  - M15: resistance 1.09429 (0.82 ATR, 13 bar sentuh) · support 1.09371 (0.19 ATR, 22 bar sentuh)
- **GBP/USD** (NO TRADE)
  - H1: resistance 1.30783 (0.83 ATR, 9 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance 1.308 (0.71 ATR, 16 bar sentuh) · support 1.30689 (0.87 ATR, 16 bar sentuh)
- **USD/JPY** (NO TRADE)
  - H1: resistance 159.25371 (0.17 ATR, 68 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance 159.4145 (0.15 ATR, 16 bar sentuh) · support tidak ada dalam jarak
- **USD/CHF** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 0.83503 (0.18 ATR, 7 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 0.83552 (0.4 ATR, 35 bar sentuh)
- **AUD/USD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support tidak ada dalam jarak
  - M15: resistance tidak ada dalam jarak · support tidak ada dalam jarak
- **USD/CAD** (NO TRADE)
  - H1: resistance 1.43034 (0.87 ATR, 38 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance 1.42895 (0.46 ATR, 6 bar sentuh) · support tidak ada dalam jarak
- **NZD/USD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 0.54451 (0.66 ATR, 13 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 0.54567 (0.22 ATR, 20 bar sentuh)
- **EUR/GBP** (NO TRADE)
  - H1: resistance 0.83698 (0.71 ATR, 24 bar sentuh) · support 0.83661 (0.17 ATR, 32 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 0.83651 (0.3 ATR, 54 bar sentuh)
- **EUR/JPY** (NO TRADE)
  - H1: resistance 174.2705 (0.8 ATR, 21 bar sentuh) · support 174.0085 (0.43 ATR, 13 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 174.28875 (0.5 ATR, 24 bar sentuh)
- **EUR/CHF** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support tidak ada dalam jarak
  - M15: resistance tidak ada dalam jarak · support tidak ada dalam jarak
- **EUR/AUD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support tidak ada dalam jarak
  - M15: resistance tidak ada dalam jarak · support tidak ada dalam jarak
- **EUR/CAD** (NO TRADE)
  - H1: resistance 1.56452 (1.22 ATR, 9 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance 1.56279 (0.06 ATR, 11 bar sentuh) · support tidak ada dalam jarak
- **EUR/NZD** (NO TRADE)
  - H1: resistance 2.00637 (0.09 ATR, 17 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance tidak ada dalam jarak · support tidak ada dalam jarak
- **XAU/USD** (NO TRADE)
  - H1: resistance 3533.6145 (0.51 ATR, 15 bar sentuh) · support 3514.546 (0.46 ATR, 8 bar sentuh)
  - M15: resistance 3533.6145 (0.14 ATR, 6 bar sentuh) · support tidak ada dalam jarak
- **XAU/AUD** (NO TRADE)
  - H1: resistance 5385.145 (0.6 ATR, 16 bar sentuh) · support 5341.0465 (0.95 ATR, 21 bar sentuh)
  - M15: resistance 5377.0385 (0.26 ATR, 23 bar sentuh) · support 5363.2716 (0.75 ATR, 24 bar sentuh)

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

