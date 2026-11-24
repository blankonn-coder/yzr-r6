# Laporan Scanner Adaptive Forex

- Waktu eksekusi: 2026-11-24T15:15:25Z
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
| EUR/USD | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.09742 | — | 168/180 | 2026-11-24T14:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| GBP/USD | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.3114 | — | 168/180 | 2026-11-24T14:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| USD/JPY | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 159.2295 | — | 168/180 | 2026-11-24T14:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |
| USD/CHF | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.83586 | — | 168/180 | 2026-11-24T14:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| AUD/USD | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.66557 | — | 168/180 | 2026-11-24T14:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |
| USD/CAD | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.42912 | — | 168/180 | 2026-11-24T14:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| NZD/USD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.54889 | — | 168/180 | 2026-11-24T14:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| EUR/GBP | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.83683 | — | 168/180 | 2026-11-24T14:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |
| EUR/JPY | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 174.7435 | — | 168/180 | 2026-11-24T14:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| EUR/CHF | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.91729 | — | 168/180 | 2026-11-24T14:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| EUR/AUD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.6489 | — | 168/180 | 2026-11-24T14:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| EUR/CAD | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.56824 | — | 168/180 | 2026-11-24T14:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| EUR/NZD | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.99934 | — | 168/180 | 2026-11-24T14:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |
| XAU/USD | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 3622.0475 | — | 168/180 | 2026-11-24T14:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |
| XAU/AUD | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 5442.1425 | — | 168/180 | 2026-11-24T14:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |

## Saran analisa cadangan (BUKAN sinyal, tidak divalidasi backtest)
5 pair dengan level H1 terdekat. BUY dari support, SELL dari resistance. SL 0.5 ATR di seberang level, TP 1.5R. Tanpa cek spread, news, atau batas risiko §9. Tidak mengubah label.
| Pair | Arah | Level H1 (jarak, sentuhan) | Entry | SL | TP | Risiko SL |
|---|---|---|---|---|---|---|
| AUD/USD | **BUY** | 0.66551 support (0.05 ATR, 20 sentuh) | 0.66557 | 0.6649 | 0.66658 | 6.7 pip |
| EUR/CHF | **SELL** | 0.91743 resistance (0.13 ATR, 10 sentuh) | 0.91729 | 0.91794 | 0.91632 | 6.5 pip |
| EUR/GBP | **SELL** | 0.83698 resistance (0.28 ATR, 26 sentuh) | 0.83683 | 0.83725 | 0.83619 | 4.3 pip |
| XAU/USD | **BUY** | 3616.2534 support (0.29 ATR, 21 sentuh) | 3622.0475 | 3606.34418 | 3645.60248 | 157.0 pip |
| NZD/USD | **SELL** | 0.54935 resistance (0.54 ATR, 57 sentuh) | 0.54889 | 0.54978 | 0.54756 | 8.9 pip |

## Pemantauan 15 menit (entry dan analisa cadangan)
Nilai di kolom 15m-60m = pip dari entry pada close candle M15 ke-1 sampai ke-4. Jika SL dan TP kena di candle yang sama, dihitung SL. Analisa cadangan BUKAN sinyal.
| Sumber | Pair | Arah | Entry | SL | TP | 15m | 30m | 45m | 60m | Hasil | Pip sekarang | Umur |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ANALISA CADANGAN (bukan sinyal) | EUR/JPY | BUY | 174.7435 | 174.61248 | 174.94003 | -9.0 | - | - | - | BERJALAN | LOSS 9.0 pip | 15 mnt |
| ANALISA CADANGAN (bukan sinyal) | AUD/USD | BUY | 0.66557 | 0.6649 | 0.66658 | - | - | - | - | SL kena | LOSS 6.7 pip | 15 mnt |
| ANALISA CADANGAN (bukan sinyal) | EUR/CHF | SELL | 0.91729 | 0.91794 | 0.91632 | - | - | - | - | SL kena | LOSS 6.5 pip | 15 mnt |
| ANALISA CADANGAN (bukan sinyal) | EUR/NZD | BUY | 1.99934 | 1.99769 | 2.00182 | -3.2 | - | - | - | BERJALAN | LOSS 3.2 pip | 15 mnt |
| ANALISA CADANGAN (bukan sinyal) | EUR/AUD | BUY | 1.6489 | 1.64695 | 1.65182 | -0.1 | - | - | - | BERJALAN | LOSS 0.1 pip | 15 mnt |

## Evaluasi 1 jam (entry dan analisa cadangan)
Dibuat setelah 60 menit atau saat SL/TP kena. MFE = gerak terbaik, MAE = gerak terburuk, dalam pip.
| Sumber | Pair | Arah | Hasil | Pip akhir | MFE (pip) | MAE (pip) | Ditutup (UTC) |
|---|---|---|---|---|---|---|---|
| ANALISA CADANGAN (bukan sinyal) | AUD/USD | BUY | SL kena · menit 15 | LOSS 6.7 pip | 0.5 | -9.8 | 2026-11-24T15:15:25Z |
| ANALISA CADANGAN (bukan sinyal) | EUR/CHF | SELL | SL kena · menit 15 | LOSS 6.5 pip | 1.3 | -7.0 | 2026-11-24T15:15:25Z |

## Level analisa cadangan (BUKAN sinyal, tanpa statistik)
Level S/R terdekat untuk konteks scalping. Tidak mengubah label atau keputusan apa pun.
- **EUR/USD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 1.09599 (1.1 ATR, 21 bar sentuh)
  - M15: resistance 1.09673 (0.71 ATR, 25 bar sentuh) · support 1.09558 (0.74 ATR, 7 bar sentuh)
- **GBP/USD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 1.31042 (0.66 ATR, 28 bar sentuh)
  - M15: resistance 1.31082 (0.4 ATR, 29 bar sentuh) · support tidak ada dalam jarak
- **USD/JPY** (NO TRADE)
  - H1: resistance 159.40047 (0.9 ATR, 53 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance 159.4145 (0.74 ATR, 9 bar sentuh) · support 159.24239 (0.88 ATR, 27 bar sentuh)
- **USD/CHF** (NO TRADE)
  - H1: resistance 0.83669 (0.67 ATR, 3 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance tidak ada dalam jarak · support tidak ada dalam jarak
- **AUD/USD** (NO TRADE)
  - H1: resistance 0.66726 (1.37 ATR, 14 bar sentuh) · support 0.66551 (0.05 ATR, 20 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 0.66466 (0.17 ATR, 34 bar sentuh)
- **USD/CAD** (NO TRADE)
  - H1: resistance 1.43026 (0.93 ATR, 39 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance tidak ada dalam jarak · support tidak ada dalam jarak
- **NZD/USD** (NO TRADE)
  - H1: resistance 0.54935 (0.54 ATR, 57 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance tidak ada dalam jarak · support tidak ada dalam jarak
- **EUR/GBP** (NO TRADE)
  - H1: resistance 0.83698 (0.28 ATR, 26 bar sentuh) · support 0.83661 (0.38 ATR, 30 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support tidak ada dalam jarak
- **EUR/JPY** (NO TRADE)
  - H1: resistance 174.9835 (0.92 ATR, 25 bar sentuh) · support 174.743 (0.0 ATR, 30 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support tidak ada dalam jarak
- **EUR/CHF** (NO TRADE)
  - H1: resistance 0.91743 (0.13 ATR, 10 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance 0.91786 (0.66 ATR, 55 bar sentuh) · support tidak ada dalam jarak
- **EUR/AUD** (NO TRADE)
  - H1: resistance 1.65051 (0.57 ATR, 15 bar sentuh) · support 1.64836 (0.19 ATR, 26 bar sentuh)
  - M15: resistance 1.65031 (0.92 ATR, 20 bar sentuh) · support 1.64858 (0.2 ATR, 13 bar sentuh)
- **EUR/CAD** (NO TRADE)
  - H1: resistance 1.56922 (0.65 ATR, 13 bar sentuh) · support 1.56742 (0.54 ATR, 9 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 1.56669 (0.52 ATR, 43 bar sentuh)
- **EUR/NZD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 1.99896 (0.15 ATR, 47 bar sentuh)
  - M15: resistance 1.99968 (0.49 ATR, 12 bar sentuh) · support tidak ada dalam jarak
- **XAU/USD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 3616.2534 (0.29 ATR, 21 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support tidak ada dalam jarak
- **XAU/AUD** (NO TRADE)
  - H1: resistance 5460.94038 (0.72 ATR, 20 bar sentuh) · support 5416.917 (0.97 ATR, 7 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 5416.917 (0.2 ATR, 8 bar sentuh)

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

