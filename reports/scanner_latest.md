# Laporan Scanner Adaptive Forex

- Waktu eksekusi: 2026-11-24T18:00:43Z
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
| EUR/USD | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.09733 | — | 168/180 | 2026-11-24T17:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| GBP/USD | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.31217 | — | 168/180 | 2026-11-24T17:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| USD/JPY | VOLATIL/CHOPPY | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 159.2115 | — | 168/180 | 2026-11-24T17:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime VOLATIL/CHOPPY belum punya metode prioritas di ranking |
| USD/CHF | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.83537 | — | 168/180 | 2026-11-24T17:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| AUD/USD | MIXED | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.6643 | — | 168/180 | 2026-11-24T17:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime MIXED belum punya metode prioritas di ranking |
| USD/CAD | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.42772 | — | 168/180 | 2026-11-24T17:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| NZD/USD | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.54877 | — | 168/180 | 2026-11-24T17:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| EUR/GBP | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.83625 | — | 168/180 | 2026-11-24T17:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |
| EUR/JPY | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 174.7055 | — | 168/180 | 2026-11-24T17:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| EUR/CHF | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.91666 | — | 168/180 | 2026-11-24T17:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| EUR/AUD | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.65183 | — | 168/180 | 2026-11-24T17:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| EUR/CAD | MIXED | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.56656 | — | 168/180 | 2026-11-24T17:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime MIXED belum punya metode prioritas di ranking |
| EUR/NZD | VOLATIL/CHOPPY | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.99962 | — | 168/180 | 2026-11-24T17:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime VOLATIL/CHOPPY belum punya metode prioritas di ranking |
| XAU/USD | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 3566.8455 | — | 168/180 | 2026-11-24T17:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |
| XAU/AUD | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 5369.268 | — | 168/180 | 2026-11-24T17:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |

## Saran analisa cadangan (BUKAN sinyal, tidak divalidasi backtest)
3 pair dengan level H1 terdekat. BUY dari support, SELL dari resistance. SL 0.5 ATR di seberang level, TP 1.5R. Tanpa cek spread, news, atau batas risiko §9. Tidak mengubah label.
| Pair | Arah | Level H1 (jarak, sentuhan) | Entry | SL | TP | Risiko SL |
|---|---|---|---|---|---|---|
| EUR/NZD | **BUY** | 1.99896 support (0.26 ATR, 49 sentuh) | 1.99962 | 1.99766 | 2.00256 | 19.6 pip |
| USD/JPY | **SELL** | 159.26545 resistance (0.28 ATR, 58 sentuh) | 159.2115 | 159.36338 | 158.98367 | 15.2 pip |
| EUR/AUD | **SELL** | 1.65267 resistance (0.28 ATR, 18 sentuh) | 1.65183 | 1.65416 | 1.64834 | 23.3 pip |

## Pemantauan 15 menit (entry dan analisa cadangan)
Nilai di kolom 15m-60m = pip dari entry pada close candle M15 ke-1 sampai ke-4. Jika SL dan TP kena di candle yang sama, dihitung SL. Analisa cadangan BUKAN sinyal.
| Sumber | Pair | Arah | Entry | SL | TP | 15m | 30m | 45m | 60m | Hasil | Pip sekarang | Umur |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ANALISA CADANGAN (bukan sinyal) | XAU/AUD | SELL | 5374.964 | 5391.8385 | 5349.65225 | -31.2 | +76.4 | +29.9 | +57.0 | Selesai 60 menit | PROFIT 57.0 pip | 60 mnt |
| ANALISA CADANGAN (bukan sinyal) | EUR/JPY | BUY | 174.5555 | 174.38896 | 174.80532 | +4.8 | +14.7 | +12.7 | +15.0 | Selesai 60 menit | PROFIT 15.0 pip | 60 mnt |
| ANALISA CADANGAN (bukan sinyal) | EUR/AUD | BUY | 1.65372 | 1.65118 | 1.65753 | -22.3 | -20.0 | -20.9 | -18.9 | Selesai 60 menit | LOSS 18.9 pip | 60 mnt |
| ANALISA CADANGAN (bukan sinyal) | EUR/GBP | SELL | 0.83639 | 0.83688 | 0.83565 | +1.1 | +1.4 | +0.9 | +1.3 | Selesai 60 menit | PROFIT 1.3 pip | 60 mnt |
| ANALISA CADANGAN (bukan sinyal) | USD/JPY | SELL | 159.1515 | 159.36264 | 158.83478 | -8.5 | -12.4 | -9.0 | -6.0 | Selesai 60 menit | LOSS 6.0 pip | 45 mnt |
| ANALISA CADANGAN (bukan sinyal) | NZD/USD | BUY | 0.54807 | 0.54713 | 0.54949 | +3.4 | +6.4 | +5.6 | +7.0 | Selesai 60 menit | PROFIT 7.0 pip | 45 mnt |
| ANALISA CADANGAN (bukan sinyal) | GBP/USD | BUY | 1.3113 | 1.30966 | 1.31375 | -1.9 | +4.2 | +3.8 | +8.7 | Selesai 60 menit | PROFIT 8.7 pip | 45 mnt |
| ANALISA CADANGAN (bukan sinyal) | EUR/USD | BUY | 1.09678 | 1.09533 | 1.09896 | -2.8 | +1.3 | +1.7 | +5.5 | Selesai 60 menit | PROFIT 5.5 pip | 45 mnt |
| ANALISA CADANGAN (bukan sinyal) | EUR/NZD | BUY | 2.00114 | 1.99766 | 2.00636 | -17.4 | -20.9 | -16.4 | -15.1 | Selesai 60 menit | LOSS 15.1 pip | 30 mnt |
| ANALISA CADANGAN (bukan sinyal) | AUD/USD | SELL | 0.66323 | 0.66411 | 0.66191 | -7.0 | - | - | - | SL kena | LOSS 8.8 pip | 15 mnt |
| ANALISA CADANGAN (bukan sinyal) | USD/CAD | BUY | 1.43127 | 1.42957 | 1.43382 | -6.5 | - | - | - | SL kena | LOSS 17.0 pip | 15 mnt |

## Evaluasi 1 jam (entry dan analisa cadangan)
Dibuat setelah 60 menit atau saat SL/TP kena. MFE = gerak terbaik, MAE = gerak terburuk, dalam pip.
| Sumber | Pair | Arah | Hasil | Pip akhir | MFE (pip) | MAE (pip) | Ditutup (UTC) |
|---|---|---|---|---|---|---|---|
| ANALISA CADANGAN (bukan sinyal) | XAU/AUD | SELL | Selesai 60 menit | PROFIT 57.0 pip | 121.8 | -75.9 | 2026-11-24T18:00:43Z |
| ANALISA CADANGAN (bukan sinyal) | EUR/JPY | BUY | Selesai 60 menit | PROFIT 15.0 pip | 19.3 | -0.7 | 2026-11-24T18:00:43Z |
| ANALISA CADANGAN (bukan sinyal) | EUR/AUD | BUY | Selesai 60 menit | LOSS 18.9 pip | 2.8 | -24.8 | 2026-11-24T18:00:43Z |
| ANALISA CADANGAN (bukan sinyal) | EUR/GBP | SELL | Selesai 60 menit | PROFIT 1.3 pip | 1.8 | -1.3 | 2026-11-24T18:00:43Z |
| ANALISA CADANGAN (bukan sinyal) | USD/JPY | SELL | Selesai 60 menit | LOSS 6.0 pip | 1.4 | -14.6 | 2026-11-24T18:00:43Z |
| ANALISA CADANGAN (bukan sinyal) | NZD/USD | BUY | Selesai 60 menit | PROFIT 7.0 pip | 8.7 | -0.6 | 2026-11-24T18:00:43Z |
| ANALISA CADANGAN (bukan sinyal) | GBP/USD | BUY | Selesai 60 menit | PROFIT 8.7 pip | 9.7 | -2.7 | 2026-11-24T18:00:43Z |
| ANALISA CADANGAN (bukan sinyal) | EUR/USD | BUY | Selesai 60 menit | PROFIT 5.5 pip | 7.3 | -4.0 | 2026-11-24T18:00:43Z |
| ANALISA CADANGAN (bukan sinyal) | EUR/NZD | BUY | Selesai 60 menit | LOSS 15.1 pip | 1.8 | -24.4 | 2026-11-24T18:00:43Z |
| ANALISA CADANGAN (bukan sinyal) | AUD/USD | SELL | SL kena · menit 30 | LOSS 8.8 pip | 1.1 | -9.2 | 2026-11-24T18:00:43Z |
| ANALISA CADANGAN (bukan sinyal) | USD/CAD | BUY | SL kena · menit 30 | LOSS 17.0 pip | 0.8 | -29.9 | 2026-11-24T18:00:43Z |

## Level analisa cadangan (BUKAN sinyal, tanpa statistik)
Level S/R terdekat untuk konteks scalping. Tidak mengubah label atau keputusan apa pun.
- **EUR/USD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 1.09599 (1.03 ATR, 23 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 1.09684 (0.64 ATR, 34 bar sentuh)
- **GBP/USD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 1.31042 (1.18 ATR, 30 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 1.31162 (0.62 ATR, 21 bar sentuh)
- **USD/JPY** (NO TRADE)
  - H1: resistance 159.26545 (0.28 ATR, 58 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance 159.2532 (0.39 ATR, 34 bar sentuh) · support tidak ada dalam jarak
- **USD/CHF** (NO TRADE)
  - H1: resistance 0.83669 (1.04 ATR, 4 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance 0.8354 (0.05 ATR, 11 bar sentuh) · support tidak ada dalam jarak
- **AUD/USD** (NO TRADE)
  - H1: resistance 0.66553 (0.94 ATR, 21 bar sentuh) · support 0.66346 (0.65 ATR, 28 bar sentuh)
  - M15: resistance 0.6649 (0.92 ATR, 24 bar sentuh) · support tidak ada dalam jarak
- **USD/CAD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 1.42685 (0.56 ATR, 9 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support tidak ada dalam jarak
- **NZD/USD** (NO TRADE)
  - H1: resistance 0.54933 (0.64 ATR, 55 bar sentuh) · support 0.54756 (1.38 ATR, 18 bar sentuh)
  - M15: resistance 0.54891 (0.31 ATR, 3 bar sentuh) · support tidak ada dalam jarak
- **EUR/GBP** (NO TRADE)
  - H1: resistance 0.83661 (0.68 ATR, 33 bar sentuh) · support 0.83594 (0.6 ATR, 10 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support tidak ada dalam jarak
- **EUR/JPY** (NO TRADE)
  - H1: resistance 174.903 (0.77 ATR, 33 bar sentuh) · support 174.5197 (0.72 ATR, 27 bar sentuh)
  - M15: resistance 174.798 (0.74 ATR, 12 bar sentuh) · support 174.6385 (0.54 ATR, 22 bar sentuh)
- **EUR/CHF** (NO TRADE)
  - H1: resistance 0.91743 (0.71 ATR, 12 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance tidak ada dalam jarak · support tidak ada dalam jarak
- **EUR/AUD** (NO TRADE)
  - H1: resistance 1.65267 (0.28 ATR, 18 bar sentuh) · support 1.64946 (0.8 ATR, 18 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 1.65031 (0.93 ATR, 20 bar sentuh)
- **EUR/CAD** (NO TRADE)
  - H1: resistance 1.56742 (0.48 ATR, 12 bar sentuh) · support 1.56439 (1.21 ATR, 2 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 1.56638 (0.16 ATR, 35 bar sentuh)
- **EUR/NZD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 1.99896 (0.26 ATR, 49 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 1.99954 (0.06 ATR, 10 bar sentuh)
- **XAU/USD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support tidak ada dalam jarak
  - M15: resistance 3568.257 (0.12 ATR, 15 bar sentuh) · support 3559.9175 (0.61 ATR, 6 bar sentuh)
- **XAU/AUD** (NO TRADE)
  - H1: resistance 5377.382 (0.29 ATR, 15 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance 5371.05867 (0.12 ATR, 10 bar sentuh) · support tidak ada dalam jarak

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

