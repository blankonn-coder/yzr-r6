# Laporan Scanner Adaptive Forex

- Waktu eksekusi: 2026-11-25T16:15:27Z
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
| EUR/USD | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.09397 | — | 168/180 | 2026-11-25T14:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |
| GBP/USD | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.30567 | — | 168/180 | 2026-11-25T14:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| USD/JPY | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 159.2695 | — | 168/180 | 2026-11-25T14:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |
| USD/CHF | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.8314 | — | 168/180 | 2026-11-25T14:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| AUD/USD | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.65856 | — | 168/180 | 2026-11-25T14:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| USD/CAD | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.42325 | — | 168/180 | 2026-11-25T14:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| NZD/USD | VOLATIL/CHOPPY | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.54598 | — | 168/180 | 2026-11-25T14:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime VOLATIL/CHOPPY belum punya metode prioritas di ranking |
| EUR/GBP | MIXED | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.83789 | — | 168/180 | 2026-11-25T14:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime MIXED belum punya metode prioritas di ranking |
| EUR/JPY | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 174.2335 | — | 168/180 | 2026-11-25T14:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |
| EUR/CHF | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.90958 | — | 168/180 | 2026-11-25T14:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| EUR/AUD | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.66115 | — | 168/180 | 2026-11-25T14:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| EUR/CAD | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.55707 | — | 168/180 | 2026-11-25T14:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| EUR/NZD | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 2.00366 | — | 168/180 | 2026-11-25T14:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |
| XAU/USD | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 3472.2095 | — | 168/180 | 2026-11-25T14:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| XAU/AUD | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 5272.3865 | — | 168/180 | 2026-11-25T14:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |

## Saran analisa cadangan (BUKAN sinyal, tidak divalidasi backtest)
Dari lead-lag, maks 3 pair: leader bergerak, follower tertinggal 5-60 menit. BUY/SELL mengikuti arah leader. SL 0.5 ATR H1, TP 1.5R. Tanpa cek spread, news, atau batas risiko §9. Tidak mengubah label.
Tidak ada saran (tidak ada level H1 dalam jarak 1.0 ATR, dan tidak ada kandidat lead-lag).

## Lead-lag (backtest 6 jam, BUKAN sinyal)
- Status: dianalisa
- Pair gagal diambil (M5): tidak ada
- Backtest jendela 360 menit, diperbarui 2026-11-25T16:15:27Z, pasangan lolos 0.

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
  - H1: resistance tidak ada dalam jarak · support 1.09315 (0.69 ATR, 9 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support tidak ada dalam jarak
- **GBP/USD** (NO TRADE)
  - H1: resistance 1.30788 (1.42 ATR, 17 bar sentuh) · support 1.30502 (0.41 ATR, 9 bar sentuh)
  - M15: resistance 1.30698 (0.63 ATR, 28 bar sentuh) · support 1.30578 (0.45 ATR, 13 bar sentuh)
- **USD/JPY** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 159.22001 (0.26 ATR, 66 bar sentuh)
  - M15: resistance 159.24279 (0.41 ATR, 79 bar sentuh) · support tidak ada dalam jarak
- **USD/CHF** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support tidak ada dalam jarak
  - M15: resistance tidak ada dalam jarak · support 0.83159 (0.25 ATR, 7 bar sentuh)
- **AUD/USD** (NO TRADE)
  - H1: resistance 0.65977 (0.87 ATR, 3 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance 0.6586 (0.71 ATR, 8 bar sentuh) · support 0.65748 (0.66 ATR, 19 bar sentuh)
- **USD/CAD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support tidak ada dalam jarak
  - M15: resistance 1.42527 (0.55 ATR, 4 bar sentuh) · support tidak ada dalam jarak
- **NZD/USD** (NO TRADE)
  - H1: resistance 0.54636 (0.43 ATR, 16 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance tidak ada dalam jarak · support tidak ada dalam jarak
- **EUR/GBP** (NO TRADE)
  - H1: resistance 0.83796 (0.1 ATR, 33 bar sentuh) · support 0.83698 (1.44 ATR, 32 bar sentuh)
  - M15: resistance 0.8378 (0.74 ATR, 11 bar sentuh) · support tidak ada dalam jarak
- **EUR/JPY** (NO TRADE)
  - H1: resistance 174.2705 (0.16 ATR, 29 bar sentuh) · support 173.9605 (1.16 ATR, 10 bar sentuh)
  - M15: resistance 174.23739 (0.56 ATR, 24 bar sentuh) · support tidak ada dalam jarak
- **EUR/CHF** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support tidak ada dalam jarak
  - M15: resistance tidak ada dalam jarak · support 0.90997 (0.09 ATR, 7 bar sentuh)
- **EUR/AUD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 1.65908 (0.64 ATR, 4 bar sentuh)
  - M15: resistance 1.66329 (0.4 ATR, 12 bar sentuh) · support 1.66166 (0.43 ATR, 4 bar sentuh)
- **EUR/CAD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support tidak ada dalam jarak
  - M15: resistance 1.55911 (0.5 ATR, 5 bar sentuh) · support tidak ada dalam jarak
- **EUR/NZD** (NO TRADE)
  - H1: resistance 2.00657 (1.14 ATR, 21 bar sentuh) · support 2.00101 (1.03 ATR, 56 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support tidak ada dalam jarak
- **XAU/USD** (NO TRADE)
  - H1: resistance 3509.9505 (1.48 ATR, 10 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance tidak ada dalam jarak · support tidak ada dalam jarak
- **XAU/AUD** (NO TRADE)
  - H1: resistance 5288.495 (0.43 ATR, 6 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance 5273.18 (0.58 ATR, 6 bar sentuh) · support tidak ada dalam jarak

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

