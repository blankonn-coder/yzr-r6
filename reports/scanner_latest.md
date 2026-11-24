# Laporan Scanner Adaptive Forex

- Waktu eksekusi: 2026-11-24T19:00:52Z
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
| EUR/USD | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.09655 | — | 168/180 | 2026-11-24T18:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| GBP/USD | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.31146 | — | 168/180 | 2026-11-24T18:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| USD/JPY | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 159.2865 | — | 168/180 | 2026-11-24T18:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |
| USD/CHF | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.83551 | — | 168/180 | 2026-11-24T18:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| AUD/USD | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.66416 | — | 168/180 | 2026-11-24T18:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |
| USD/CAD | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.42727 | — | 168/180 | 2026-11-24T18:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| NZD/USD | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.54831 | — | 168/180 | 2026-11-24T18:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| EUR/GBP | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.83613 | — | 168/180 | 2026-11-24T18:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |
| EUR/JPY | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 174.6665 | — | 168/180 | 2026-11-24T18:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| EUR/CHF | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.91616 | — | 168/180 | 2026-11-24T18:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| EUR/AUD | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.65099 | — | 168/180 | 2026-11-24T18:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| EUR/CAD | MIXED | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.56493 | — | 168/180 | 2026-11-24T18:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime MIXED belum punya metode prioritas di ranking |
| EUR/NZD | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.99985 | — | 168/180 | 2026-11-24T18:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |
| XAU/USD | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 3555.1005 | — | 168/180 | 2026-11-24T18:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |
| XAU/AUD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 5352.613 | — | 168/180 | 2026-11-24T18:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |

## Saran analisa cadangan (BUKAN sinyal, tidak divalidasi backtest)
3 pair dengan level H1 terdekat. BUY dari support, SELL dari resistance. SL 0.5 ATR di seberang level, TP 1.5R. Tanpa cek spread, news, atau batas risiko §9. Tidak mengubah label.
| Pair | Arah | Level H1 (jarak, sentuhan) | Entry | SL | TP | Risiko SL |
|---|---|---|---|---|---|---|
| USD/JPY | **BUY** | 159.25986 support (0.14 ATR, 59 sentuh) | 159.2865 | 159.16528 | 159.46834 | 12.1 pip |
| EUR/GBP | **BUY** | 0.83601 support (0.24 ATR, 13 sentuh) | 0.83613 | 0.83575 | 0.8367 | 3.8 pip |
| USD/CAD | **BUY** | 1.42685 support (0.27 ATR, 9 sentuh) | 1.42727 | 1.42609 | 1.42904 | 11.8 pip |

## Pemantauan 15 menit (entry dan analisa cadangan)
Nilai di kolom 15m-60m = pip dari entry pada close candle M15 ke-1 sampai ke-4. Jika SL dan TP kena di candle yang sama, dihitung SL. Analisa cadangan BUKAN sinyal.
| Sumber | Pair | Arah | Entry | SL | TP | 15m | 30m | 45m | 60m | Hasil | Pip sekarang | Umur |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ANALISA CADANGAN (bukan sinyal) | EUR/NZD | BUY | 1.99962 | 1.99766 | 2.00256 | -11.8 | -8.7 | +1.2 | +2.3 | Selesai 60 menit | PROFIT 2.3 pip | 60 mnt |
| ANALISA CADANGAN (bukan sinyal) | USD/JPY | SELL | 159.2115 | 159.36338 | 158.98367 | -3.5 | -6.7 | -7.3 | -7.5 | Selesai 60 menit | LOSS 7.5 pip | 60 mnt |
| ANALISA CADANGAN (bukan sinyal) | EUR/AUD | SELL | 1.65183 | 1.65416 | 1.64834 | +9.0 | +11.4 | +8.2 | +8.4 | Selesai 60 menit | PROFIT 8.4 pip | 60 mnt |
| ANALISA CADANGAN (bukan sinyal) | XAU/AUD | SELL | 5369.268 | 5391.51189 | 5335.90216 | +78.0 | +75.2 | +159.5 | +166.5 | Selesai 60 menit | PROFIT 166.5 pip | 45 mnt |
| ANALISA CADANGAN (bukan sinyal) | EUR/CAD | SELL | 1.56656 | 1.56831 | 1.56393 | +6.7 | +11.4 | +13.0 | +16.3 | Selesai 60 menit | PROFIT 16.3 pip | 45 mnt |
| ANALISA CADANGAN (bukan sinyal) | USD/CAD | BUY | 1.42772 | 1.42608 | 1.43018 | -2.8 | -4.4 | -5.9 | -4.6 | Selesai 60 menit | LOSS 4.6 pip | 45 mnt |
| ANALISA CADANGAN (bukan sinyal) | EUR/GBP | BUY | 0.83625 | 0.83568 | 0.83711 | -0.7 | -1.2 | -1.8 | -1.2 | Selesai 60 menit | LOSS 1.2 pip | 30 mnt |
| ANALISA CADANGAN (bukan sinyal) | NZD/USD | SELL | 0.54877 | 0.54977 | 0.54727 | -2.0 | -0.1 | +2.6 | +4.6 | Selesai 60 menit | PROFIT 4.6 pip | 30 mnt |
| ANALISA CADANGAN (bukan sinyal) | AUD/USD | BUY | 0.6643 | 0.66281 | 0.66653 | +2.2 | +2.0 | +0.7 | -1.4 | Selesai 60 menit | LOSS 1.4 pip | 30 mnt |
| ANALISA CADANGAN (bukan sinyal) | EUR/CHF | SELL | 0.91666 | 0.91797 | 0.9147 | +2.6 | +4.9 | +3.8 | +5.0 | Selesai 60 menit | PROFIT 5.0 pip | 15 mnt |
| ANALISA CADANGAN (bukan sinyal) | EUR/JPY | BUY | 174.7055 | 174.39115 | 175.17702 | -0.2 | +0.3 | +1.0 | -3.9 | Selesai 60 menit | LOSS 3.9 pip | 15 mnt |

## Evaluasi 1 jam (entry dan analisa cadangan)
Dibuat setelah 60 menit atau saat SL/TP kena. MFE = gerak terbaik, MAE = gerak terburuk, dalam pip.
| Sumber | Pair | Arah | 15m | 30m | 45m | 60m | Hasil | Pip akhir | MFE (pip) | MAE (pip) | Ditutup (UTC) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ANALISA CADANGAN (bukan sinyal) | EUR/NZD | BUY | -11.8 | -8.7 | +1.2 | +2.3 | Selesai 60 menit | PROFIT 2.3 pip | 3.6 | -14.3 | 2026-11-24T19:00:52Z |
| ANALISA CADANGAN (bukan sinyal) | USD/JPY | SELL | -3.5 | -6.7 | -7.3 | -7.5 | Selesai 60 menit | LOSS 7.5 pip | 0.6 | -9.6 | 2026-11-24T19:00:52Z |
| ANALISA CADANGAN (bukan sinyal) | EUR/AUD | SELL | +9.0 | +11.4 | +8.2 | +8.4 | Selesai 60 menit | PROFIT 8.4 pip | 13.8 | -0.5 | 2026-11-24T19:00:52Z |
| ANALISA CADANGAN (bukan sinyal) | XAU/AUD | SELL | +78.0 | +75.2 | +159.5 | +166.5 | Selesai 60 menit | PROFIT 166.5 pip | 206.6 | -15.6 | 2026-11-24T19:00:52Z |
| ANALISA CADANGAN (bukan sinyal) | EUR/CAD | SELL | +6.7 | +11.4 | +13.0 | +16.3 | Selesai 60 menit | PROFIT 16.3 pip | 18.3 | -0.3 | 2026-11-24T19:00:52Z |
| ANALISA CADANGAN (bukan sinyal) | USD/CAD | BUY | -2.8 | -4.4 | -5.9 | -4.6 | Selesai 60 menit | LOSS 4.6 pip | 0.8 | -11.2 | 2026-11-24T19:00:52Z |
| ANALISA CADANGAN (bukan sinyal) | EUR/GBP | BUY | -0.7 | -1.2 | -1.8 | -1.2 | Selesai 60 menit | LOSS 1.2 pip | 0.9 | -2.5 | 2026-11-24T19:00:52Z |
| ANALISA CADANGAN (bukan sinyal) | NZD/USD | SELL | -2.0 | -0.1 | +2.6 | +4.6 | Selesai 60 menit | PROFIT 4.6 pip | 4.7 | -3.3 | 2026-11-24T19:00:52Z |
| ANALISA CADANGAN (bukan sinyal) | AUD/USD | BUY | +2.2 | +2.0 | +0.7 | -1.4 | Selesai 60 menit | LOSS 1.4 pip | 4.2 | -1.5 | 2026-11-24T19:00:52Z |
| ANALISA CADANGAN (bukan sinyal) | EUR/CHF | SELL | +2.6 | +4.9 | +3.8 | +5.0 | Selesai 60 menit | PROFIT 5.0 pip | 5.7 | -0.4 | 2026-11-24T19:00:52Z |
| ANALISA CADANGAN (bukan sinyal) | EUR/JPY | BUY | -0.2 | +0.3 | +1.0 | -3.9 | Selesai 60 menit | LOSS 3.9 pip | 5.4 | -4.7 | 2026-11-24T19:00:52Z |

## Level analisa cadangan (BUKAN sinyal, tanpa statistik)
Level S/R terdekat untuk konteks scalping. Tidak mengubah label atau keputusan apa pun.
- **EUR/USD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 1.09599 (0.44 ATR, 22 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 1.09629 (0.38 ATR, 27 bar sentuh)
- **GBP/USD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 1.31042 (0.72 ATR, 30 bar sentuh)
  - M15: resistance 1.31162 (0.21 ATR, 23 bar sentuh) · support tidak ada dalam jarak
- **USD/JPY** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 159.25986 (0.14 ATR, 59 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 159.25192 (0.38 ATR, 37 bar sentuh)
- **USD/CHF** (NO TRADE)
  - H1: resistance 0.83669 (0.98 ATR, 3 bar sentuh) · support 0.8344 (0.9 ATR, 1 bar sentuh)
  - M15: resistance 0.83591 (0.59 ATR, 9 bar sentuh) · support 0.83525 (0.38 ATR, 12 bar sentuh)
- **AUD/USD** (NO TRADE)
  - H1: resistance 0.66553 (1.09 ATR, 21 bar sentuh) · support 0.66284 (1.06 ATR, 29 bar sentuh)
  - M15: resistance 0.66466 (0.87 ATR, 33 bar sentuh) · support tidak ada dalam jarak
- **USD/CAD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 1.42685 (0.27 ATR, 9 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support tidak ada dalam jarak
- **NZD/USD** (NO TRADE)
  - H1: resistance 0.54933 (1.17 ATR, 55 bar sentuh) · support 0.54756 (0.86 ATR, 18 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support tidak ada dalam jarak
- **EUR/GBP** (NO TRADE)
  - H1: resistance 0.83661 (0.93 ATR, 33 bar sentuh) · support 0.83601 (0.24 ATR, 13 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support tidak ada dalam jarak
- **EUR/JPY** (NO TRADE)
  - H1: resistance 174.903 (0.96 ATR, 33 bar sentuh) · support 174.505 (0.66 ATR, 25 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 174.6385 (0.26 ATR, 22 bar sentuh)
- **EUR/CHF** (NO TRADE)
  - H1: resistance 0.91743 (1.22 ATR, 11 bar sentuh) · support 0.91556 (0.58 ATR, 1 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support tidak ada dalam jarak
- **EUR/AUD** (NO TRADE)
  - H1: resistance 1.65267 (0.59 ATR, 18 bar sentuh) · support 1.64946 (0.53 ATR, 18 bar sentuh)
  - M15: resistance 1.65229 (0.93 ATR, 28 bar sentuh) · support 1.65031 (0.49 ATR, 20 bar sentuh)
- **EUR/CAD** (NO TRADE)
  - H1: resistance 1.56742 (1.39 ATR, 12 bar sentuh) · support 1.56439 (0.3 ATR, 3 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 1.56437 (0.57 ATR, 5 bar sentuh)
- **EUR/NZD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 1.99896 (0.35 ATR, 50 bar sentuh)
  - M15: resistance 1.99998 (0.1 ATR, 18 bar sentuh) · support 1.99899 (0.7 ATR, 11 bar sentuh)
- **XAU/USD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support tidak ada dalam jarak
  - M15: resistance 3559.9175 (0.47 ATR, 8 bar sentuh) · support tidak ada dalam jarak
- **XAU/AUD** (NO TRADE)
  - H1: resistance 5377.382 (0.89 ATR, 14 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance tidak ada dalam jarak · support tidak ada dalam jarak

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

