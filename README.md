# Adaptive Forex Scanner (Skema FINAL BERSIH v2)

Scanner forex per jam berbasis regime pasar H1 dan ranking hasil backtest.
Spesifikasi lengkap ada di dokumen skema; file ini merangkum cara kerja dan batasannya.

## Alur
1. **Backtest** (lokal, tiap 3 bulan): `python -m backtest.run`
   - Data M1 bid/ask dari cache CSV (`DUKASCOPY_CACHE_DIR`).
   - Lima metode diuji per pair, dibagi 4 fold out-of-sample, tanpa optimasi parameter.
   - Hasil di-append ke `database/ranking_history.jsonl` dan ditulis ke `reports/ranking.md`.
2. **Scanner live** (GitHub Actions, menit ke-5 tiap jam): `python main.py`
   - Ambil H1 dan H4 tertutup dari biquote, validasi, hitung regime dan bias H4.
   - Ambil metode PRIORITAS untuk pair + regime dari ranking aktif (bintang ≥ 3, lolos penguci).
   - Tanpa ranking aktif, semua pair berlabel NO TRADE.
   - Hasil: `reports/scanner_latest.md`, `scanner/latest.json`, dan Discord.

## Label
- `ENTRY LONG/SHORT`: trigger terpenuhi, tidak ada news ±30 menit, dan spread terverifikasi.
- `WATCHLIST`: metode ada tetapi trigger belum, ada news, kalender gagal, atau spread belum terverifikasi.
- `NO TRADE`: tidak ada metode PRIORITAS untuk regime tersebut.
- `DATA INVALID`: gagal ambil atau validasi data.

## Keadaan saat ini
- Spread live belum tersambung (`SPREAD_TERSEDIA = False`), sehingga tidak ada ENTRY.
- Ranking belum ada, sehingga scanner hanya menghasilkan NO TRADE.
- §9 manajemen risiko (batas 3 trade/pair/hari, korelasi) belum diimplementasi.

## Yang belum diverifikasi (ASUMSI)
- Endpoint dan skema kalender biquote (`BIQUOTE_CALENDAR_PATH`). Jika gagal, scanner tidak membuat ENTRY.
- Batas jumlah candle per request di biquote (`H1_COUNT`, `H4_COUNT`).
- Integrasi dukascopy-downloader. Saat ini loader membaca CSV dari cache; format ada di `backtest/dukascopy_loader.py`.
- Periode indikator standar (ATR 14, ADX 14, MACD 12/26/9, Stoch 14/3/3, BB 20/2, Fisher 10).
  Spesifikasi tidak menyebutkannya.

## Konfigurasi GitHub
- Secret `DISCORD_WEBHOOK_URL`
- Variable `DISCORD_NOTIFY_MODE` (`signal` default | `always` | `off`)

## Tes
    python -m pytest tests/
