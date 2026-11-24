# Laporan Scanner Adaptive Forex

- Waktu eksekusi: 2026-11-24T17:30:37Z
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
| AUD/USD | **SELL** | 0.66346 resistance (0.18 ATR, 27 sentuh) | 0.66323 | 0.66411 | 0.66191 | 8.8 pip |
| USD/CAD | **BUY** | 1.43026 support (0.73 ATR, 41 sentuh) | 1.43127 | 1.42957 | 1.43382 | 17.0 pip |
| EUR/NZD | **BUY** | 1.99896 support (0.84 ATR, 48 sentuh) | 2.00114 | 1.99766 | 2.00636 | 34.8 pip |

## Pemantauan 15 menit (entry dan analisa cadangan)
Nilai di kolom 15m-60m = pip dari entry pada close candle M15 ke-1 sampai ke-4. Jika SL dan TP kena di candle yang sama, dihitung SL. Analisa cadangan BUKAN sinyal.
| Sumber | Pair | Arah | Entry | SL | TP | 15m | 30m | 45m | 60m | Hasil | Pip sekarang | Umur |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ANALISA CADANGAN (bukan sinyal) | XAU/AUD | SELL | 5374.964 | 5391.8385 | 5349.65225 | -31.2 | +76.4 | - | - | BERJALAN | PROFIT 76.4 pip | 30 mnt |
| ANALISA CADANGAN (bukan sinyal) | EUR/JPY | BUY | 174.5555 | 174.38896 | 174.80532 | +4.8 | +14.7 | - | - | BERJALAN | PROFIT 14.7 pip | 30 mnt |
| ANALISA CADANGAN (bukan sinyal) | AUD/USD | SELL | 0.66323 | 0.66411 | 0.66191 | -7.0 | - | - | - | SL kena | LOSS 8.8 pip | 30 mnt |
| ANALISA CADANGAN (bukan sinyal) | EUR/AUD | BUY | 1.65372 | 1.65118 | 1.65753 | -22.3 | -20.0 | - | - | BERJALAN | LOSS 20.0 pip | 30 mnt |
| ANALISA CADANGAN (bukan sinyal) | EUR/GBP | SELL | 0.83639 | 0.83688 | 0.83565 | +1.1 | +1.4 | - | - | BERJALAN | PROFIT 1.4 pip | 30 mnt |
| ANALISA CADANGAN (bukan sinyal) | USD/JPY | SELL | 159.1515 | 159.36264 | 158.83478 | -8.5 | -12.4 | - | - | BERJALAN | LOSS 12.4 pip | 15 mnt |
| ANALISA CADANGAN (bukan sinyal) | NZD/USD | BUY | 0.54807 | 0.54713 | 0.54949 | +3.4 | +6.4 | - | - | BERJALAN | PROFIT 6.4 pip | 15 mnt |
| ANALISA CADANGAN (bukan sinyal) | GBP/USD | BUY | 1.3113 | 1.30966 | 1.31375 | -1.9 | +4.2 | - | - | BERJALAN | PROFIT 4.2 pip | 15 mnt |
| ANALISA CADANGAN (bukan sinyal) | EUR/USD | BUY | 1.09678 | 1.09533 | 1.09896 | -2.8 | +1.3 | - | - | BERJALAN | PROFIT 1.3 pip | 15 mnt |
| ANALISA CADANGAN (bukan sinyal) | USD/CAD | BUY | 1.43127 | 1.42957 | 1.43382 | -6.5 | - | - | - | SL kena | LOSS 17.0 pip | 15 mnt |

## Evaluasi 1 jam (entry dan analisa cadangan)
Dibuat setelah 60 menit atau saat SL/TP kena. MFE = gerak terbaik, MAE = gerak terburuk, dalam pip.
| Sumber | Pair | Arah | Hasil | Pip akhir | MFE (pip) | MAE (pip) | Ditutup (UTC) |
|---|---|---|---|---|---|---|---|
| ANALISA CADANGAN (bukan sinyal) | AUD/USD | SELL | SL kena · menit 30 | LOSS 8.8 pip | 1.1 | -9.2 | 2026-11-24T17:30:37Z |
| ANALISA CADANGAN (bukan sinyal) | USD/CAD | BUY | SL kena · menit 30 | LOSS 17.0 pip | 0.8 | -29.9 | 2026-11-24T17:30:37Z |

## Level analisa cadangan (BUKAN sinyal, tanpa statistik)
Level S/R terdekat untuk konteks scalping. Tidak mengubah label atau keputusan apa pun.
- **EUR/USD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 1.09599 (0.6 ATR, 23 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 1.09684 (0.08 ATR, 33 bar sentuh)
- **GBP/USD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 1.31042 (0.59 ATR, 30 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 1.31162 (0.1 ATR, 20 bar sentuh)
- **USD/JPY** (NO TRADE)
  - H1: resistance 159.26333 (0.56 ATR, 58 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance 159.28008 (0.04 ATR, 37 bar sentuh) · support tidak ada dalam jarak
- **USD/CHF** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support tidak ada dalam jarak
  - M15: resistance tidak ada dalam jarak · support 0.8354 (0.37 ATR, 9 bar sentuh)
- **AUD/USD** (NO TRADE)
  - H1: resistance 0.66346 (0.18 ATR, 27 bar sentuh) · support 0.66205 (0.91 ATR, 21 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support tidak ada dalam jarak
- **USD/CAD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 1.43026 (0.73 ATR, 41 bar sentuh)
  - M15: resistance 1.42895 (0.33 ATR, 3 bar sentuh) · support tidak ada dalam jarak
- **NZD/USD** (NO TRADE)
  - H1: resistance 0.54933 (1.44 ATR, 55 bar sentuh) · support 0.54756 (0.58 ATR, 18 bar sentuh)
  - M15: resistance 0.54891 (0.42 ATR, 2 bar sentuh) · support tidak ada dalam jarak
- **EUR/GBP** (NO TRADE)
  - H1: resistance 0.83661 (0.4 ATR, 32 bar sentuh) · support 0.83594 (0.83 ATR, 10 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 0.83605 (0.56 ATR, 11 bar sentuh)
- **EUR/JPY** (NO TRADE)
  - H1: resistance 174.903 (1.33 ATR, 33 bar sentuh) · support 174.5197 (0.14 ATR, 26 bar sentuh)
  - M15: resistance 174.798 (0.71 ATR, 12 bar sentuh) · support tidak ada dalam jarak
- **EUR/CHF** (NO TRADE)
  - H1: resistance 0.91743 (1.45 ATR, 11 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance tidak ada dalam jarak · support tidak ada dalam jarak
- **EUR/AUD** (NO TRADE)
  - H1: resistance 1.65596 (0.75 ATR, 11 bar sentuh) · support 1.65267 (0.35 ATR, 17 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 1.65031 (0.81 ATR, 21 bar sentuh)
- **EUR/CAD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 1.56742 (1.34 ATR, 10 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 1.56638 (0.44 ATR, 34 bar sentuh)
- **EUR/NZD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 1.99896 (0.84 ATR, 48 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support tidak ada dalam jarak
- **XAU/USD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support tidak ada dalam jarak
  - M15: resistance 3568.257 (0.33 ATR, 14 bar sentuh) · support 3558.8285 (0.45 ATR, 6 bar sentuh)
- **XAU/AUD** (NO TRADE)
  - H1: resistance 5377.382 (0.08 ATR, 14 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance 5371.05867 (0.23 ATR, 8 bar sentuh) · support tidak ada dalam jarak

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

