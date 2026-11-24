# Laporan Scanner Adaptive Forex

- Waktu eksekusi: 2026-11-24T16:45:28Z
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
| EUR/USD | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.09708 | — | 168/180 | 2026-11-24T15:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| GBP/USD | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.31161 | — | 168/180 | 2026-11-24T15:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| USD/JPY | VOLATIL/CHOPPY | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 159.0815 | — | 168/180 | 2026-11-24T15:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime VOLATIL/CHOPPY belum punya metode prioritas di ranking |
| USD/CHF | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.83542 | — | 168/180 | 2026-11-24T15:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| AUD/USD | VOLATIL/CHOPPY | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.66372 | — | 168/180 | 2026-11-24T15:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime VOLATIL/CHOPPY belum punya metode prioritas di ranking |
| USD/CAD | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.43117 | — | 168/180 | 2026-11-24T15:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| NZD/USD | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.54802 | — | 168/180 | 2026-11-24T15:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| EUR/GBP | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.83644 | — | 168/180 | 2026-11-24T15:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |
| EUR/JPY | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 174.5275 | — | 168/180 | 2026-11-24T15:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| EUR/CHF | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.91655 | — | 168/180 | 2026-11-24T15:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| EUR/AUD | MIXED | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.65299 | — | 168/180 | 2026-11-24T15:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime MIXED belum punya metode prioritas di ranking |
| EUR/CAD | MIXED | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.57001 | — | 168/180 | 2026-11-24T15:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime MIXED belum punya metode prioritas di ranking |
| EUR/NZD | VOLATIL/CHOPPY | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 2.00191 | — | 168/180 | 2026-11-24T15:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime VOLATIL/CHOPPY belum punya metode prioritas di ranking |
| XAU/USD | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 3569.1975 | — | 168/180 | 2026-11-24T15:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |
| XAU/AUD | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 5377.3865 | — | 168/180 | 2026-11-24T15:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |

## Saran analisa cadangan (BUKAN sinyal, tidak divalidasi backtest)
5 pair dengan level H1 terdekat. BUY dari support, SELL dari resistance. SL 0.5 ATR di seberang level, TP 1.5R. Tanpa cek spread, news, atau batas risiko §9. Tidak mengubah label.
| Pair | Arah | Level H1 (jarak, sentuhan) | Entry | SL | TP | Risiko SL |
|---|---|---|---|---|---|---|
| AUD/USD | **BUY** | 0.66346 support (0.2 ATR, 26 sentuh) | 0.66372 | 0.6628 | 0.6651 | 9.2 pip |
| EUR/GBP | **SELL** | 0.83661 resistance (0.31 ATR, 31 sentuh) | 0.83644 | 0.83688 | 0.83577 | 4.5 pip |

## Pemantauan 15 menit (entry dan analisa cadangan)
Nilai di kolom 15m-60m = pip dari entry pada close candle M15 ke-1 sampai ke-4. Jika SL dan TP kena di candle yang sama, dihitung SL. Analisa cadangan BUKAN sinyal.
| Sumber | Pair | Arah | Entry | SL | TP | 15m | 30m | 45m | 60m | Hasil | Pip sekarang | Umur |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ANALISA CADANGAN (bukan sinyal) | XAU/AUD | BUY | 5377.3865 | 5362.80985 | 5399.25147 | +29.9 | +3.2 | +141.3 | - | BERJALAN | PROFIT 141.3 pip | 45 mnt |
| ANALISA CADANGAN (bukan sinyal) | EUR/JPY | BUY | 174.5275 | 174.3879 | 174.7369 | +1.5 | +10.8 | +5.0 | - | BERJALAN | PROFIT 5.0 pip | 45 mnt |
| ANALISA CADANGAN (bukan sinyal) | EUR/AUD | BUY | 1.65299 | 1.65116 | 1.65574 | +20.2 | +10.7 | +7.1 | - | BERJALAN | PROFIT 7.1 pip | 45 mnt |
| ANALISA CADANGAN (bukan sinyal) | AUD/USD | BUY | 0.66372 | 0.6628 | 0.6651 | -6.3 | -3.9 | - | - | SL kena | LOSS 9.2 pip | 45 mnt |
| ANALISA CADANGAN (bukan sinyal) | NZD/USD | BUY | 0.54802 | 0.54712 | 0.54937 | -0.9 | -0.3 | -2.2 | - | BERJALAN | LOSS 2.2 pip | 30 mnt |
| ANALISA CADANGAN (bukan sinyal) | USD/CAD | BUY | 1.43117 | 1.42958 | 1.43356 | +3.8 | +0.2 | +8.9 | - | BERJALAN | PROFIT 8.9 pip | 30 mnt |
| ANALISA CADANGAN (bukan sinyal) | GBP/USD | BUY | 1.31161 | 1.30966 | 1.31454 | -3.2 | -1.8 | -5.0 | - | BERJALAN | LOSS 5.0 pip | 30 mnt |
| ANALISA CADANGAN (bukan sinyal) | EUR/USD | BUY | 1.09708 | 1.09533 | 1.09971 | +3.1 | +0.9 | -5.0 | - | BERJALAN | LOSS 5.0 pip | 30 mnt |
| ANALISA CADANGAN (bukan sinyal) | EUR/GBP | SELL | 0.83644 | 0.83688 | 0.83577 | - | - | - | - | SL kena | LOSS 4.4 pip | 15 mnt |
| ANALISA CADANGAN (bukan sinyal) | EUR/CHF | SELL | 0.91655 | 0.91796 | 0.91443 | +4.3 | +5.8 | +6.5 | - | BERJALAN | PROFIT 6.5 pip | 15 mnt |
| ANALISA CADANGAN (bukan sinyal) | USD/JPY | SELL | 159.0815 | 159.36747 | 158.65255 | +2.6 | -8.9 | -12.1 | - | BERJALAN | LOSS 12.1 pip | 15 mnt |

## Evaluasi 1 jam (entry dan analisa cadangan)
Dibuat setelah 60 menit atau saat SL/TP kena. MFE = gerak terbaik, MAE = gerak terburuk, dalam pip.
| Sumber | Pair | Arah | Hasil | Pip akhir | MFE (pip) | MAE (pip) | Ditutup (UTC) |
|---|---|---|---|---|---|---|---|
| ANALISA CADANGAN (bukan sinyal) | AUD/USD | BUY | SL kena · menit 45 | LOSS 9.2 pip | -0.3 | -9.8 | 2026-11-24T16:45:28Z |
| ANALISA CADANGAN (bukan sinyal) | EUR/GBP | SELL | SL kena · menit 15 | LOSS 4.4 pip | 0.0 | -5.0 | 2026-11-24T16:45:28Z |

## Level analisa cadangan (BUKAN sinyal, tanpa statistik)
Level S/R terdekat untuk konteks scalping. Tidak mengubah label atau keputusan apa pun.
- **EUR/USD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 1.09599 (0.82 ATR, 22 bar sentuh)
  - M15: resistance 1.09689 (0.36 ATR, 30 bar sentuh) · support tidak ada dalam jarak
- **GBP/USD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 1.31042 (0.79 ATR, 29 bar sentuh)
  - M15: resistance 1.31158 (0.49 ATR, 18 bar sentuh) · support 1.31037 (0.76 ATR, 27 bar sentuh)
- **USD/JPY** (NO TRADE)
  - H1: resistance 159.26955 (0.96 ATR, 56 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance 159.28008 (0.65 ATR, 35 bar sentuh) · support tidak ada dalam jarak
- **USD/CHF** (NO TRADE)
  - H1: resistance 0.83669 (1.01 ATR, 4 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance 0.8354 (0.16 ATR, 6 bar sentuh) · support tidak ada dalam jarak
- **AUD/USD** (NO TRADE)
  - H1: resistance 0.66551 (1.36 ATR, 21 bar sentuh) · support 0.66346 (0.2 ATR, 26 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 0.66284 (0.4 ATR, 75 bar sentuh)
- **USD/CAD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 1.43026 (0.66 ATR, 41 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 1.43129 (0.81 ATR, 14 bar sentuh)
- **NZD/USD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 0.54756 (0.52 ATR, 17 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 0.54763 (0.35 ATR, 40 bar sentuh)
- **EUR/GBP** (NO TRADE)
  - H1: resistance 0.83661 (0.31 ATR, 31 bar sentuh) · support 0.83594 (0.93 ATR, 10 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support tidak ada dalam jarak
- **EUR/JPY** (NO TRADE)
  - H1: resistance 174.743 (0.82 ATR, 31 bar sentuh) · support 174.5197 (0.03 ATR, 25 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 174.45763 (0.87 ATR, 23 bar sentuh)
- **EUR/CHF** (NO TRADE)
  - H1: resistance 0.91743 (0.84 ATR, 11 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance tidak ada dalam jarak · support tidak ada dalam jarak
- **EUR/AUD** (NO TRADE)
  - H1: resistance 1.65596 (0.98 ATR, 11 bar sentuh) · support 1.65267 (0.11 ATR, 16 bar sentuh)
  - M15: resistance 1.65416 (0.26 ATR, 45 bar sentuh) · support tidak ada dalam jarak
- **EUR/CAD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support tidak ada dalam jarak
  - M15: resistance tidak ada dalam jarak · support 1.56952 (0.67 ATR, 17 bar sentuh)
- **EUR/NZD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 1.99896 (1.12 ATR, 48 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support tidak ada dalam jarak
- **XAU/USD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support tidak ada dalam jarak
  - M15: resistance 3575.443 (0.02 ATR, 14 bar sentuh) · support 3568.257 (0.56 ATR, 13 bar sentuh)
- **XAU/AUD** (NO TRADE)
  - H1: resistance 5394.819 (0.6 ATR, 9 bar sentuh) · support 5377.382 (0.0 ATR, 13 bar sentuh)
  - M15: resistance 5405.348 (0.83 ATR, 8 bar sentuh) · support 5386.528 (0.3 ATR, 14 bar sentuh)

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

