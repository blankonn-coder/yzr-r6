# Forex Screening Bot

Struktur repositori (semua folder berada di root):

- `src/` kode bot (jalankan dengan `python -m src.main`)
- `state/` status kalibrasi dan pemantauan
- `database/signal_history.json` database sinyal mentah
- `reports/latest_report.md` laporan run terakhir
- `.github/workflows/forex_scalper.yml` jadwal GitHub Actions

Secret yang dibutuhkan: `OANDA_API_KEY` (wajib), `FINEX_REFERENCE_JSON` (opsional).

Notifikasi Discord (opsional):
- Secret `DISCORD_WEBHOOK_URL`: URL webhook channel Discord.
- Variable `DISCORD_NOTIFY_MODE`: `signal` (default, hanya saat ada BUY/SELL), `always`, atau `off`.
