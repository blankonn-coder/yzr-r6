# Laporan Scanner Adaptive Forex

- Waktu eksekusi: 2026-11-26T04:30:33Z
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
| EUR/USD | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.09609 | — | 168/180 | 2026-11-26T03:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |
| GBP/USD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.31004 | — | 168/180 | 2026-11-26T03:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| USD/JPY | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 159.1575 | — | 168/180 | 2026-11-26T03:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| USD/CHF | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.83186 | — | 168/180 | 2026-11-26T03:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| AUD/USD | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.66404 | — | 168/180 | 2026-11-26T03:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| USD/CAD | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.42208 | — | 168/180 | 2026-11-26T03:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| NZD/USD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.54826 | — | 168/180 | 2026-11-26T03:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| EUR/GBP | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.83669 | — | 168/180 | 2026-11-26T03:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| EUR/JPY | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 174.4495 | — | 168/180 | 2026-11-26T03:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |
| EUR/CHF | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.91177 | — | 168/180 | 2026-11-26T03:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| EUR/AUD | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.65058 | — | 168/180 | 2026-11-26T03:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| EUR/CAD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.5585 | — | 168/180 | 2026-11-26T03:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| EUR/NZD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.99918 | — | 168/180 | 2026-11-26T03:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| XAU/USD | MIXED | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 3575.3915 | — | 168/180 | 2026-11-26T03:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime MIXED belum punya metode prioritas di ranking |
| XAU/AUD | MIXED | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 5384.0775 | — | 168/180 | 2026-11-26T03:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime MIXED belum punya metode prioritas di ranking |

## Saran analisa cadangan (BUKAN sinyal, tidak divalidasi backtest)
Dari lead-lag, maks 3 pair: leader bergerak, follower tertinggal 5-60 menit. BUY/SELL mengikuti arah leader. SL 0.5 ATR H1, TP 1.5R. Tanpa cek spread, news, atau batas risiko §9. Tidak mengubah label.
Tidak ada saran (tidak ada level H1 dalam jarak 1.0 ATR, dan tidak ada kandidat lead-lag).

## Lead-lag (backtest 6 jam, BUKAN sinyal)
- Status: dianalisa
- Pair gagal diambil (M5): tidak ada
- Backtest jendela 360 menit, diperbarui 2026-11-26T04:30:33Z, pasangan lolos 0.

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
  - H1: resistance tidak ada dalam jarak · support 1.09609 (0.0 ATR, 30 bar sentuh)
  - M15: resistance 1.09618 (0.28 ATR, 30 bar sentuh) · support tidak ada dalam jarak
- **GBP/USD** (NO TRADE)
  - H1: resistance 1.31042 (0.27 ATR, 37 bar sentuh) · support 1.3094 (0.45 ATR, 27 bar sentuh)
  - M15: resistance 1.31055 (0.74 ATR, 18 bar sentuh) · support 1.30995 (0.4 ATR, 17 bar sentuh)
- **USD/JPY** (NO TRADE)
  - H1: resistance 159.1918 (0.18 ATR, 68 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance tidak ada dalam jarak · support 159.10162 (0.39 ATR, 35 bar sentuh)
- **USD/CHF** (NO TRADE)
  - H1: resistance 0.83207 (0.19 ATR, 6 bar sentuh) · support 0.83066 (1.06 ATR, 10 bar sentuh)
  - M15: resistance 0.83218 (0.97 ATR, 7 bar sentuh) · support 0.83169 (0.35 ATR, 21 bar sentuh)
- **AUD/USD** (NO TRADE)
  - H1: resistance 0.66553 (1.18 ATR, 23 bar sentuh) · support 0.66293 (0.88 ATR, 41 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 0.66422 (0.71 ATR, 41 bar sentuh)
- **USD/CAD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 1.421 (0.84 ATR, 7 bar sentuh)
  - M15: resistance 1.42232 (0.62 ATR, 9 bar sentuh) · support 1.42179 (0.62 ATR, 12 bar sentuh)
- **NZD/USD** (NO TRADE)
  - H1: resistance 0.5487 (0.55 ATR, 42 bar sentuh) · support 0.54756 (0.87 ATR, 23 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 0.54834 (0.41 ATR, 32 bar sentuh)
- **EUR/GBP** (NO TRADE)
  - H1: resistance 0.83696 (0.53 ATR, 34 bar sentuh) · support 0.83606 (1.2 ATR, 27 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 0.83657 (0.11 ATR, 41 bar sentuh)
- **EUR/JPY** (NO TRADE)
  - H1: resistance 174.66761 (1.01 ATR, 34 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance 174.48743 (1.0 ATR, 31 bar sentuh) · support 174.3695 (0.55 ATR, 45 bar sentuh)
- **EUR/CHF** (NO TRADE)
  - H1: resistance 0.91241 (0.67 ATR, 7 bar sentuh) · support 0.9116 (0.16 ATR, 7 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 0.91173 (0.09 ATR, 17 bar sentuh)
- **EUR/AUD** (NO TRADE)
  - H1: resistance 1.65267 (0.7 ATR, 24 bar sentuh) · support 1.64955 (0.35 ATR, 20 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 1.64864 (0.47 ATR, 14 bar sentuh)
- **EUR/CAD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support tidak ada dalam jarak
  - M15: resistance tidak ada dalam jarak · support 1.55812 (0.74 ATR, 13 bar sentuh)
- **EUR/NZD** (NO TRADE)
  - H1: resistance 2.00105 (0.83 ATR, 55 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance tidak ada dalam jarak · support 1.99808 (0.24 ATR, 7 bar sentuh)
- **XAU/USD** (NO TRADE)
  - H1: resistance 3607.46442 (1.08 ATR, 16 bar sentuh) · support 3543.02175 (1.09 ATR, 24 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 3587.4665 (0.21 ATR, 15 bar sentuh)
- **XAU/AUD** (NO TRADE)
  - H1: resistance 5385.4644 (0.03 ATR, 29 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance 5414.32925 (0.58 ATR, 8 bar sentuh) · support tidak ada dalam jarak

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

