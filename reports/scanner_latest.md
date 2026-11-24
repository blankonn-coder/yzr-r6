# Laporan Scanner Adaptive Forex

- Waktu eksekusi: 2026-11-24T17:00:44Z
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
| EUR/USD | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.09678 | — | 168/180 | 2026-11-24T16:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| GBP/USD | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.3113 | — | 168/180 | 2026-11-24T16:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| USD/JPY | VOLATIL/CHOPPY | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 159.1515 | — | 168/180 | 2026-11-24T16:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime VOLATIL/CHOPPY belum punya metode prioritas di ranking |
| USD/CHF | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.83501 | — | 168/180 | 2026-11-24T16:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| AUD/USD | VOLATIL/CHOPPY | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.66323 | — | 168/180 | 2026-11-24T16:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime VOLATIL/CHOPPY belum punya metode prioritas di ranking |
| USD/CAD | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.43127 | — | 168/180 | 2026-11-24T16:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| NZD/USD | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.54807 | — | 168/180 | 2026-11-24T16:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| EUR/GBP | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.83639 | — | 168/180 | 2026-11-24T16:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |
| EUR/JPY | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 174.5555 | — | 168/180 | 2026-11-24T16:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| EUR/CHF | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.91587 | — | 168/180 | 2026-11-24T16:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| EUR/AUD | MIXED | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.65372 | — | 168/180 | 2026-11-24T16:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime MIXED belum punya metode prioritas di ranking |
| EUR/CAD | MIXED | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.56966 | — | 168/180 | 2026-11-24T16:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime MIXED belum punya metode prioritas di ranking |
| EUR/NZD | VOLATIL/CHOPPY | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 2.00114 | — | 168/180 | 2026-11-24T16:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime VOLATIL/CHOPPY belum punya metode prioritas di ranking |
| XAU/USD | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 3564.9405 | — | 168/180 | 2026-11-24T16:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |
| XAU/AUD | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 5374.964 | — | 168/180 | 2026-11-24T16:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |

## Saran analisa cadangan (BUKAN sinyal, tidak divalidasi backtest)
5 pair dengan level H1 terdekat. BUY dari support, SELL dari resistance. SL 0.5 ATR di seberang level, TP 1.5R. Tanpa cek spread, news, atau batas risiko §9. Tidak mengubah label.
| Pair | Arah | Level H1 (jarak, sentuhan) | Entry | SL | TP | Risiko SL |
|---|---|---|---|---|---|---|
| XAU/AUD | **SELL** | 5377.382 resistance (0.08 ATR, 14 sentuh) | 5374.964 | 5391.8385 | 5349.65225 | 168.7 pip |
| EUR/JPY | **BUY** | 174.5197 support (0.14 ATR, 26 sentuh) | 174.5555 | 174.38896 | 174.80532 | 16.7 pip |
| AUD/USD | **SELL** | 0.66346 resistance (0.18 ATR, 27 sentuh) | 0.66323 | 0.66411 | 0.66191 | 8.8 pip |
| EUR/AUD | **BUY** | 1.65267 support (0.35 ATR, 17 sentuh) | 1.65372 | 1.65118 | 1.65753 | 25.4 pip |
| EUR/GBP | **SELL** | 0.83661 resistance (0.4 ATR, 32 sentuh) | 0.83639 | 0.83688 | 0.83565 | 5.0 pip |

## Pemantauan 15 menit (entry dan analisa cadangan)
Nilai di kolom 15m-60m = pip dari entry pada close candle M15 ke-1 sampai ke-4. Jika SL dan TP kena di candle yang sama, dihitung SL. Analisa cadangan BUKAN sinyal.
| Sumber | Pair | Arah | Entry | SL | TP | 15m | 30m | 45m | 60m | Hasil | Pip sekarang | Umur |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ANALISA CADANGAN (bukan sinyal) | XAU/AUD | BUY | 5377.3865 | 5362.80985 | 5399.25147 | +29.9 | +3.2 | +141.3 | -24.2 | Selesai 60 menit | LOSS 24.2 pip | 60 mnt |
| ANALISA CADANGAN (bukan sinyal) | EUR/JPY | BUY | 174.5275 | 174.3879 | 174.7369 | +1.5 | +10.8 | +5.0 | +2.8 | Selesai 60 menit | PROFIT 2.8 pip | 60 mnt |
| ANALISA CADANGAN (bukan sinyal) | EUR/AUD | BUY | 1.65299 | 1.65116 | 1.65574 | +20.2 | +10.7 | +7.1 | +7.3 | Selesai 60 menit | PROFIT 7.3 pip | 60 mnt |
| ANALISA CADANGAN (bukan sinyal) | NZD/USD | BUY | 0.54802 | 0.54712 | 0.54937 | -0.9 | -0.3 | -2.2 | +0.5 | Selesai 60 menit | PROFIT 0.5 pip | 45 mnt |
| ANALISA CADANGAN (bukan sinyal) | USD/CAD | BUY | 1.43117 | 1.42958 | 1.43356 | +3.8 | +0.2 | +8.9 | +0.9 | Selesai 60 menit | PROFIT 0.9 pip | 45 mnt |
| ANALISA CADANGAN (bukan sinyal) | GBP/USD | BUY | 1.31161 | 1.30966 | 1.31454 | -3.2 | -1.8 | -5.0 | -3.0 | Selesai 60 menit | LOSS 3.0 pip | 45 mnt |
| ANALISA CADANGAN (bukan sinyal) | EUR/USD | BUY | 1.09708 | 1.09533 | 1.09971 | +3.1 | +0.9 | -5.0 | -3.0 | Selesai 60 menit | LOSS 3.0 pip | 45 mnt |
| ANALISA CADANGAN (bukan sinyal) | EUR/CHF | SELL | 0.91655 | 0.91796 | 0.91443 | +4.3 | +5.8 | +6.5 | +6.7 | Selesai 60 menit | PROFIT 6.7 pip | 30 mnt |
| ANALISA CADANGAN (bukan sinyal) | USD/JPY | SELL | 159.0815 | 159.36747 | 158.65255 | +2.6 | -8.9 | -12.1 | -7.0 | Selesai 60 menit | LOSS 7.0 pip | 30 mnt |
| ANALISA CADANGAN (bukan sinyal) | AUD/USD | BUY | 0.66372 | 0.6628 | 0.6651 | -6.3 | -3.9 | - | - | SL kena | LOSS 9.2 pip | 15 mnt |
| ANALISA CADANGAN (bukan sinyal) | EUR/GBP | SELL | 0.83644 | 0.83688 | 0.83577 | - | - | - | - | SL kena | LOSS 4.4 pip | 15 mnt |

## Evaluasi 1 jam (entry dan analisa cadangan)
Dibuat setelah 60 menit atau saat SL/TP kena. MFE = gerak terbaik, MAE = gerak terburuk, dalam pip.
| Sumber | Pair | Arah | Hasil | Pip akhir | MFE (pip) | MAE (pip) | Ditutup (UTC) |
|---|---|---|---|---|---|---|---|
| ANALISA CADANGAN (bukan sinyal) | XAU/AUD | BUY | Selesai 60 menit | LOSS 24.2 pip | 144.9 | -114.1 | 2026-11-24T17:00:44Z |
| ANALISA CADANGAN (bukan sinyal) | EUR/JPY | BUY | Selesai 60 menit | PROFIT 2.8 pip | 13.8 | -9.6 | 2026-11-24T17:00:44Z |
| ANALISA CADANGAN (bukan sinyal) | EUR/AUD | BUY | Selesai 60 menit | PROFIT 7.3 pip | 22.8 | -1.1 | 2026-11-24T17:00:44Z |
| ANALISA CADANGAN (bukan sinyal) | NZD/USD | BUY | Selesai 60 menit | PROFIT 0.5 pip | 2.1 | -5.1 | 2026-11-24T17:00:44Z |
| ANALISA CADANGAN (bukan sinyal) | USD/CAD | BUY | Selesai 60 menit | PROFIT 0.9 pip | 13.0 | -3.8 | 2026-11-24T17:00:44Z |
| ANALISA CADANGAN (bukan sinyal) | GBP/USD | BUY | Selesai 60 menit | LOSS 3.0 pip | 2.5 | -10.7 | 2026-11-24T17:00:44Z |
| ANALISA CADANGAN (bukan sinyal) | EUR/USD | BUY | Selesai 60 menit | LOSS 3.0 pip | 3.7 | -8.6 | 2026-11-24T17:00:44Z |
| ANALISA CADANGAN (bukan sinyal) | EUR/CHF | SELL | Selesai 60 menit | PROFIT 6.7 pip | 9.9 | -2.0 | 2026-11-24T17:00:44Z |
| ANALISA CADANGAN (bukan sinyal) | USD/JPY | SELL | Selesai 60 menit | LOSS 7.0 pip | 5.1 | -18.4 | 2026-11-24T17:00:44Z |
| ANALISA CADANGAN (bukan sinyal) | AUD/USD | BUY | SL kena · menit 45 | LOSS 9.2 pip | -0.3 | -9.8 | 2026-11-24T17:00:44Z |
| ANALISA CADANGAN (bukan sinyal) | EUR/GBP | SELL | SL kena · menit 15 | LOSS 4.4 pip | 0.0 | -5.0 | 2026-11-24T17:00:44Z |

## Level analisa cadangan (BUKAN sinyal, tanpa statistik)
Level S/R terdekat untuk konteks scalping. Tidak mengubah label atau keputusan apa pun.
- **EUR/USD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 1.09599 (0.6 ATR, 23 bar sentuh)
  - M15: resistance 1.09689 (0.13 ATR, 31 bar sentuh) · support tidak ada dalam jarak
- **GBP/USD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 1.31042 (0.59 ATR, 30 bar sentuh)
  - M15: resistance 1.31162 (0.33 ATR, 18 bar sentuh) · support 1.31037 (0.98 ATR, 26 bar sentuh)
- **USD/JPY** (NO TRADE)
  - H1: resistance 159.26333 (0.56 ATR, 58 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance tidak ada dalam jarak · support tidak ada dalam jarak
- **USD/CHF** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support tidak ada dalam jarak
  - M15: resistance 0.8354 (0.43 ATR, 7 bar sentuh) · support 0.8344 (0.68 ATR, 1 bar sentuh)
- **AUD/USD** (NO TRADE)
  - H1: resistance 0.66346 (0.18 ATR, 27 bar sentuh) · support 0.66205 (0.91 ATR, 21 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 0.66284 (0.57 ATR, 73 bar sentuh)
- **USD/CAD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 1.43026 (0.73 ATR, 41 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 1.43119 (0.08 ATR, 14 bar sentuh)
- **NZD/USD** (NO TRADE)
  - H1: resistance 0.54933 (1.44 ATR, 55 bar sentuh) · support 0.54756 (0.58 ATR, 18 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 0.54767 (0.84 ATR, 37 bar sentuh)
- **EUR/GBP** (NO TRADE)
  - H1: resistance 0.83661 (0.4 ATR, 32 bar sentuh) · support 0.83594 (0.83 ATR, 10 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support tidak ada dalam jarak
- **EUR/JPY** (NO TRADE)
  - H1: resistance 174.903 (1.33 ATR, 33 bar sentuh) · support 174.5197 (0.14 ATR, 26 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 174.47062 (0.63 ATR, 25 bar sentuh)
- **EUR/CHF** (NO TRADE)
  - H1: resistance 0.91743 (1.45 ATR, 11 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance tidak ada dalam jarak · support 0.91556 (0.48 ATR, 1 bar sentuh)
- **EUR/AUD** (NO TRADE)
  - H1: resistance 1.65596 (0.75 ATR, 11 bar sentuh) · support 1.65267 (0.35 ATR, 17 bar sentuh)
  - M15: resistance 1.65404 (0.19 ATR, 43 bar sentuh) · support tidak ada dalam jarak
- **EUR/CAD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 1.56742 (1.34 ATR, 10 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 1.56952 (0.13 ATR, 18 bar sentuh)
- **EUR/NZD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 1.99896 (0.84 ATR, 48 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support tidak ada dalam jarak
- **XAU/USD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support tidak ada dalam jarak
  - M15: resistance 3568.257 (0.27 ATR, 13 bar sentuh) · support 3558.8285 (0.5 ATR, 7 bar sentuh)
- **XAU/AUD** (NO TRADE)
  - H1: resistance 5377.382 (0.08 ATR, 14 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance 5386.528 (0.69 ATR, 15 bar sentuh) · support 5371.05867 (0.23 ATR, 7 bar sentuh)

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

