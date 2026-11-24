# Laporan Scanner Adaptive Forex

- Waktu eksekusi: 2026-11-24T18:45:25Z
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
| EUR/CHF | **SELL** | 0.91743 resistance (0.71 ATR, 12 sentuh) | 0.91666 | 0.91797 | 0.9147 | 13.1 pip |
| EUR/JPY | **BUY** | 174.5197 support (0.72 ATR, 27 sentuh) | 174.7055 | 174.39115 | 175.17702 | 31.4 pip |

## Pemantauan 15 menit (entry dan analisa cadangan)
Nilai di kolom 15m-60m = pip dari entry pada close candle M15 ke-1 sampai ke-4. Jika SL dan TP kena di candle yang sama, dihitung SL. Analisa cadangan BUKAN sinyal.
| Sumber | Pair | Arah | Entry | SL | TP | 15m | 30m | 45m | 60m | Hasil | Pip sekarang | Umur |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ANALISA CADANGAN (bukan sinyal) | EUR/NZD | BUY | 1.99962 | 1.99766 | 2.00256 | -11.8 | -8.7 | +1.2 | - | BERJALAN | PROFIT 1.2 pip | 45 mnt |
| ANALISA CADANGAN (bukan sinyal) | USD/JPY | SELL | 159.2115 | 159.36338 | 158.98367 | -3.5 | -6.7 | -7.3 | - | BERJALAN | LOSS 7.3 pip | 45 mnt |
| ANALISA CADANGAN (bukan sinyal) | EUR/AUD | SELL | 1.65183 | 1.65416 | 1.64834 | +9.0 | +11.4 | +8.2 | - | BERJALAN | PROFIT 8.2 pip | 45 mnt |
| ANALISA CADANGAN (bukan sinyal) | XAU/AUD | SELL | 5369.268 | 5391.51189 | 5335.90216 | +78.0 | +75.2 | +159.5 | - | BERJALAN | PROFIT 159.5 pip | 30 mnt |
| ANALISA CADANGAN (bukan sinyal) | EUR/CAD | SELL | 1.56656 | 1.56831 | 1.56393 | +6.7 | +11.4 | +13.0 | - | BERJALAN | PROFIT 13.0 pip | 30 mnt |
| ANALISA CADANGAN (bukan sinyal) | USD/CAD | BUY | 1.42772 | 1.42608 | 1.43018 | -2.8 | -4.4 | -5.9 | - | BERJALAN | LOSS 5.9 pip | 30 mnt |
| ANALISA CADANGAN (bukan sinyal) | EUR/GBP | BUY | 0.83625 | 0.83568 | 0.83711 | -0.7 | -1.2 | -1.8 | - | BERJALAN | LOSS 1.8 pip | 15 mnt |
| ANALISA CADANGAN (bukan sinyal) | NZD/USD | SELL | 0.54877 | 0.54977 | 0.54727 | -2.0 | -0.1 | +2.6 | - | BERJALAN | PROFIT 2.6 pip | 15 mnt |
| ANALISA CADANGAN (bukan sinyal) | AUD/USD | BUY | 0.6643 | 0.66281 | 0.66653 | +2.2 | +2.0 | +0.7 | - | BERJALAN | PROFIT 0.7 pip | 15 mnt |

## Evaluasi 1 jam (entry dan analisa cadangan)
Dibuat setelah 60 menit atau saat SL/TP kena. MFE = gerak terbaik, MAE = gerak terburuk, dalam pip.
Belum ada evaluasi yang selesai di run ini.

## Level analisa cadangan (BUKAN sinyal, tanpa statistik)
Level S/R terdekat untuk konteks scalping. Tidak mengubah label atau keputusan apa pun.
- **EUR/USD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 1.09599 (1.03 ATR, 23 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support tidak ada dalam jarak
- **GBP/USD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 1.31042 (1.18 ATR, 30 bar sentuh)
  - M15: resistance 1.31242 (0.64 ATR, 17 bar sentuh) · support 1.31162 (0.37 ATR, 22 bar sentuh)
- **USD/JPY** (NO TRADE)
  - H1: resistance 159.26545 (0.28 ATR, 58 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance tidak ada dalam jarak · support 159.25192 (0.35 ATR, 36 bar sentuh)
- **USD/CHF** (NO TRADE)
  - H1: resistance 0.83669 (1.04 ATR, 4 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance 0.83591 (0.77 ATR, 9 bar sentuh) · support 0.83525 (0.15 ATR, 12 bar sentuh)
- **AUD/USD** (NO TRADE)
  - H1: resistance 0.66553 (0.94 ATR, 21 bar sentuh) · support 0.66346 (0.65 ATR, 28 bar sentuh)
  - M15: resistance 0.66489 (0.86 ATR, 24 bar sentuh) · support tidak ada dalam jarak
- **USD/CAD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 1.42685 (0.56 ATR, 9 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support tidak ada dalam jarak
- **NZD/USD** (NO TRADE)
  - H1: resistance 0.54933 (0.64 ATR, 55 bar sentuh) · support 0.54756 (1.38 ATR, 18 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support tidak ada dalam jarak
- **EUR/GBP** (NO TRADE)
  - H1: resistance 0.83661 (0.68 ATR, 33 bar sentuh) · support 0.83594 (0.6 ATR, 10 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support tidak ada dalam jarak
- **EUR/JPY** (NO TRADE)
  - H1: resistance 174.903 (0.77 ATR, 33 bar sentuh) · support 174.5197 (0.72 ATR, 27 bar sentuh)
  - M15: resistance 174.798 (0.74 ATR, 12 bar sentuh) · support 174.6385 (0.7 ATR, 21 bar sentuh)
- **EUR/CHF** (NO TRADE)
  - H1: resistance 0.91743 (0.71 ATR, 12 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance tidak ada dalam jarak · support tidak ada dalam jarak
- **EUR/AUD** (NO TRADE)
  - H1: resistance 1.65267 (0.28 ATR, 18 bar sentuh) · support 1.64946 (0.8 ATR, 18 bar sentuh)
  - M15: resistance 1.65229 (0.87 ATR, 28 bar sentuh) · support 1.65031 (0.48 ATR, 20 bar sentuh)
- **EUR/CAD** (NO TRADE)
  - H1: resistance 1.56742 (0.48 ATR, 12 bar sentuh) · support 1.56439 (1.21 ATR, 2 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 1.56437 (0.88 ATR, 5 bar sentuh)
- **EUR/NZD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 1.99896 (0.26 ATR, 49 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 1.99965 (0.07 ATR, 14 bar sentuh)
- **XAU/USD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support tidak ada dalam jarak
  - M15: resistance 3559.9175 (0.3 ATR, 8 bar sentuh) · support tidak ada dalam jarak
- **XAU/AUD** (NO TRADE)
  - H1: resistance 5377.382 (0.29 ATR, 15 bar sentuh) · support tidak ada dalam jarak
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

