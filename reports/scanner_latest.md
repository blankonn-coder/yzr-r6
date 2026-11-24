# Laporan Scanner Adaptive Forex

- Waktu eksekusi: 2026-11-24T13:45:25Z
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
Tidak ada saran (tidak ada level H1 dalam jarak 1.0 ATR).

## Pemantauan 15 menit (entry dan analisa cadangan)
Nilai di kolom 15m-60m = pip dari entry pada close candle M15 ke-1 sampai ke-4. Jika SL dan TP kena di candle yang sama, dihitung SL. Analisa cadangan BUKAN sinyal.
| Sumber | Pair | Arah | Entry | SL | TP | 15m | 30m | 45m | 60m | Hasil | Pip sekarang | Umur |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ANALISA CADANGAN (bukan sinyal) | EUR/USD | BUY | 1.09602 | 1.09536 | 1.09701 | +5.1 | +1.4 | -1.2 | - | BERJALAN | LOSS 1.2 pip | 45 mnt |
| ANALISA CADANGAN (bukan sinyal) | EUR/GBP | SELL | 0.83688 | 0.83724 | 0.83634 | -2.5 | +0.2 | -0.4 | - | BERJALAN | LOSS 0.4 pip | 45 mnt |
| ANALISA CADANGAN (bukan sinyal) | GBP/USD | BUY | 1.30966 | 1.30868 | 1.31112 | +2.2 | +1.9 | -2.1 | - | BERJALAN | LOSS 2.1 pip | 45 mnt |
| ANALISA CADANGAN (bukan sinyal) | EUR/JPY | SELL | 174.4455 | 174.64589 | 174.14491 | +5.1 | +0.9 | +0.7 | - | BERJALAN | PROFIT 0.7 pip | 45 mnt |
| ANALISA CADANGAN (bukan sinyal) | EUR/AUD | BUY | 1.64925 | 1.647 | 1.65263 | +21.8 | +8.4 | +8.2 | - | BERJALAN | PROFIT 8.2 pip | 45 mnt |
| ANALISA CADANGAN (bukan sinyal) | USD/CAD | BUY | 1.43314 | 1.43226 | 1.43445 | -2.3 | -7.2 | -5.5 | - | BERJALAN | LOSS 5.5 pip | 30 mnt |
| ANALISA CADANGAN (bukan sinyal) | XAU/AUD | SELL | 5480.731 | 5508.06444 | 5439.73083 | +113.8 | +209.0 | +342.7 | - | BERJALAN | PROFIT 342.7 pip | 30 mnt |
| ANALISA CADANGAN (bukan sinyal) | EUR/CHF | SELL | 0.91893 | 0.92 | 0.91732 | +9.1 | +9.9 | +8.4 | - | BERJALAN | PROFIT 8.4 pip | 30 mnt |
| ANALISA CADANGAN (bukan sinyal) | NZD/USD | SELL | 0.54706 | 0.54795 | 0.54573 | -0.4 | +0.6 | +0.8 | - | BERJALAN | PROFIT 0.8 pip | 30 mnt |
| ANALISA CADANGAN (bukan sinyal) | AUD/USD | SELL | 0.66456 | 0.66609 | 0.66226 | +5.5 | +2.7 | +4.2 | - | BERJALAN | PROFIT 4.2 pip | 30 mnt |

## Evaluasi 1 jam (entry dan analisa cadangan)
Dibuat setelah 60 menit atau saat SL/TP kena. MFE = gerak terbaik, MAE = gerak terburuk, dalam pip.
Belum ada evaluasi yang selesai di run ini.

## Level analisa cadangan (BUKAN sinyal, tanpa statistik)
Level S/R terdekat untuk konteks scalping. Tidak mengubah label atau keputusan apa pun.
- **EUR/USD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 1.09599 (0.02 ATR, 19 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 1.09575 (0.21 ATR, 10 bar sentuh)
- **GBP/USD** (NO TRADE)
  - H1: resistance 1.31042 (0.53 ATR, 25 bar sentuh) · support 1.3094 (0.18 ATR, 20 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 1.30913 (0.4 ATR, 23 bar sentuh)
- **USD/JPY** (NO TRADE)
  - H1: resistance 159.41066 (1.33 ATR, 50 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance 159.24775 (0.65 ATR, 22 bar sentuh) · support tidak ada dalam jarak
- **USD/CHF** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support tidak ada dalam jarak
  - M15: resistance 0.8379 (0.18 ATR, 13 bar sentuh) · support tidak ada dalam jarak
- **AUD/USD** (NO TRADE)
  - H1: resistance 0.66551 (0.81 ATR, 18 bar sentuh) · support 0.66346 (0.94 ATR, 23 bar sentuh)
  - M15: resistance 0.66466 (0.89 ATR, 31 bar sentuh) · support tidak ada dalam jarak
- **USD/CAD** (NO TRADE)
  - H1: resistance 1.43386 (0.71 ATR, 27 bar sentuh) · support 1.43278 (0.35 ATR, 39 bar sentuh)
  - M15: resistance 1.43269 (0.15 ATR, 30 bar sentuh) · support tidak ada dalam jarak
- **NZD/USD** (NO TRADE)
  - H1: resistance 0.54756 (0.65 ATR, 14 bar sentuh) · support 0.54628 (1.01 ATR, 6 bar sentuh)
  - M15: resistance 0.54722 (0.6 ATR, 28 bar sentuh) · support tidak ada dalam jarak
- **EUR/GBP** (NO TRADE)
  - H1: resistance 0.83698 (0.18 ATR, 24 bar sentuh) · support 0.83661 (0.52 ATR, 30 bar sentuh)
  - M15: resistance 0.83713 (0.73 ATR, 23 bar sentuh) · support tidak ada dalam jarak
- **EUR/JPY** (NO TRADE)
  - H1: resistance 174.5197 (0.29 ATR, 22 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance 174.4535 (0.11 ATR, 31 bar sentuh) · support tidak ada dalam jarak
- **EUR/CHF** (NO TRADE)
  - H1: resistance 0.91953 (0.62 ATR, 11 bar sentuh) · support 0.91819 (0.78 ATR, 18 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 0.91783 (0.39 ATR, 48 bar sentuh)
- **EUR/AUD** (NO TRADE)
  - H1: resistance 1.65051 (0.46 ATR, 13 bar sentuh) · support 1.64836 (0.33 ATR, 25 bar sentuh)
  - M15: resistance 1.65031 (0.16 ATR, 17 bar sentuh) · support tidak ada dalam jarak
- **EUR/CAD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support 1.56922 (1.03 ATR, 12 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 1.56942 (0.49 ATR, 11 bar sentuh)
- **EUR/NZD** (NO TRADE)
  - H1: resistance 2.00637 (1.25 ATR, 15 bar sentuh) · support tidak ada dalam jarak
  - M15: resistance 2.00388 (0.33 ATR, 44 bar sentuh) · support tidak ada dalam jarak
- **XAU/USD** (NO TRADE)
  - H1: resistance tidak ada dalam jarak · support tidak ada dalam jarak
  - M15: resistance 3620.05122 (0.29 ATR, 52 bar sentuh) · support tidak ada dalam jarak
- **XAU/AUD** (NO TRADE)
  - H1: resistance 5495.14 (0.56 ATR, 14 bar sentuh) · support 5460.94038 (0.77 ATR, 18 bar sentuh)
  - M15: resistance tidak ada dalam jarak · support 5435.56775 (0.8 ATR, 19 bar sentuh)

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

