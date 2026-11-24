# Laporan Scanner Adaptive Forex

- Waktu eksekusi: 2026-11-24T16:00:49Z
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
| XAU/AUD | **BUY** | 5377.382 support (0.0 ATR, 13 sentuh) | 5377.3865 | 5362.80985 | 5399.25147 | 145.8 pip |
| EUR/JPY | **BUY** | 174.5197 support (0.03 ATR, 25 sentuh) | 174.5275 | 174.3879 | 174.7369 | 14.0 pip |
| EUR/AUD | **BUY** | 1.65267 support (0.11 ATR, 16 sentuh) | 1.65299 | 1.65116 | 1.65574 | 18.3 pip |
| AUD/USD | **BUY** | 0.66346 support (0.2 ATR, 26 sentuh) | 0.66372 | 0.6628 | 0.6651 | 9.2 pip |
| EUR/GBP | **SELL** | 0.83661 resistance (0.31 ATR, 31 sentuh) | 0.83644 | 0.83688 | 0.83577 | 4.5 pip |

## Pemantauan 15 menit (entry dan analisa cadangan)
Nilai di kolom 15m-60m = pip dari entry pada close candle M15 ke-1 sampai ke-4. Jika SL dan TP kena di candle yang sama, dihitung SL. Analisa cadangan BUKAN sinyal.
| Sumber | Pair | Arah | Entry | SL | TP | 15m | 30m | 45m | 60m | Hasil | Pip sekarang | Umur |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ANALISA CADANGAN (bukan sinyal) | EUR/GBP | SELL | 0.83683 | 0.83725 | 0.83619 | +3.8 | +1.7 | +1.8 | +3.8 | Selesai 60 menit | PROFIT 3.8 pip | 45 mnt |
| ANALISA CADANGAN (bukan sinyal) | EUR/JPY | BUY | 174.7435 | 174.61248 | 174.94003 | -9.0 | - | - | - | SL kena | LOSS 13.1 pip | 15 mnt |
| ANALISA CADANGAN (bukan sinyal) | AUD/USD | BUY | 0.66557 | 0.6649 | 0.66658 | - | - | - | - | SL kena | LOSS 6.7 pip | 15 mnt |
| ANALISA CADANGAN (bukan sinyal) | EUR/CHF | SELL | 0.91729 | 0.91794 | 0.91632 | - | - | - | - | SL kena | LOSS 6.5 pip | 15 mnt |
| ANALISA CADANGAN (bukan sinyal) | EUR/NZD | BUY | 1.99934 | 1.99769 | 2.00182 | -3.2 | +17.7 | - | - | TP kena | PROFIT 24.8 pip | 15 mnt |
| ANALISA CADANGAN (bukan sinyal) | EUR/AUD | BUY | 1.6489 | 1.64695 | 1.65182 | -0.1 | - | - | - | TP kena | PROFIT 29.2 pip | 15 mnt |

## Evaluasi 1 jam (entry dan analisa cadangan)
Dibuat setelah 60 menit atau saat SL/TP kena. MFE = gerak terbaik, MAE = gerak terburuk, dalam pip.
| Sumber | Pair | Arah | Hasil | Pip akhir | MFE (pip) | MAE (pip) | Ditutup (UTC) |
|---|---|---|---|---|---|---|---|
| ANALISA CADANGAN (bukan sinyal) | EUR/GBP | SELL | Selesai 60 menit | PROFIT 3.8 pip | 4.8 | -0.5 | 2026-11-24T16:00:49Z |
| ANALISA CADANGAN (bukan sinyal) | EUR/JPY | BUY | SL kena · menit 30 | LOSS 13.1 pip | 6.3 | -17.9 | 2026-11-24T16:00:49Z |
| ANALISA CADANGAN (bukan sinyal) | AUD/USD | BUY | SL kena · menit 15 | LOSS 6.7 pip | 0.5 | -9.8 | 2026-11-24T16:00:49Z |
| ANALISA CADANGAN (bukan sinyal) | EUR/CHF | SELL | SL kena · menit 15 | LOSS 6.5 pip | 1.3 | -7.0 | 2026-11-24T16:00:49Z |
| ANALISA CADANGAN (bukan sinyal) | EUR/NZD | BUY | TP kena · menit 45 | PROFIT 24.8 pip | 28.0 | -3.6 | 2026-11-24T16:00:49Z |
| ANALISA CADANGAN (bukan sinyal) | EUR/AUD | BUY | TP kena · menit 30 | PROFIT 29.2 pip | 33.5 | -3.2 | 2026-11-24T16:00:49Z |

## Level analisa cadangan (BUKAN sinyal, tanpa statistik)
Level S/R terdekat untuk konteks scalping. Tidak mengubah label atau keputusan apa pun.
- **EUR/USD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 1.09599 (0.82 ATR, 22 bar sentuh)
  - M15: resistance 1.09792 (0.95 ATR, 29 bar sentuh) · support 1.09648 (0.68 ATR, 28 bar sentuh)
- **GBP/USD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 1.31042 (0.79 ATR, 29 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 1.31096 (0.66 ATR, 30 bar sentuh)
- **USD/JPY** (NO TRADE)
  - H1: resistance 159.26955 (0.96 ATR, 56 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance tidak ada dalam jarak · support 158.96902 (0.94 ATR, 62 bar sentuh)
- **USD/CHF** (NO TRADE)
  - H1: resistance 0.83669 (1.01 ATR, 4 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance tidak ada dalam jarak · support 0.8354 (0.01 ATR, 4 bar sentuh)
- **AUD/USD** (NO TRADE)
  - H1: resistance 0.66551 (1.36 ATR, 21 bar sentuh) · support 0.66346 (0.2 ATR, 26 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 0.66349 (0.32 ATR, 47 bar sentuh)
- **USD/CAD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 1.43026 (0.66 ATR, 41 bar sentuh)
  - M15: resistance 1.43133 (0.18 ATR, 14 bar sentuh) · support tidak ada dalam jarak
- **NZD/USD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 0.54756 (0.52 ATR, 17 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 0.54764 (0.77 ATR, 37 bar sentuh)
- **EUR/GBP** (NO TRADE)
  - H1: resistance 0.83661 (0.31 ATR, 31 bar sentuh) · support 0.83594 (0.93 ATR, 10 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support tidak ada dalam jarak
- **EUR/JPY** (NO TRADE)
  - H1: resistance 174.743 (0.82 ATR, 31 bar sentuh) · support 174.5197 (0.03 ATR, 25 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 174.4595 (0.49 ATR, 24 bar sentuh)
- **EUR/CHF** (NO TRADE)
  - H1: resistance 0.91743 (0.84 ATR, 11 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance tidak ada dalam jarak · support tidak ada dalam jarak
- **EUR/AUD** (NO TRADE)
  - H1: resistance 1.65596 (0.98 ATR, 11 bar sentuh) · support 1.65267 (0.11 ATR, 16 bar sentuh)
  - M15: resistance 1.65411 (0.64 ATR, 42 bar sentuh) · support tidak ada dalam jarak
- **EUR/CAD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support tidak ada dalam jarak
  - M15: resistance tidak ada dalam jarak · support 1.56952 (0.47 ATR, 16 bar sentuh)
- **EUR/NZD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 1.99896 (1.12 ATR, 48 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support tidak ada dalam jarak
- **XAU/USD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support tidak ada dalam jarak
  - M15: resistance 3575.443 (0.49 ATR, 16 bar sentuh) · support 3568.257 (0.07 ATR, 13 bar sentuh)
- **XAU/AUD** (NO TRADE)
  - H1: resistance 5394.819 (0.6 ATR, 9 bar sentuh) · support 5377.382 (0.0 ATR, 13 bar sentuh)
  - M15: resistance 5386.528 (0.54 ATR, 11 bar sentuh) · support 5374.86217 (0.15 ATR, 11 bar sentuh)

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

