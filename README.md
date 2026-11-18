## Cooldown sinyal
- Pair yang sudah muncul BUY/SELL tidak muncul lagi di hasil screening (laporan, Discord, database) dengan arah yang sama selama 60 menit sejak sinyal pertama (`COOLDOWN_MINUTES`). Pemantauan berjalan selama 60 menit yang sama.
- Arah berlawanan boleh masuk screening sebagai sinyal baru; sinyal lama ditutup dan pemantauan dimulai ulang.
- Status disimpan di `state/cooldown_state.json`.
