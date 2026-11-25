# Laporan Scanner Adaptive Forex

- Waktu eksekusi: 2026-11-25T05:15:24Z
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
| EUR/USD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.09452 | — | 168/180 | 2026-11-25T04:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| GBP/USD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.30892 | — | 168/180 | 2026-11-25T04:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| USD/JPY | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 159.3805 | — | 168/180 | 2026-11-25T04:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |
| USD/CHF | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.83634 | — | 168/180 | 2026-11-25T04:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| AUD/USD | MIXED | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.65942 | — | 168/180 | 2026-11-25T04:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime MIXED belum punya metode prioritas di ranking |
| USD/CAD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.42736 | — | 168/180 | 2026-11-25T04:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| NZD/USD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.54666 | — | 168/180 | 2026-11-25T04:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| EUR/GBP | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.8362 | — | 168/180 | 2026-11-25T04:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| EUR/JPY | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 174.4455 | — | 168/180 | 2026-11-25T04:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| EUR/CHF | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.91536 | — | 168/180 | 2026-11-25T04:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| EUR/AUD | MIXED | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.65985 | — | 168/180 | 2026-11-25T04:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime MIXED belum punya metode prioritas di ranking |
| EUR/CAD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.56227 | — | 168/180 | 2026-11-25T04:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| EUR/NZD | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 2.00217 | — | 168/180 | 2026-11-25T04:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |
| XAU/USD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 3549.2135 | — | 168/180 | 2026-11-25T04:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| XAU/AUD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 5382.8265 | — | 168/180 | 2026-11-25T04:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |

## Saran analisa cadangan (BUKAN sinyal, tidak divalidasi backtest)
Dari lead-lag, maks 3 pair: leader bergerak, follower tertinggal 5-60 menit. BUY/SELL mengikuti arah leader. SL 0.5 ATR H1, TP 1.5R. Tanpa cek spread, news, atau batas risiko §9. Tidak mengubah label.
Tidak ada saran (tidak ada level H1 dalam jarak 1.0 ATR, dan tidak ada kandidat lead-lag).

## Lead-lag (backtest 6 jam, BUKAN sinyal)
- Status: dianalisa
- Pair gagal diambil (M5): tidak ada
- Backtest jendela 360 menit, diperbarui 2026-11-25T05:15:24Z, pasangan lolos 0.

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
  - H1: resistance tidak ada dalam jarak · support tidak ada dalam jarak
  - M15: resistance 1.09474 (0.58 ATR, 12 bar sentuh) · support 1.09443 (0.21 ATR, 13 bar sentuh)
- **GBP/USD** (NO TRADE)
  - H1: resistance 1.3094 (0.41 ATR, 23 bar sentuh) · support 1.30783 (0.96 ATR, 7 bar sentuh)
  - M15: resistance 1.30913 (0.46 ATR, 11 bar sentuh) · support 1.30889 (0.07 ATR, 8 bar sentuh)
- **USD/JPY** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 159.25376 (0.79 ATR, 65 bar sentuh)
  - M15: resistance 159.4145 (0.18 ATR, 10 bar sentuh) · support tidak ada dalam jarak
- **USD/CHF** (NO TRADE)
  - H1: resistance 0.83669 (0.39 ATR, 5 bar sentuh) · support 0.83503 (1.43 ATR, 6 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 0.83601 (0.44 ATR, 22 bar sentuh)
- **AUD/USD** (NO TRADE)
  - H1: resistance 0.65977 (0.25 ATR, 2 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance tidak ada dalam jarak · support tidak ada dalam jarak
- **USD/CAD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 1.42735 (0.01 ATR, 13 bar sentuh)
  - M15: resistance 1.42741 (0.06 ATR, 14 bar sentuh) · support tidak ada dalam jarak
- **NZD/USD** (NO TRADE)
  - H1: resistance 0.54756 (1.15 ATR, 23 bar sentuh) · support 0.54628 (0.48 ATR, 6 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 0.54639 (0.41 ATR, 11 bar sentuh)
- **EUR/GBP** (NO TRADE)
  - H1: resistance 0.83626 (0.14 ATR, 29 bar sentuh) · support 0.83589 (0.78 ATR, 13 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 0.83615 (0.37 ATR, 50 bar sentuh)
- **EUR/JPY** (NO TRADE)
  - H1: resistance 174.51236 (0.34 ATR, 27 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance tidak ada dalam jarak · support tidak ada dalam jarak
- **EUR/CHF** (NO TRADE)
  - H1: resistance 0.91569 (0.44 ATR, 7 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance tidak ada dalam jarak · support tidak ada dalam jarak
- **EUR/AUD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 1.65908 (0.24 ATR, 2 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support tidak ada dalam jarak
- **EUR/CAD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support tidak ada dalam jarak
  - M15: resistance tidak ada dalam jarak · support 1.56201 (0.62 ATR, 2 bar sentuh)
- **EUR/NZD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 2.00078 (0.58 ATR, 57 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 2.0025 (0.0 ATR, 63 bar sentuh)
- **XAU/USD** (NO TRADE)
  - H1: resistance 3572.2265 (1.2 ATR, 20 bar sentuh) · support 3546.6735 (0.13 ATR, 17 bar sentuh)
  - M15: resistance 3552.7495 (0.64 ATR, 28 bar sentuh) · support 3544.275 (0.25 ATR, 11 bar sentuh)
- **XAU/AUD** (NO TRADE)
  - H1: resistance 5393.18225 (0.37 ATR, 11 bar sentuh) · support 5377.10775 (0.21 ATR, 19 bar sentuh)
  - M15: resistance 5391.7115 (0.76 ATR, 5 bar sentuh) · support 5376.8335 (0.41 ATR, 20 bar sentuh)

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

