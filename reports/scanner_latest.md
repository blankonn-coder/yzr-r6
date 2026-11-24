# Laporan Scanner Adaptive Forex

- Waktu eksekusi: 2026-11-24T12:15:25Z
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
| EUR/USD | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.09555 | — | 168/180 | 2026-11-24T11:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| GBP/USD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.30889 | — | 168/180 | 2026-11-24T11:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| USD/JPY | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 159.2105 | — | 168/180 | 2026-11-24T11:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |
| USD/CHF | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.83886 | — | 168/180 | 2026-11-24T11:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| AUD/USD | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.66406 | — | 168/180 | 2026-11-24T11:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |
| USD/CAD | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.4326 | — | 168/180 | 2026-11-24T11:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |
| NZD/USD | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.54673 | — | 168/180 | 2026-11-24T11:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| EUR/GBP | TRENDING LEMAH | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.83701 | — | 168/180 | 2026-11-24T11:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING LEMAH belum punya metode prioritas di ranking |
| EUR/JPY | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 174.4245 | — | 168/180 | 2026-11-24T11:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| EUR/CHF | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 0.91904 | — | 168/180 | 2026-11-24T11:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| EUR/AUD | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.64983 | — | 168/180 | 2026-11-24T11:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |
| EUR/CAD | TRENDING KUAT | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 1.56935 | — | 168/180 | 2026-11-24T11:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime TRENDING KUAT belum punya metode prioritas di ranking |
| EUR/NZD | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 2.00386 | — | 168/180 | 2026-11-24T11:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |
| XAU/USD | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 3635.4365 | — | 168/180 | 2026-11-24T11:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |
| XAU/AUD | RANGING | BELUM SIAP | NO TRADE | Tidak ada metode prioritas | - | - | — | 5474.69 | — | 168/180 | 2026-11-24T11:00:00Z | bias H4 belum bisa dihitung (bar H4: 180, butuh 200); regime RANGING belum punya metode prioritas di ranking |

## Saran analisa cadangan (BUKAN sinyal, tidak divalidasi backtest)
5 pair dengan level H1 terdekat. BUY dari support, SELL dari resistance. SL 0.5 ATR di seberang level, TP 1.5R. Tanpa cek spread, news, atau batas risiko §9. Tidak mengubah label.
| Pair | Arah | Level H1 (jarak, sentuhan) | Entry | SL | TP | Risiko SL |
|---|---|---|---|---|---|---|
| USD/CAD | **SELL** | 1.43278 resistance (0.18 ATR, 38 sentuh) | 1.4326 | 1.4333 | 1.43155 | 7.0 pip |
| GBP/USD | **SELL** | 1.3094 resistance (0.36 ATR, 19 sentuh) | 1.30889 | 1.3101 | 1.30708 | 12.1 pip |
| EUR/JPY | **SELL** | 174.5197 resistance (0.37 ATR, 21 sentuh) | 174.4245 | 174.6478 | 174.08956 | 22.3 pip |
| AUD/USD | **BUY** | 0.66346 support (0.51 ATR, 23 sentuh) | 0.66406 | 0.66287 | 0.66584 | 11.9 pip |
| XAU/AUD | **BUY** | 5460.94038 support (0.54 ATR, 17 sentuh) | 5474.69 | 5448.24953 | 5514.3507 | 264.4 pip |

## Pemantauan 15 menit (entry dan analisa cadangan)
Nilai di kolom 15m-60m = pip dari entry pada close candle M15 ke-1 sampai ke-4. Jika SL dan TP kena di candle yang sama, dihitung SL. Analisa cadangan BUKAN sinyal.
| Sumber | Pair | Arah | Entry | SL | TP | 15m | 30m | 45m | 60m | Hasil | Pip sekarang | Umur |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ANALISA CADANGAN (bukan sinyal) | EUR/GBP | BUY | 0.83701 | 0.83672 | 0.83745 | +1.8 | - | - | - | BERJALAN | PROFIT 1.8 pip | 15 mnt |
| ANALISA CADANGAN (bukan sinyal) | EUR/CAD | BUY | 1.56935 | 1.56855 | 1.57056 | +1.7 | - | - | - | BERJALAN | PROFIT 1.7 pip | 15 mnt |
| ANALISA CADANGAN (bukan sinyal) | USD/CAD | SELL | 1.4326 | 1.4333 | 1.43155 | - | - | - | - | SL kena | LOSS 7.0 pip | 15 mnt |
| ANALISA CADANGAN (bukan sinyal) | EUR/AUD | SELL | 1.64983 | 1.65192 | 1.6467 | -1.2 | - | - | - | BERJALAN | LOSS 1.2 pip | 15 mnt |
| ANALISA CADANGAN (bukan sinyal) | EUR/USD | SELL | 1.09555 | 1.09662 | 1.09395 | +1.2 | - | - | - | BERJALAN | PROFIT 1.2 pip | 15 mnt |

## Evaluasi 1 jam (entry dan analisa cadangan)
Dibuat setelah 60 menit atau saat SL/TP kena. MFE = gerak terbaik, MAE = gerak terburuk, dalam pip.
| Sumber | Pair | Arah | Hasil | Pip akhir | MFE (pip) | MAE (pip) | Ditutup (UTC) |
|---|---|---|---|---|---|---|---|
| ANALISA CADANGAN (bukan sinyal) | USD/CAD | SELL | SL kena · menit 15 | LOSS 7.0 pip | 0.2 | -7.9 | 2026-11-24T12:15:25Z |

## Level analisa cadangan (BUKAN sinyal, tanpa statistik)
Level S/R terdekat untuk konteks scalping. Tidak mengubah label atau keputusan apa pun.
- **EUR/USD** (NO TRADE)
  - H1: resistance 1.09599 (0.35 ATR, 18 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance 1.09575 (0.47 ATR, 5 bar sentuh) · support tidak ada dalam jarak
- **GBP/USD** (NO TRADE)
  - H1: resistance 1.3094 (0.36 ATR, 19 bar sentuh) · support 1.30783 (0.76 ATR, 8 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 1.308 (0.61 ATR, 14 bar sentuh)
- **USD/JPY** (NO TRADE)
  - H1: resistance 159.40508 (1.03 ATR, 49 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance 159.23 (0.81 ATR, 22 bar sentuh) · support tidak ada dalam jarak
- **USD/CHF** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support tidak ada dalam jarak
  - M15: resistance tidak ada dalam jarak · support 0.83819 (0.14 ATR, 15 bar sentuh)
- **AUD/USD** (NO TRADE)
  - H1: resistance 0.66551 (1.23 ATR, 19 bar sentuh) · support 0.66346 (0.51 ATR, 23 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support tidak ada dalam jarak
- **USD/CAD** (NO TRADE)
  - H1: resistance 1.43278 (0.18 ATR, 38 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance tidak ada dalam jarak · support 1.43271 (0.37 ATR, 24 bar sentuh)
- **NZD/USD** (NO TRADE)
  - H1: resistance 0.54756 (1.09 ATR, 14 bar sentuh) · support 0.54628 (0.59 ATR, 5 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 0.54649 (0.57 ATR, 13 bar sentuh)
- **EUR/GBP** (NO TRADE)
  - H1: resistance 0.83765 (1.22 ATR, 29 bar sentuh) · support 0.83698 (0.07 ATR, 23 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 0.83713 (0.21 ATR, 20 bar sentuh)
- **EUR/JPY** (NO TRADE)
  - H1: resistance 174.5197 (0.37 ATR, 21 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance 174.45037 (0.84 ATR, 31 bar sentuh) · support tidak ada dalam jarak
- **EUR/CHF** (NO TRADE)
  - H1: resistance 0.91953 (0.54 ATR, 11 bar sentuh) · support 0.91819 (0.92 ATR, 17 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 0.91784 (0.77 ATR, 41 bar sentuh)
- **EUR/AUD** (NO TRADE)
  - H1: resistance 1.65051 (0.24 ATR, 12 bar sentuh) · support 1.64836 (0.52 ATR, 24 bar sentuh)
  - M15: resistance 1.65036 (0.28 ATR, 14 bar sentuh) · support tidak ada dalam jarak
- **EUR/CAD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 1.56922 (0.1 ATR, 10 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 1.56942 (0.14 ATR, 10 bar sentuh)
- **EUR/NZD** (NO TRADE)
  - H1: resistance 2.00646 (1.11 ATR, 15 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance 2.00387 (0.17 ATR, 37 bar sentuh) · support tidak ada dalam jarak
- **XAU/USD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 3616.21306 (1.02 ATR, 19 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 3620.81961 (0.24 ATR, 53 bar sentuh)
- **XAU/AUD** (NO TRADE)
  - H1: resistance 5495.14 (0.81 ATR, 14 bar sentuh) · support 5460.94038 (0.54 ATR, 17 bar sentuh)
  - M15: resistance 5461.95003 (0.43 ATR, 32 bar sentuh) · support tidak ada dalam jarak

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

