"""Laporan scanner: reports/scanner_latest.md dan scanner/latest.json."""
import config as C


def _kalender(market_open, news_bersih, news_err):
    if not market_open:
        return "pasar tutup"
    if news_bersih is None:
        return f"gagal diperiksa ({news_err}), tidak ada ENTRY"
    return "bersih (tidak ada news ±30 menit)" if news_bersih else "ADA news high-impact ±30 menit"


def _ringkasan(rows):
    hitung = {}
    for r in rows:
        key = "ENTRY" if r["label"].startswith("ENTRY") else r["label"]
        hitung[key] = hitung.get(key, 0) + 1
    return ", ".join(f"{k} {hitung.get(k, 0)}" for k in ("ENTRY", "WATCHLIST", "NO TRADE", "DATA INVALID"))


def _entry_cell(r):
    if r["label"].startswith("ENTRY"):
        return f"{r['entry']} / {r['sl']} / {r['tp']}"
    return "—"


def build_scanner_md(now, status, rows, ranking_ok, news_bersih, news_err, market_open=True, rank_meta=None):
    gap_h1 = sum(1 for r in rows if (r.get("gap") or {}).get("H1"))
    gap_h4 = sum(1 for r in rows if (r.get("gap") or {}).get("H4"))

    if not ranking_ok:
        ranking_txt = "KOSONG (belum ada backtest). Semua pair jadi NO TRADE."
    else:
        ranking_txt = "ada"
        if rank_meta:
            ranking_txt += f" (dibuat {rank_meta['waktu']}, {'dengan' if rank_meta['news_filter'] else 'TANPA'} filter news)"

    L = ["# Laporan Scanner Adaptive Forex", "",
         f"- Waktu eksekusi: {C.fmt(now)}",
         f"- Status run: {status}",
         f"- Ringkasan: {_ringkasan(rows)}",
         f"- Ranking: {ranking_txt}",
         f"- Kalender: {_kalender(market_open, news_bersih, news_err)}",
         "- Spread: BELUM terverifikasi (OANDA belum tersambung), jadi tidak ada ENTRY." if not C.SPREAD_TERSEDIA
         else "- Spread: terverifikasi (OANDA).",
         "- Manajemen risiko §9: BELUM diimplementasi (tidak ada batas 3 trade/pair/hari atau korelasi).",
         f"- Celah waktu (gap): H1 di {gap_h1} pair, H4 di {gap_h4} pair. Biasanya akhir pekan atau libur, diabaikan.",
         ""]

    if rows:
        L += ["| Pair | Regime | Bias H4 | Label | Status | Metode | Arah | Harga (mid) | Entry / SL / TP "
              "| Bar H1/H4 | Bar terakhir (UTC) | Catatan |",
              "|---|---|---|---|---|---|---|---|---|---|---|---|"]
        for r in rows:
            bar = r.get("bar") or {}
            L.append(f"| {r['pair']} | {r['regime']} | {r['bias']} | {r['label']} | {r.get('status') or '-'} "
                     f"| {r['metode'] or '-'} | {r['arah'] or '-'} "
                     f"| {r['harga'] if r['harga'] is not None else '-'} | {_entry_cell(r)} "
                     f"| {bar.get('h1', '-')}/{bar.get('h4', '-')} | {r.get('bar_terakhir') or '-'} "
                     f"| {'; '.join(r['catatan']) or '-'} |")
    else:
        L.append("Tidak ada pair yang dianalisa.")

    L += ["", "## Keterangan",
          "- **ENTRY LONG/SHORT**: semua syarat terpenuhi. Entry, SL, dan TP boleh dipakai.",
          "- **WATCHLIST**: metode ada, tetapi BELUM boleh entry. Lihat kolom Status. Tidak ada harga rencana.",
          "  - *Menunggu trigger*: belum ada sinyal dari metode prioritas.",
          "  - *Trigger ada - ditahan*: sinyal sudah muncul, tetapi dihentikan oleh news, kalender, atau spread.",
          "- **NO TRADE**: regime ini belum punya metode prioritas di ranking. Bukan sinyal jual atau beli.",
          "- **DATA INVALID**: candle gagal diambil atau tidak lolos validasi.",
          "- **Harga (mid)**: close candle H1 terakhir yang sudah tutup, rata-rata bid dan ask. Bukan harga live.",
          "- **Bar H1/H4**: jumlah candle yang diterima dari biquote. EMA200 H4 butuh minimal 200 bar.",
          ""]
    return "\n".join(L) + "\n"


def build_scanner_json(now, status, rows):
    return {"waktu": C.fmt(now), "status": status, "rows": rows}
