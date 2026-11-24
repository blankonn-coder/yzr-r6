# Laporan Scanner Adaptive Forex

- Waktu eksekusi: 2026-11-24T14:00:42Z
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
| EUR/USD | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.09649 | — | 168/180 | 2026-11-24T13:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| GBP/USD | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.30984 | — | 168/180 | 2026-11-24T13:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| USD/JPY | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 159.1015 | — | 168/180 | 2026-11-24T13:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |
| USD/CHF | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.83745 | — | 168/180 | 2026-11-24T13:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| AUD/USD | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.66386 | — | 168/180 | 2026-11-24T13:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |
| USD/CAD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.4327 | — | 168/180 | 2026-11-24T13:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| NZD/USD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.54706 | — | 168/180 | 2026-11-24T13:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| EUR/GBP | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.83715 | — | 168/180 | 2026-11-24T13:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |
| EUR/JPY | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 174.4555 | — | 168/180 | 2026-11-24T13:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| EUR/CHF | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.91826 | — | 168/180 | 2026-11-24T13:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| EUR/AUD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.65169 | — | 168/180 | 2026-11-24T13:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| EUR/CAD | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.57083 | — | 168/180 | 2026-11-24T13:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| EUR/NZD | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 2.00435 | — | 168/180 | 2026-11-24T13:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |
| XAU/USD | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 3614.9115 | — | 168/180 | 2026-11-24T13:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |
| XAU/AUD | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 5445.427 | — | 168/180 | 2026-11-24T13:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |

## Saran analisa cadangan (BUKAN sinyal, tidak divalidasi backtest)
5 pair dengan level H1 terdekat. BUY dari support, SELL dari resistance. SL 0.5 ATR di seberang level, TP 1.5R. Tanpa cek spread, news, atau batas risiko §9. Tidak mengubah label.
| Pair | Arah | Level H1 (jarak, sentuhan) | Entry | SL | TP | Risiko SL |
|---|---|---|---|---|---|---|
| EUR/CHF | **BUY** | 0.91819 support (0.06 ATR, 19 sentuh) | 0.91826 | 0.91769 | 0.91911 | 5.7 pip |
| USD/CAD | **SELL** | 1.43278 resistance (0.08 ATR, 40 sentuh) | 1.4327 | 1.43329 | 1.43182 | 5.9 pip |
| XAU/USD | **BUY** | 3612.84694 support (0.1 ATR, 17 sentuh) | 3614.9115 | 3602.90189 | 3632.92591 | 120.1 pip |
| EUR/JPY | **SELL** | 174.5197 resistance (0.26 ATR, 23 sentuh) | 174.4555 | 174.64549 | 174.17052 | 19.0 pip |
| GBP/USD | **BUY** | 1.3094 support (0.3 ATR, 21 sentuh) | 1.30984 | 1.30868 | 1.31158 | 11.6 pip |

## Pemantauan 15 menit (entry dan analisa cadangan)
Nilai di kolom 15m-60m = pip dari entry pada close candle M15 ke-1 sampai ke-4. Jika SL dan TP kena di candle yang sama, dihitung SL. Analisa cadangan BUKAN sinyal.
| Sumber | Pair | Arah | Entry | SL | TP | 15m | 30m | 45m | 60m | Hasil | Pip sekarang | Umur |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ANALISA CADANGAN (bukan sinyal) | EUR/USD | BUY | 1.09602 | 1.09536 | 1.09701 | +5.1 | +1.4 | -1.2 | +4.7 | Selesai 60 menit | PROFIT 4.7 pip | 60 mnt |
| ANALISA CADANGAN (bukan sinyal) | EUR/GBP | SELL | 0.83688 | 0.83724 | 0.83634 | -2.5 | +0.2 | -0.4 | -2.7 | Selesai 60 menit | LOSS 2.7 pip | 60 mnt |
| ANALISA CADANGAN (bukan sinyal) | GBP/USD | BUY | 1.30966 | 1.30868 | 1.31112 | +2.2 | +1.9 | -2.1 | +1.8 | Selesai 60 menit | PROFIT 1.8 pip | 60 mnt |
| ANALISA CADANGAN (bukan sinyal) | EUR/JPY | SELL | 174.4455 | 174.64589 | 174.14491 | +5.1 | +0.9 | +0.7 | -1.0 | Selesai 60 menit | LOSS 1.0 pip | 60 mnt |
| ANALISA CADANGAN (bukan sinyal) | EUR/AUD | BUY | 1.64925 | 1.647 | 1.65263 | +21.8 | +8.4 | +8.2 | +24.4 | Selesai 60 menit | PROFIT 24.4 pip | 60 mnt |
| ANALISA CADANGAN (bukan sinyal) | USD/CAD | BUY | 1.43314 | 1.43226 | 1.43445 | -2.3 | -7.2 | -5.5 | - | SL kena | LOSS 8.8 pip | 45 mnt |
| ANALISA CADANGAN (bukan sinyal) | XAU/AUD | SELL | 5480.731 | 5508.06444 | 5439.73083 | +113.8 | +209.0 | +342.7 | +353.0 | Selesai 60 menit | PROFIT 353.0 pip | 45 mnt |
| ANALISA CADANGAN (bukan sinyal) | EUR/CHF | SELL | 0.91893 | 0.92 | 0.91732 | +9.1 | +9.9 | +8.4 | +6.7 | Selesai 60 menit | PROFIT 6.7 pip | 45 mnt |
| ANALISA CADANGAN (bukan sinyal) | NZD/USD | SELL | 0.54706 | 0.54795 | 0.54573 | -0.4 | +0.6 | +0.8 | +0.0 | Selesai 60 menit | PROFIT 0.0 pip | 45 mnt |
| ANALISA CADANGAN (bukan sinyal) | AUD/USD | SELL | 0.66456 | 0.66609 | 0.66226 | +5.5 | +2.7 | +4.2 | +7.0 | Selesai 60 menit | PROFIT 7.0 pip | 45 mnt |

## Evaluasi 1 jam (entry dan analisa cadangan)
Dibuat setelah 60 menit atau saat SL/TP kena. MFE = gerak terbaik, MAE = gerak terburuk, dalam pip.
| Sumber | Pair | Arah | Hasil | Pip akhir | MFE (pip) | MAE (pip) | Ditutup (UTC) |
|---|---|---|---|---|---|---|---|
| ANALISA CADANGAN (bukan sinyal) | EUR/USD | BUY | Selesai 60 menit | PROFIT 4.7 pip | 8.7 | -6.1 | 2026-11-24T14:00:42Z |
| ANALISA CADANGAN (bukan sinyal) | EUR/GBP | SELL | Selesai 60 menit | LOSS 2.7 pip | 0.9 | -3.4 | 2026-11-24T14:00:42Z |
| ANALISA CADANGAN (bukan sinyal) | GBP/USD | BUY | Selesai 60 menit | PROFIT 1.8 pip | 9.0 | -7.7 | 2026-11-24T14:00:42Z |
| ANALISA CADANGAN (bukan sinyal) | EUR/JPY | SELL | Selesai 60 menit | LOSS 1.0 pip | 14.6 | -9.5 | 2026-11-24T14:00:42Z |
| ANALISA CADANGAN (bukan sinyal) | EUR/AUD | BUY | Selesai 60 menit | PROFIT 24.4 pip | 32.6 | 0.1 | 2026-11-24T14:00:42Z |
| ANALISA CADANGAN (bukan sinyal) | USD/CAD | BUY | SL kena · menit 60 | LOSS 8.8 pip | -0.1 | -8.9 | 2026-11-24T14:00:42Z |
| ANALISA CADANGAN (bukan sinyal) | XAU/AUD | SELL | Selesai 60 menit | PROFIT 353.0 pip | 368.4 | 3.8 | 2026-11-24T14:00:42Z |
| ANALISA CADANGAN (bukan sinyal) | EUR/CHF | SELL | Selesai 60 menit | PROFIT 6.7 pip | 14.8 | -1.7 | 2026-11-24T14:00:42Z |
| ANALISA CADANGAN (bukan sinyal) | NZD/USD | SELL | Selesai 60 menit | PROFIT 0.0 pip | 3.4 | -4.0 | 2026-11-24T14:00:42Z |
| ANALISA CADANGAN (bukan sinyal) | AUD/USD | SELL | Selesai 60 menit | PROFIT 7.0 pip | 9.7 | -3.9 | 2026-11-24T14:00:42Z |

## Level analisa cadangan (BUKAN sinyal, tanpa statistik)
Level S/R terdekat untuk konteks scalping. Tidak mengubah label atau keputusan apa pun.
- **EUR/USD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 1.09599 (0.39 ATR, 20 bar sentuh)
  - M15: resistance 1.09673 (0.34 ATR, 19 bar sentuh) · support tidak ada dalam jarak
- **GBP/USD** (NO TRADE)
  - H1: resistance 1.31042 (0.4 ATR, 26 bar sentuh) · support 1.3094 (0.3 ATR, 21 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 1.30913 (0.87 ATR, 23 bar sentuh)
- **USD/JPY** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 158.84939 (1.34 ATR, 18 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support tidak ada dalam jarak
- **USD/CHF** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 0.83669 (0.65 ATR, 3 bar sentuh)
  - M15: resistance 0.8379 (0.61 ATR, 14 bar sentuh) · support tidak ada dalam jarak
- **AUD/USD** (NO TRADE)
  - H1: resistance 0.66551 (1.39 ATR, 19 bar sentuh) · support 0.66346 (0.34 ATR, 24 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 0.66333 (0.89 ATR, 45 bar sentuh)
- **USD/CAD** (NO TRADE)
  - H1: resistance 1.43278 (0.08 ATR, 40 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance tidak ada dalam jarak · support 1.43269 (0.01 ATR, 31 bar sentuh)
- **NZD/USD** (NO TRADE)
  - H1: resistance 0.54756 (0.65 ATR, 15 bar sentuh) · support 0.54628 (1.02 ATR, 6 bar sentuh)
  - M15: resistance 0.54722 (0.39 ATR, 29 bar sentuh) · support tidak ada dalam jarak
- **EUR/GBP** (NO TRADE)
  - H1: resistance 0.83763 (0.93 ATR, 28 bar sentuh) · support 0.83698 (0.32 ATR, 25 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 0.83712 (0.08 ATR, 25 bar sentuh)
- **EUR/JPY** (NO TRADE)
  - H1: resistance 174.5197 (0.26 ATR, 23 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance tidak ada dalam jarak · support 174.44444 (0.08 ATR, 33 bar sentuh)
- **EUR/CHF** (NO TRADE)
  - H1: resistance 0.91953 (1.27 ATR, 11 bar sentuh) · support 0.91819 (0.06 ATR, 19 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 0.91783 (0.66 ATR, 48 bar sentuh)
- **EUR/AUD** (NO TRADE)
  - H1: resistance 1.65267 (0.35 ATR, 14 bar sentuh) · support 1.65051 (0.43 ATR, 14 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 1.65031 (0.9 ATR, 18 bar sentuh)
- **EUR/CAD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 1.56922 (1.16 ATR, 12 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support tidak ada dalam jarak
- **EUR/NZD** (NO TRADE)
  - H1: resistance 2.00637 (0.88 ATR, 15 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance tidak ada dalam jarak · support 2.00388 (0.39 ATR, 46 bar sentuh)
- **XAU/USD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 3612.84694 (0.1 ATR, 17 bar sentuh)
  - M15: resistance 3620.05122 (0.52 ATR, 53 bar sentuh) · support tidak ada dalam jarak
- **XAU/AUD** (NO TRADE)
  - H1: resistance 5460.94038 (0.58 ATR, 19 bar sentuh) · support 5416.917 (1.07 ATR, 7 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 5435.56775 (0.74 ATR, 19 bar sentuh)

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

