# Laporan Scanner Adaptive Forex

- Waktu eksekusi: 2026-11-24T14:45:26Z
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
| EUR/JPY | **SELL** | 174.5197 resistance (0.26 ATR, 23 sentuh) | 174.4555 | 174.64549 | 174.17052 | 19.0 pip |
| AUD/USD | **BUY** | 0.66346 support (0.34 ATR, 24 sentuh) | 0.66386 | 0.66287 | 0.66535 | 9.9 pip |
| NZD/USD | **SELL** | 0.54756 resistance (0.65 ATR, 15 sentuh) | 0.54706 | 0.54795 | 0.54573 | 8.9 pip |

## Pemantauan 15 menit (entry dan analisa cadangan)
Nilai di kolom 15m-60m = pip dari entry pada close candle M15 ke-1 sampai ke-4. Jika SL dan TP kena di candle yang sama, dihitung SL. Analisa cadangan BUKAN sinyal.
| Sumber | Pair | Arah | Entry | SL | TP | 15m | 30m | 45m | 60m | Hasil | Pip sekarang | Umur |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ANALISA CADANGAN (bukan sinyal) | XAU/USD | BUY | 3614.9115 | 3602.90189 | 3632.92591 | +19.3 | +40.8 | +129.9 | - | BERJALAN | PROFIT 129.9 pip | 45 mnt |
| ANALISA CADANGAN (bukan sinyal) | GBP/USD | BUY | 1.30984 | 1.30868 | 1.31158 | -4.5 | +2.2 | +14.7 | - | BERJALAN | PROFIT 14.7 pip | 45 mnt |
| ANALISA CADANGAN (bukan sinyal) | EUR/GBP | BUY | 0.83715 | 0.83672 | 0.8378 | +4.3 | +2.1 | -0.6 | - | BERJALAN | LOSS 0.6 pip | 30 mnt |
| ANALISA CADANGAN (bukan sinyal) | AUD/USD | BUY | 0.66386 | 0.66287 | 0.66535 | +3.4 | +5.5 | - | - | TP kena | PROFIT 14.9 pip | 30 mnt |
| ANALISA CADANGAN (bukan sinyal) | EUR/AUD | SELL | 1.65169 | 1.65405 | 1.64815 | +4.4 | +6.4 | +17.3 | - | BERJALAN | PROFIT 17.3 pip | 30 mnt |
| ANALISA CADANGAN (bukan sinyal) | EUR/CHF | BUY | 0.91826 | 0.91769 | 0.91911 | - | - | - | - | SL kena | LOSS 5.7 pip | 15 mnt |
| ANALISA CADANGAN (bukan sinyal) | USD/CAD | SELL | 1.4327 | 1.43329 | 1.43182 | - | - | - | - | TP kena | PROFIT 8.8 pip | 15 mnt |
| ANALISA CADANGAN (bukan sinyal) | EUR/JPY | SELL | 174.4555 | 174.64549 | 174.17052 | -11.7 | - | - | - | SL kena | LOSS 19.0 pip | 15 mnt |
| ANALISA CADANGAN (bukan sinyal) | EUR/USD | BUY | 1.09649 | 1.09535 | 1.0982 | +2.1 | +4.8 | +12.3 | - | BERJALAN | PROFIT 12.3 pip | 15 mnt |
| ANALISA CADANGAN (bukan sinyal) | XAU/AUD | SELL | 5445.427 | 5474.25727 | 5402.18159 | -2.5 | -14.9 | -77.8 | - | BERJALAN | LOSS 77.8 pip | 15 mnt |

## Evaluasi 1 jam (entry dan analisa cadangan)
Dibuat setelah 60 menit atau saat SL/TP kena. MFE = gerak terbaik, MAE = gerak terburuk, dalam pip.
| Sumber | Pair | Arah | Hasil | Pip akhir | MFE (pip) | MAE (pip) | Ditutup (UTC) |
|---|---|---|---|---|---|---|---|
| ANALISA CADANGAN (bukan sinyal) | AUD/USD | BUY | TP kena · menit 45 | PROFIT 14.9 pip | 17.0 | -0.6 | 2026-11-24T14:45:26Z |
| ANALISA CADANGAN (bukan sinyal) | EUR/CHF | BUY | SL kena · menit 15 | LOSS 5.7 pip | 1.5 | -6.1 | 2026-11-24T14:45:26Z |
| ANALISA CADANGAN (bukan sinyal) | USD/CAD | SELL | TP kena · menit 15 | PROFIT 8.8 pip | 11.8 | -2.1 | 2026-11-24T14:45:26Z |
| ANALISA CADANGAN (bukan sinyal) | EUR/JPY | SELL | SL kena · menit 30 | LOSS 19.0 pip | 1.9 | -24.9 | 2026-11-24T14:45:26Z |

## Level analisa cadangan (BUKAN sinyal, tanpa statistik)
Level S/R terdekat untuk konteks scalping. Tidak mengubah label atau keputusan apa pun.
- **EUR/USD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 1.09599 (0.39 ATR, 20 bar sentuh)
  - M15: resistance 1.09788 (0.21 ATR, 24 bar sentuh) · support tidak ada dalam jarak
- **GBP/USD** (NO TRADE)
  - H1: resistance 1.31042 (0.4 ATR, 26 bar sentuh) · support 1.3094 (0.3 ATR, 21 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 1.31089 (0.45 ATR, 29 bar sentuh)
- **USD/JPY** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 158.84939 (1.34 ATR, 18 bar sentuh)
  - M15: resistance 159.24239 (0.35 ATR, 25 bar sentuh) · support tidak ada dalam jarak
- **USD/CHF** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 0.83669 (0.65 ATR, 3 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support tidak ada dalam jarak
- **AUD/USD** (NO TRADE)
  - H1: resistance 0.66551 (1.39 ATR, 19 bar sentuh) · support 0.66346 (0.34 ATR, 24 bar sentuh)
  - M15: resistance 0.66586 (0.87 ATR, 6 bar sentuh) · support 0.66466 (1.0 ATR, 33 bar sentuh)
- **USD/CAD** (NO TRADE)
  - H1: resistance 1.43278 (0.08 ATR, 40 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance tidak ada dalam jarak · support tidak ada dalam jarak
- **NZD/USD** (NO TRADE)
  - H1: resistance 0.54756 (0.65 ATR, 15 bar sentuh) · support 0.54628 (1.02 ATR, 6 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support tidak ada dalam jarak
- **EUR/GBP** (NO TRADE)
  - H1: resistance 0.83763 (0.93 ATR, 28 bar sentuh) · support 0.83698 (0.32 ATR, 25 bar sentuh)
  - M15: resistance 0.83711 (0.08 ATR, 29 bar sentuh) · support tidak ada dalam jarak
- **EUR/JPY** (NO TRADE)
  - H1: resistance 174.5197 (0.26 ATR, 23 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance 174.7755 (0.1 ATR, 10 bar sentuh) · support tidak ada dalam jarak
- **EUR/CHF** (NO TRADE)
  - H1: resistance 0.91953 (1.27 ATR, 11 bar sentuh) · support 0.91819 (0.06 ATR, 19 bar sentuh)
  - M15: resistance 0.91784 (0.21 ATR, 53 bar sentuh) · support tidak ada dalam jarak
- **EUR/AUD** (NO TRADE)
  - H1: resistance 1.65267 (0.35 ATR, 14 bar sentuh) · support 1.65051 (0.43 ATR, 14 bar sentuh)
  - M15: resistance 1.65031 (0.22 ATR, 20 bar sentuh) · support 1.64858 (0.88 ATR, 15 bar sentuh)
- **EUR/CAD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 1.56922 (1.16 ATR, 12 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 1.56952 (0.27 ATR, 14 bar sentuh)
- **EUR/NZD** (NO TRADE)
  - H1: resistance 2.00637 (0.88 ATR, 15 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance tidak ada dalam jarak · support 1.99968 (0.79 ATR, 11 bar sentuh)
- **XAU/USD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 3612.84694 (0.1 ATR, 17 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 3619.79746 (0.8 ATR, 56 bar sentuh)
- **XAU/AUD** (NO TRADE)
  - H1: resistance 5460.94038 (0.58 ATR, 19 bar sentuh) · support 5416.917 (1.07 ATR, 7 bar sentuh)
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

