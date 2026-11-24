# Laporan Scanner Adaptive Forex

- Waktu eksekusi: 2026-11-24T13:00:43Z
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
| EUR/USD | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.09602 | — | 168/180 | 2026-11-24T12:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| GBP/USD | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.30966 | — | 168/180 | 2026-11-24T12:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| USD/JPY | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 159.1625 | — | 168/180 | 2026-11-24T12:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |
| USD/CHF | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.83842 | — | 168/180 | 2026-11-24T12:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |
| AUD/USD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.66456 | — | 168/180 | 2026-11-24T12:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| USD/CAD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.43314 | — | 168/180 | 2026-11-24T12:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| NZD/USD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.54706 | — | 168/180 | 2026-11-24T12:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| EUR/GBP | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.83688 | — | 168/180 | 2026-11-24T12:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |
| EUR/JPY | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 174.4455 | — | 168/180 | 2026-11-24T12:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| EUR/CHF | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.91893 | — | 168/180 | 2026-11-24T12:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| EUR/AUD | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.64925 | — | 168/180 | 2026-11-24T12:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |
| EUR/CAD | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.57063 | — | 168/180 | 2026-11-24T12:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| EUR/NZD | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 2.0035 | — | 168/180 | 2026-11-24T12:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |
| XAU/USD | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 3642.3085 | — | 168/180 | 2026-11-24T12:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |
| XAU/AUD | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 5480.731 | — | 168/180 | 2026-11-24T12:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |

## Saran analisa cadangan (BUKAN sinyal, tidak divalidasi backtest)
5 pair dengan level H1 terdekat. BUY dari support, SELL dari resistance. SL 0.5 ATR di seberang level, TP 1.5R. Tanpa cek spread, news, atau batas risiko §9. Tidak mengubah label.
| Pair | Arah | Level H1 (jarak, sentuhan) | Entry | SL | TP | Risiko SL |
|---|---|---|---|---|---|---|
| EUR/USD | **BUY** | 1.09599 support (0.02 ATR, 19 sentuh) | 1.09602 | 1.09536 | 1.09701 | 6.6 pip |
| EUR/GBP | **SELL** | 0.83698 resistance (0.18 ATR, 24 sentuh) | 0.83688 | 0.83724 | 0.83634 | 3.6 pip |
| GBP/USD | **BUY** | 1.3094 support (0.18 ATR, 20 sentuh) | 1.30966 | 1.30868 | 1.31112 | 9.8 pip |
| EUR/JPY | **SELL** | 174.5197 resistance (0.29 ATR, 22 sentuh) | 174.4455 | 174.64589 | 174.14491 | 20.0 pip |
| EUR/AUD | **BUY** | 1.64836 support (0.33 ATR, 25 sentuh) | 1.64925 | 1.647 | 1.65263 | 22.5 pip |

## Pemantauan 15 menit (entry dan analisa cadangan)
Nilai di kolom 15m-60m = pip dari entry pada close candle M15 ke-1 sampai ke-4. Jika SL dan TP kena di candle yang sama, dihitung SL. Analisa cadangan BUKAN sinyal.
| Sumber | Pair | Arah | Entry | SL | TP | 15m | 30m | 45m | 60m | Hasil | Pip sekarang | Umur |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ANALISA CADANGAN (bukan sinyal) | EUR/GBP | BUY | 0.83701 | 0.83672 | 0.83745 | +1.8 | +2.2 | +0.4 | -1.3 | Selesai 60 menit | LOSS 1.3 pip | 60 mnt |
| ANALISA CADANGAN (bukan sinyal) | EUR/AUD | SELL | 1.64983 | 1.65192 | 1.6467 | -1.2 | -5.8 | +6.2 | +5.8 | Selesai 60 menit | PROFIT 5.8 pip | 60 mnt |
| ANALISA CADANGAN (bukan sinyal) | EUR/USD | SELL | 1.09555 | 1.09662 | 1.09395 | +1.2 | -2.8 | -4.6 | -4.7 | Selesai 60 menit | LOSS 4.7 pip | 60 mnt |
| ANALISA CADANGAN (bukan sinyal) | GBP/USD | SELL | 1.30889 | 1.3101 | 1.30708 | +4.2 | +0.3 | -4.9 | -7.6 | Selesai 60 menit | LOSS 7.6 pip | 45 mnt |
| ANALISA CADANGAN (bukan sinyal) | EUR/JPY | SELL | 174.4245 | 174.6478 | 174.08956 | +8.6 | +7.2 | -1.9 | -2.1 | Selesai 60 menit | LOSS 2.1 pip | 45 mnt |
| ANALISA CADANGAN (bukan sinyal) | AUD/USD | BUY | 0.66406 | 0.66287 | 0.66584 | -1.5 | -0.7 | +5.2 | +5.0 | Selesai 60 menit | PROFIT 5.0 pip | 45 mnt |
| ANALISA CADANGAN (bukan sinyal) | XAU/AUD | BUY | 5474.69 | 5448.24953 | 5514.3507 | -179.6 | -129.6 | +81.2 | +60.4 | Selesai 60 menit | PROFIT 60.4 pip | 45 mnt |
| ANALISA CADANGAN (bukan sinyal) | EUR/CHF | SELL | 0.91904 | 0.91999 | 0.91761 | +7.7 | +12.6 | +6.1 | +1.1 | Selesai 60 menit | PROFIT 1.1 pip | 30 mnt |
| ANALISA CADANGAN (bukan sinyal) | NZD/USD | BUY | 0.54673 | 0.5459 | 0.54798 | -0.2 | -1.1 | +3.9 | +3.3 | Selesai 60 menit | PROFIT 3.3 pip | 30 mnt |
| ANALISA CADANGAN (bukan sinyal) | EUR/CAD | BUY | 1.56935 | 1.56855 | 1.57056 | +1.7 | +6.7 | - | - | TP kena | PROFIT 12.1 pip | 15 mnt |
| ANALISA CADANGAN (bukan sinyal) | USD/CAD | SELL | 1.4326 | 1.4333 | 1.43155 | - | - | - | - | SL kena | LOSS 7.0 pip | 15 mnt |

## Evaluasi 1 jam (entry dan analisa cadangan)
Dibuat setelah 60 menit atau saat SL/TP kena. MFE = gerak terbaik, MAE = gerak terburuk, dalam pip.
| Sumber | Pair | Arah | Hasil | Pip akhir | MFE (pip) | MAE (pip) | Ditutup (UTC) |
|---|---|---|---|---|---|---|---|
| ANALISA CADANGAN (bukan sinyal) | EUR/GBP | BUY | Selesai 60 menit | LOSS 1.3 pip | 3.3 | -1.7 | 2026-11-24T13:00:43Z |
| ANALISA CADANGAN (bukan sinyal) | EUR/AUD | SELL | Selesai 60 menit | PROFIT 5.8 pip | 9.4 | -6.8 | 2026-11-24T13:00:43Z |
| ANALISA CADANGAN (bukan sinyal) | EUR/USD | SELL | Selesai 60 menit | LOSS 4.7 pip | 5.2 | -8.5 | 2026-11-24T13:00:43Z |
| ANALISA CADANGAN (bukan sinyal) | GBP/USD | SELL | Selesai 60 menit | LOSS 7.6 pip | 7.5 | -10.3 | 2026-11-24T13:00:43Z |
| ANALISA CADANGAN (bukan sinyal) | EUR/JPY | SELL | Selesai 60 menit | LOSS 2.1 pip | 15.1 | -5.2 | 2026-11-24T13:00:43Z |
| ANALISA CADANGAN (bukan sinyal) | AUD/USD | BUY | Selesai 60 menit | PROFIT 5.0 pip | 7.0 | -3.3 | 2026-11-24T13:00:43Z |
| ANALISA CADANGAN (bukan sinyal) | XAU/AUD | BUY | Selesai 60 menit | PROFIT 60.4 pip | 126.7 | -192.5 | 2026-11-24T13:00:43Z |
| ANALISA CADANGAN (bukan sinyal) | EUR/CHF | SELL | Selesai 60 menit | PROFIT 1.1 pip | 13.3 | -0.9 | 2026-11-24T13:00:43Z |
| ANALISA CADANGAN (bukan sinyal) | NZD/USD | BUY | Selesai 60 menit | PROFIT 3.3 pip | 5.6 | -3.5 | 2026-11-24T13:00:43Z |
| ANALISA CADANGAN (bukan sinyal) | EUR/CAD | BUY | TP kena · menit 45 | PROFIT 12.1 pip | 12.2 | -2.2 | 2026-11-24T13:00:43Z |
| ANALISA CADANGAN (bukan sinyal) | USD/CAD | SELL | SL kena · menit 15 | LOSS 7.0 pip | 0.2 | -7.9 | 2026-11-24T13:00:43Z |

## Level analisa cadangan (BUKAN sinyal, tanpa statistik)
Level S/R terdekat untuk konteks scalping. Tidak mengubah label atau keputusan apa pun.
- **EUR/USD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 1.09599 (0.02 ATR, 19 bar sentuh)
  - M15: resistance 1.09642 (0.59 ATR, 16 bar sentuh) · support 1.09575 (0.4 ATR, 8 bar sentuh)
- **GBP/USD** (NO TRADE)
  - H1: resistance 1.31042 (0.53 ATR, 25 bar sentuh) · support 1.3094 (0.18 ATR, 20 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 1.30913 (0.67 ATR, 22 bar sentuh)
- **USD/JPY** (NO TRADE)
  - H1: resistance 159.41066 (1.33 ATR, 50 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance 159.24775 (0.93 ATR, 21 bar sentuh) · support tidak ada dalam jarak
- **USD/CHF** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support tidak ada dalam jarak
  - M15: resistance tidak ada dalam jarak · support 0.83808 (0.5 ATR, 15 bar sentuh)
- **AUD/USD** (NO TRADE)
  - H1: resistance 0.66551 (0.81 ATR, 18 bar sentuh) · support 0.66346 (0.94 ATR, 23 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 0.66444 (0.22 ATR, 30 bar sentuh)
- **USD/CAD** (NO TRADE)
  - H1: resistance 1.43386 (0.71 ATR, 27 bar sentuh) · support 1.43278 (0.35 ATR, 39 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 1.43269 (0.75 ATR, 26 bar sentuh)
- **NZD/USD** (NO TRADE)
  - H1: resistance 0.54756 (0.65 ATR, 14 bar sentuh) · support 0.54628 (1.01 ATR, 6 bar sentuh)
  - M15: resistance 0.54717 (0.27 ATR, 25 bar sentuh) · support tidak ada dalam jarak
- **EUR/GBP** (NO TRADE)
  - H1: resistance 0.83698 (0.18 ATR, 24 bar sentuh) · support 0.83661 (0.52 ATR, 30 bar sentuh)
  - M15: resistance 0.83713 (0.82 ATR, 22 bar sentuh) · support tidak ada dalam jarak
- **EUR/JPY** (NO TRADE)
  - H1: resistance 174.5197 (0.29 ATR, 22 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance tidak ada dalam jarak · support 174.43794 (0.06 ATR, 33 bar sentuh)
- **EUR/CHF** (NO TRADE)
  - H1: resistance 0.91953 (0.62 ATR, 11 bar sentuh) · support 0.91819 (0.78 ATR, 18 bar sentuh)
  - M15: resistance 0.91944 (0.86 ATR, 24 bar sentuh) · support tidak ada dalam jarak
- **EUR/AUD** (NO TRADE)
  - H1: resistance 1.65051 (0.46 ATR, 13 bar sentuh) · support 1.64836 (0.33 ATR, 25 bar sentuh)
  - M15: resistance 1.65036 (0.8 ATR, 16 bar sentuh) · support 1.6485 (0.55 ATR, 14 bar sentuh)
- **EUR/CAD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 1.56922 (1.03 ATR, 12 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support tidak ada dalam jarak
- **EUR/NZD** (NO TRADE)
  - H1: resistance 2.00637 (1.25 ATR, 15 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance 2.00387 (0.32 ATR, 40 bar sentuh) · support tidak ada dalam jarak
- **XAU/USD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support tidak ada dalam jarak
  - M15: resistance tidak ada dalam jarak · support 3641.84133 (0.05 ATR, 15 bar sentuh)
- **XAU/AUD** (NO TRADE)
  - H1: resistance 5495.14 (0.56 ATR, 14 bar sentuh) · support 5460.94038 (0.77 ATR, 18 bar sentuh)
  - M15: resistance 5492.08425 (0.92 ATR, 18 bar sentuh) · support tidak ada dalam jarak

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

