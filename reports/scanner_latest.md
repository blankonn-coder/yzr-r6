# Laporan Scanner Adaptive Forex

- Waktu eksekusi: 2026-11-25T11:45:28Z
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
| EUR/USD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.09377 | — | 168/180 | 2026-11-25T10:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| GBP/USD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.30679 | — | 168/180 | 2026-11-25T10:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| USD/JPY | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 159.3695 | — | 168/180 | 2026-11-25T10:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |
| USD/CHF | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.83239 | — | 168/180 | 2026-11-25T10:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| AUD/USD | MIXED | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.65692 | — | 168/180 | 2026-11-25T10:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime MIXED belum punya metode prioritas di ranking |
| USD/CAD | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.42837 | — | 168/180 | 2026-11-25T10:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| NZD/USD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.54592 | — | 168/180 | 2026-11-25T10:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| EUR/GBP | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.83698 | — | 168/180 | 2026-11-25T10:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |
| EUR/JPY | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 174.3105 | — | 168/180 | 2026-11-25T10:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |
| EUR/CHF | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.91038 | — | 168/180 | 2026-11-25T10:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| EUR/AUD | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.66493 | — | 168/180 | 2026-11-25T10:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| EUR/CAD | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.56229 | — | 168/180 | 2026-11-25T10:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| EUR/NZD | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 2.0035 | — | 168/180 | 2026-11-25T10:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |
| XAU/USD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 3532.0565 | — | 168/180 | 2026-11-25T10:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| XAU/AUD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 5376.8895 | — | 168/180 | 2026-11-25T10:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |

## Saran analisa cadangan (BUKAN sinyal, tidak divalidasi backtest)
Dari lead-lag, maks 3 pair: leader bergerak, follower tertinggal 5-60 menit. BUY/SELL mengikuti arah leader. SL 0.5 ATR H1, TP 1.5R. Tanpa cek spread, news, atau batas risiko §9. Tidak mengubah label.
Tidak ada saran (tidak ada level H1 dalam jarak 1.0 ATR, dan tidak ada kandidat lead-lag).

## Lead-lag (backtest 6 jam, BUKAN sinyal)
- Status: dianalisa
- Pair gagal diambil (M5): tidak ada
- Backtest jendela 360 menit, diperbarui 2026-11-25T11:45:28Z, pasangan lolos 0.

Tidak ada pasangan yang lolos ambang.

Tidak ada kandidat di run ini.

## Pemantauan 15 menit (entry dan analisa cadangan)
Nilai di kolom 15m-60m = pip dari entry pada close candle M15 ke-1 sampai ke-4. Jika SL dan TP kena di candle yang sama, dihitung SL. Analisa cadangan BUKAN sinyal.
| Sumber | Pair | Arah | Entry | SL | TP | 15m | 30m | 45m | 60m | Hasil | Pip sekarang | Umur |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LEAD-LAG (analisa cadangan, bukan sinyal) | AUD/USD | SELL | 0.65705 | 0.65777 | 0.65597 | +1.3 | -1.3 | +2.7 | +3.5 | Selesai 60 menit | PROFIT 3.5 pip | 60 mnt |

## Evaluasi 1 jam (entry dan analisa cadangan)
Dibuat setelah 60 menit atau saat SL/TP kena. MFE = gerak terbaik, MAE = gerak terburuk, dalam pip.
| Sumber | Pair | Arah | 15m | 30m | 45m | 60m | Hasil | Pip akhir | MFE (pip) | MAE (pip) | Ditutup (UTC) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| LEAD-LAG (analisa cadangan, bukan sinyal) | AUD/USD | SELL | +1.3 | -1.3 | +2.7 | +3.5 | Selesai 60 menit | PROFIT 3.5 pip | 5.1 | -4.4 | 2026-11-25T11:45:28Z |

## Level analisa cadangan (BUKAN sinyal, tanpa statistik)
Level S/R terdekat untuk konteks scalping. Tidak mengubah label atau keputusan apa pun.
- **EUR/USD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 1.09315 (0.6 ATR, 8 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 1.09325 (0.4 ATR, 16 bar sentuh)
- **GBP/USD** (NO TRADE)
  - H1: resistance 1.30783 (0.77 ATR, 13 bar sentuh) · support 1.30481 (1.48 ATR, 8 bar sentuh)
  - M15: resistance 1.30608 (0.52 ATR, 14 bar sentuh) · support tidak ada dalam jarak
- **USD/JPY** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 159.23522 (0.73 ATR, 67 bar sentuh)
  - M15: resistance 159.458 (0.87 ATR, 14 bar sentuh) · support tidak ada dalam jarak
- **USD/CHF** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support tidak ada dalam jarak
  - M15: resistance tidak ada dalam jarak · support 0.83159 (0.9 ATR, 2 bar sentuh)
- **AUD/USD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 0.6559 (0.73 ATR, 2 bar sentuh)
  - M15: resistance 0.65731 (0.94 ATR, 13 bar sentuh) · support 0.65636 (0.52 ATR, 8 bar sentuh)
- **USD/CAD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 1.42739 (0.81 ATR, 13 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support tidak ada dalam jarak
- **NZD/USD** (NO TRADE)
  - H1: resistance 0.54628 (0.42 ATR, 11 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance tidak ada dalam jarak · support 0.54567 (0.14 ATR, 27 bar sentuh)
- **EUR/GBP** (NO TRADE)
  - H1: resistance 0.83698 (0.01 ATR, 29 bar sentuh) · support 0.83661 (0.7 ATR, 36 bar sentuh)
  - M15: resistance 0.83776 (0.62 ATR, 4 bar sentuh) · support 0.83738 (0.64 ATR, 17 bar sentuh)
- **EUR/JPY** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 174.2705 (0.17 ATR, 25 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 174.2799 (0.0 ATR, 30 bar sentuh)
- **EUR/CHF** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support tidak ada dalam jarak
  - M15: resistance tidak ada dalam jarak · support 0.90997 (0.22 ATR, 2 bar sentuh)
- **EUR/AUD** (NO TRADE)
  - H1: resistance 1.66752 (0.82 ATR, 1 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance 1.66636 (0.84 ATR, 11 bar sentuh) · support 1.66435 (0.58 ATR, 9 bar sentuh)
- **EUR/CAD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 1.5612 (0.81 ATR, 1 bar sentuh)
  - M15: resistance 1.56184 (0.68 ATR, 10 bar sentuh) · support 1.5612 (0.17 ATR, 2 bar sentuh)
- **EUR/NZD** (NO TRADE)
  - H1: resistance 2.00657 (1.22 ATR, 20 bar sentuh) · support 2.00101 (0.98 ATR, 56 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support tidak ada dalam jarak
- **XAU/USD** (NO TRADE)
  - H1: resistance 3540.21417 (0.44 ATR, 19 bar sentuh) · support 3513.53475 (0.99 ATR, 8 bar sentuh)
  - M15: resistance 3514.8695 (0.47 ATR, 6 bar sentuh) · support tidak ada dalam jarak
- **XAU/AUD** (NO TRADE)
  - H1: resistance 5385.4644 (0.32 ATR, 19 bar sentuh) · support 5338.993 (1.42 ATR, 21 bar sentuh)
  - M15: resistance 5348.606 (0.22 ATR, 24 bar sentuh) · support 5339.22567 (0.57 ATR, 9 bar sentuh)

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

