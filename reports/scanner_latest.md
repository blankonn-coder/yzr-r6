# Laporan Scanner Adaptive Forex

- Waktu eksekusi: 2026-11-26T17:45:34Z
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
| EUR/USD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.09708 | — | 168/180 | 2026-11-26T16:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| GBP/USD | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.31052 | — | 168/180 | 2026-11-26T16:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |
| USD/JPY | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 159.2945 | — | 168/180 | 2026-11-26T16:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |
| USD/CHF | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.83432 | — | 168/180 | 2026-11-26T16:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| AUD/USD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.66305 | — | 168/180 | 2026-11-26T16:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| USD/CAD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.42434 | — | 168/180 | 2026-11-26T16:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| NZD/USD | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.54712 | — | 168/180 | 2026-11-26T16:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |
| EUR/GBP | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.83717 | — | 168/180 | 2026-11-26T16:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| EUR/JPY | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 174.7575 | — | 168/180 | 2026-11-26T16:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |
| EUR/CHF | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.91533 | — | 168/180 | 2026-11-26T16:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| EUR/AUD | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.65463 | — | 168/180 | 2026-11-26T16:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |
| EUR/CAD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.56243 | — | 168/180 | 2026-11-26T16:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| EUR/NZD | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 2.0052 | — | 168/180 | 2026-11-26T16:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |
| XAU/USD | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 3572.0535 | — | 168/180 | 2026-11-26T16:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |
| XAU/AUD | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 5387.29 | — | 168/180 | 2026-11-26T16:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |

## Saran analisa cadangan (BUKAN sinyal, tidak divalidasi backtest)
Dari lead-lag, maks 3 pair: leader bergerak, follower tertinggal 5-60 menit. BUY/SELL mengikuti arah leader. SL 0.5 ATR H1, TP 1.5R. Tanpa cek spread, news, atau batas risiko §9. Tidak mengubah label.
Tidak ada saran (tidak ada level H1 dalam jarak 1.0 ATR, dan tidak ada kandidat lead-lag).

## Lead-lag (backtest 6 jam, BUKAN sinyal)
- Status: dianalisa
- Pair gagal diambil (M5): tidak ada
- Backtest jendela 360 menit, diperbarui 2026-11-26T17:45:34Z, pasangan lolos 0.

Tidak ada pasangan yang lolos ambang.

Tidak ada kandidat di run ini.

## Pemantauan 15 menit (entry dan analisa cadangan)
Nilai di kolom 15m-60m = pip dari entry pada close candle M15 ke-1 sampai ke-4. Jika SL dan TP kena di candle yang sama, dihitung SL. Analisa cadangan BUKAN sinyal.
| Sumber | Pair | Arah | Entry | SL | TP | 15m | 30m | 45m | 60m | Hasil | Pip sekarang | Umur |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LEAD-LAG (analisa cadangan, bukan sinyal) | EUR/CAD | SELL | 1.56263 | 1.56329 | 1.56164 | +2.0 | +3.8 | +2.7 | +2.3 | Selesai 60 menit | PROFIT 2.3 pip | 60 mnt |

## Evaluasi 1 jam (entry dan analisa cadangan)
Dibuat setelah 60 menit atau saat SL/TP kena. MFE = gerak terbaik, MAE = gerak terburuk, dalam pip.
| Sumber | Pair | Arah | 15m | 30m | 45m | 60m | Hasil | Pip akhir | MFE (pip) | MAE (pip) | Ditutup (UTC) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| LEAD-LAG (analisa cadangan, bukan sinyal) | EUR/CAD | SELL | +2.0 | +3.8 | +2.7 | +2.3 | Selesai 60 menit | PROFIT 2.3 pip | 4.6 | -1.8 | 2026-11-26T17:45:34Z |

## Level analisa cadangan (BUKAN sinyal, tanpa statistik)
Level S/R terdekat untuk konteks scalping. Tidak mengubah label atau keputusan apa pun.
- **EUR/USD** (NO TRADE)
  - H1: resistance 1.09824 (1.12 ATR, 36 bar sentuh) · support 1.09605 (0.99 ATR, 31 bar sentuh)
  - M15: resistance 1.09715 (0.47 ATR, 50 bar sentuh) · support tidak ada dalam jarak
- **GBP/USD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 1.31042 (0.07 ATR, 47 bar sentuh)
  - M15: resistance 1.31053 (0.17 ATR, 43 bar sentuh) · support tidak ada dalam jarak
- **USD/JPY** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 159.14405 (1.16 ATR, 49 bar sentuh)
  - M15: resistance 159.34408 (0.81 ATR, 27 bar sentuh) · support 159.3015 (0.28 ATR, 63 bar sentuh)
- **USD/CHF** (NO TRADE)
  - H1: resistance 0.83483 (0.46 ATR, 11 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance 0.83453 (0.1 ATR, 21 bar sentuh) · support tidak ada dalam jarak
- **AUD/USD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 0.66262 (0.45 ATR, 41 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 0.66283 (0.37 ATR, 31 bar sentuh)
- **USD/CAD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 1.4228 (1.38 ATR, 12 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 1.42413 (0.75 ATR, 11 bar sentuh)
- **NZD/USD** (NO TRADE)
  - H1: resistance 0.54755 (0.62 ATR, 27 bar sentuh) · support 0.54648 (0.93 ATR, 15 bar sentuh)
  - M15: resistance 0.54735 (0.76 ATR, 11 bar sentuh) · support 0.547 (0.68 ATR, 11 bar sentuh)
- **EUR/GBP** (NO TRADE)
  - H1: resistance 0.83769 (0.98 ATR, 46 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance tidak ada dalam jarak · support tidak ada dalam jarak
- **EUR/JPY** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 174.68744 (0.39 ATR, 39 bar sentuh)
  - M15: resistance 174.7725 (0.25 ATR, 30 bar sentuh) · support 174.7178 (0.65 ATR, 33 bar sentuh)
- **EUR/CHF** (NO TRADE)
  - H1: resistance 0.91578 (0.49 ATR, 14 bar sentuh) · support 0.91477 (0.61 ATR, 7 bar sentuh)
  - M15: resistance 0.91575 (0.99 ATR, 28 bar sentuh) · support 0.91501 (0.93 ATR, 17 bar sentuh)
- **EUR/AUD** (NO TRADE)
  - H1: resistance 1.65586 (0.5 ATR, 26 bar sentuh) · support 1.65297 (0.67 ATR, 28 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 1.65423 (0.49 ATR, 41 bar sentuh)
- **EUR/CAD** (NO TRADE)
  - H1: resistance 1.56434 (1.43 ATR, 8 bar sentuh) · support 1.5612 (0.92 ATR, 9 bar sentuh)
  - M15: resistance 1.56277 (0.59 ATR, 29 bar sentuh) · support tidak ada dalam jarak
- **EUR/NZD** (NO TRADE)
  - H1: resistance 2.00691 (0.87 ATR, 19 bar sentuh) · support 2.00332 (0.95 ATR, 40 bar sentuh)
  - M15: resistance 2.00499 (0.26 ATR, 41 bar sentuh) · support tidak ada dalam jarak
- **XAU/USD** (NO TRADE)
  - H1: resistance 3589.53663 (0.84 ATR, 21 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance 3569.10425 (0.53 ATR, 61 bar sentuh) · support 3561.03172 (0.76 ATR, 27 bar sentuh)
- **XAU/AUD** (NO TRADE)
  - H1: resistance 5423.0105 (1.26 ATR, 10 bar sentuh) · support 5373.17342 (0.5 ATR, 39 bar sentuh)
  - M15: resistance 5378.50733 (0.02 ATR, 63 bar sentuh) · support tidak ada dalam jarak

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

