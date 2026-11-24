"""Laporan scanner: reports/scanner_latest.md dan scanner/latest.json."""
import config as C


def _news_status(market_open, news_bersih, news_err):
    if not market_open:
        return "PASAR TUTUP"
    if news_bersih is None:
        return f"GAGAL diperiksa ({news_err}): tidak ada ENTRY baru"
    return "tidak ada news ±30 menit" if news_bersih else "ADA news high-impact ±30 menit"


def build_scanner_md(now, status, rows, ranking_ok, news_bersih, news_err, market_open=True):
    L = ["# Laporan Scanner Adaptive Forex", "",
         f"- Waktu eksekusi: {C.fmt(now)}",
         f"- Status: {status}",
         f"- Ranking aktif: {'ada' if ranking_ok else 'KOSONG (belum ada backtest) -> hanya NO TRADE'}",
         f"- Kalender: {_news_status(market_open, news_bersih, news_err)}",
         f"- Spread: {'terverifikasi' if C.SPREAD_TERSEDIA else 'BELUM terverifikasi (OANDA belum tersambung): sinyal jadi WATCHLIST'}",
         "- Manajemen risiko §9: BELUM diimplementasi. Scanner tidak membatasi 3 trade/pair/hari "
         "maupun korelasi mata uang.",
         f"- Pair dianalisa: {len(rows)}", ""]
    if rows:
        L += ["| Pair | Regime | Bias H4 | Label | Metode | Arah | Harga | Entry | SL | TP | Catatan |",
              "|---|---|---|---|---|---|---|---|---|---|---|"]
        for r in rows:
            L.append(f"| {r['pair']} | {r['regime']} | {r['bias']} | {r['label']} | {r['metode'] or '-'} "
                     f"| {r['arah'] or '-'} | {r['harga'] if r['harga'] is not None else '-'} "
                     f"| {r['entry'] or '-'} | {r['sl'] or '-'} | {r['tp'] or '-'} "
                     f"| {'; '.join(r['catatan']) or '-'} |")
    else:
        L.append("Tidak ada pair yang dianalisa.")
    return "\n".join(L) + "\n"


def build_scanner_json(now, status, rows):
    return {"waktu": C.fmt(now), "status": status, "rows": rows}
