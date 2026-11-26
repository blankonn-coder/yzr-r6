# Laporan Scanner Adaptive Forex

- Waktu eksekusi: 2026-11-26T08:00:41Z
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
| EUR/USD | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.09736 | — | 168/180 | 2026-11-26T07:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |
| GBP/USD | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.31038 | — | 168/180 | 2026-11-26T07:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |
| USD/JPY | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 159.1695 | — | 168/180 | 2026-11-26T07:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| USD/CHF | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.83284 | — | 168/180 | 2026-11-26T07:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| AUD/USD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.66355 | — | 168/180 | 2026-11-26T07:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| USD/CAD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.42226 | — | 168/180 | 2026-11-26T07:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| NZD/USD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.54814 | — | 168/180 | 2026-11-26T07:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| EUR/GBP | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.83744 | — | 168/180 | 2026-11-26T07:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| EUR/JPY | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 174.6655 | — | 168/180 | 2026-11-26T07:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |
| EUR/CHF | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.91395 | — | 168/180 | 2026-11-26T07:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| EUR/AUD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.65375 | — | 168/180 | 2026-11-26T07:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| EUR/CAD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.56056 | — | 168/180 | 2026-11-26T07:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| EUR/NZD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 2.00201 | — | 168/180 | 2026-11-26T07:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| XAU/USD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 3564.8575 | — | 168/180 | 2026-11-26T07:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| XAU/AUD | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 5372.495 | — | 168/180 | 2026-11-26T07:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |

## Saran analisa cadangan (BUKAN sinyal, tidak divalidasi backtest)
Dari lead-lag, maks 3 pair: leader bergerak, follower tertinggal 5-60 menit. BUY/SELL mengikuti arah leader. SL 0.5 ATR H1, TP 1.5R. Tanpa cek spread, news, atau batas risiko §9. Tidak mengubah label.
Tidak ada saran (tidak ada level H1 dalam jarak 1.0 ATR, dan tidak ada kandidat lead-lag).

## Lead-lag (backtest 6 jam, BUKAN sinyal)
- Status: dianalisa
- Pair gagal diambil (M5): tidak ada
- Backtest jendela 360 menit, diperbarui 2026-11-26T08:00:41Z, pasangan lolos 0.

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
  - H1: resistance 1.09819 (0.87 ATR, 35 bar sentuh) · support 1.09606 (1.36 ATR, 30 bar sentuh)
  - M15: resistance 1.09751 (0.34 ATR, 25 bar sentuh) · support tidak ada dalam jarak
- **GBP/USD** (NO TRADE)
  - H1: resistance 1.31042 (0.02 ATR, 39 bar sentuh) · support 1.30952 (0.67 ATR, 32 bar sentuh)
  - M15: resistance 1.31052 (0.24 ATR, 25 bar sentuh) · support tidak ada dalam jarak
- **USD/JPY** (NO TRADE)
  - H1: resistance 159.18943 (0.12 ATR, 67 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance tidak ada dalam jarak · support tidak ada dalam jarak
- **USD/CHF** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 0.83234 (0.49 ATR, 6 bar sentuh)
  - M15: resistance 0.83322 (0.84 ATR, 3 bar sentuh) · support tidak ada dalam jarak
- **AUD/USD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 0.66293 (0.53 ATR, 41 bar sentuh)
  - M15: resistance 0.66371 (0.35 ATR, 39 bar sentuh) · support tidak ada dalam jarak
- **USD/CAD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 1.421 (1.13 ATR, 7 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 1.42226 (0.0 ATR, 19 bar sentuh)
- **NZD/USD** (NO TRADE)
  - H1: resistance 0.5487 (0.77 ATR, 39 bar sentuh) · support 0.54756 (0.79 ATR, 23 bar sentuh)
  - M15: resistance 0.54834 (0.67 ATR, 35 bar sentuh) · support tidak ada dalam jarak
- **EUR/GBP** (NO TRADE)
  - H1: resistance 0.83766 (0.47 ATR, 39 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance 0.83745 (0.12 ATR, 25 bar sentuh) · support 0.83735 (0.52 ATR, 25 bar sentuh)
- **EUR/JPY** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 174.65594 (0.05 ATR, 37 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support tidak ada dalam jarak
- **EUR/CHF** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support tidak ada dalam jarak
  - M15: resistance tidak ada dalam jarak · support tidak ada dalam jarak
- **EUR/AUD** (NO TRADE)
  - H1: resistance 1.65585 (0.73 ATR, 21 bar sentuh) · support 1.65267 (0.37 ATR, 26 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 1.6534 (0.3 ATR, 19 bar sentuh)
- **EUR/CAD** (NO TRADE)
  - H1: resistance 1.5612 (0.54 ATR, 3 bar sentuh) · support 1.56036 (0.17 ATR, 6 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support tidak ada dalam jarak
- **EUR/NZD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 2.00082 (0.55 ATR, 54 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 2.00134 (0.71 ATR, 33 bar sentuh)
- **XAU/USD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 3543.02175 (0.79 ATR, 24 bar sentuh)
  - M15: resistance 3575.1187 (0.91 ATR, 32 bar sentuh) · support tidak ada dalam jarak
- **XAU/AUD** (NO TRADE)
  - H1: resistance 5385.4644 (0.34 ATR, 31 bar sentuh) · support 5316.15157 (1.47 ATR, 17 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 5369.99546 (0.16 ATR, 43 bar sentuh)

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

