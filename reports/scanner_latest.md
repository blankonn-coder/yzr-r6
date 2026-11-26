# Laporan Scanner Adaptive Forex

- Waktu eksekusi: 2026-11-26T14:00:43Z
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
| EUR/USD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.09849 | — | 168/180 | 2026-11-26T13:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| GBP/USD | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.31193 | — | 168/180 | 2026-11-26T13:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |
| USD/JPY | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 159.2025 | — | 168/180 | 2026-11-26T13:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| USD/CHF | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.83327 | — | 168/180 | 2026-11-26T13:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| AUD/USD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.66373 | — | 168/180 | 2026-11-26T13:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| USD/CAD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.42324 | — | 168/180 | 2026-11-26T13:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| NZD/USD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.54825 | — | 168/180 | 2026-11-26T13:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| EUR/GBP | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.83734 | — | 168/180 | 2026-11-26T13:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| EUR/JPY | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 174.8815 | — | 168/180 | 2026-11-26T13:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |
| EUR/CHF | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.91539 | — | 168/180 | 2026-11-26T13:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| EUR/AUD | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.65503 | — | 168/180 | 2026-11-26T13:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |
| EUR/CAD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.56323 | — | 168/180 | 2026-11-26T13:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| EUR/NZD | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 2.00365 | — | 168/180 | 2026-11-26T13:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |
| XAU/USD | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 3571.6895 | — | 168/180 | 2026-11-26T13:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |
| XAU/AUD | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 5381.3645 | — | 168/180 | 2026-11-26T13:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |

## Saran analisa cadangan (BUKAN sinyal, tidak divalidasi backtest)
Dari lead-lag, maks 3 pair: leader bergerak, follower tertinggal 5-60 menit. BUY/SELL mengikuti arah leader. SL 0.5 ATR H1, TP 1.5R. Tanpa cek spread, news, atau batas risiko §9. Tidak mengubah label.
Tidak ada saran (tidak ada level H1 dalam jarak 1.0 ATR, dan tidak ada kandidat lead-lag).

## Lead-lag (backtest 6 jam, BUKAN sinyal)
- Status: dianalisa
- Pair gagal diambil (M5): tidak ada
- Backtest jendela 360 menit, diperbarui 2026-11-26T14:00:43Z, pasangan lolos 0.

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
  - H1: resistance tidak ada dalam jarak · support 1.0982 (0.29 ATR, 39 bar sentuh)
  - M15: resistance 1.09853 (0.08 ATR, 2 bar sentuh) · support tidak ada dalam jarak
- **GBP/USD** (NO TRADE)
  - H1: resistance 1.3124 (0.35 ATR, 15 bar sentuh) · support 1.31042 (1.13 ATR, 44 bar sentuh)
  - M15: resistance 1.31242 (0.75 ATR, 6 bar sentuh) · support 1.31131 (0.93 ATR, 58 bar sentuh)
- **USD/JPY** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 159.18221 (0.14 ATR, 59 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support tidak ada dalam jarak
- **USD/CHF** (NO TRADE)
  - H1: resistance 0.83483 (1.36 ATR, 11 bar sentuh) · support 0.83183 (1.26 ATR, 13 bar sentuh)
  - M15: resistance 0.83343 (0.29 ATR, 9 bar sentuh) · support tidak ada dalam jarak
- **AUD/USD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 0.66291 (0.81 ATR, 44 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 0.66371 (0.06 ATR, 43 bar sentuh)
- **USD/CAD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 1.4228 (0.41 ATR, 11 bar sentuh)
  - M15: resistance 1.42335 (0.24 ATR, 24 bar sentuh) · support tidak ada dalam jarak
- **NZD/USD** (NO TRADE)
  - H1: resistance 0.5487 (0.66 ATR, 37 bar sentuh) · support 0.54755 (1.04 ATR, 26 bar sentuh)
  - M15: resistance 0.54829 (0.15 ATR, 39 bar sentuh) · support tidak ada dalam jarak
- **EUR/GBP** (NO TRADE)
  - H1: resistance 0.83767 (0.61 ATR, 44 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance tidak ada dalam jarak · support tidak ada dalam jarak
- **EUR/JPY** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 174.67687 (1.07 ATR, 37 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support tidak ada dalam jarak
- **EUR/CHF** (NO TRADE)
  - H1: resistance 0.91569 (0.31 ATR, 11 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance 0.91577 (0.76 ATR, 25 bar sentuh) · support 0.91506 (0.63 ATR, 14 bar sentuh)
- **EUR/AUD** (NO TRADE)
  - H1: resistance 1.65589 (0.33 ATR, 23 bar sentuh) · support 1.65267 (0.9 ATR, 28 bar sentuh)
  - M15: resistance 1.65567 (0.67 ATR, 20 bar sentuh) · support 1.65417 (0.9 ATR, 32 bar sentuh)
- **EUR/CAD** (NO TRADE)
  - H1: resistance 1.56434 (0.85 ATR, 8 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance 1.56324 (0.02 ATR, 18 bar sentuh) · support 1.56279 (0.69 ATR, 21 bar sentuh)
- **EUR/NZD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 2.00332 (0.16 ATR, 38 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 2.00318 (0.51 ATR, 33 bar sentuh)
- **XAU/USD** (NO TRADE)
  - H1: resistance 3589.66555 (0.79 ATR, 21 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance 3575.41139 (0.46 ATR, 40 bar sentuh) · support 3568.8385 (0.35 ATR, 56 bar sentuh)
- **XAU/AUD** (NO TRADE)
  - H1: resistance 5423.0105 (1.32 ATR, 12 bar sentuh) · support 5370.73464 (0.34 ATR, 37 bar sentuh)
  - M15: resistance 5388.9175 (0.67 ATR, 36 bar sentuh) · support tidak ada dalam jarak

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

