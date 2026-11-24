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


def _sel_cell(r):
    sel = r.get("sel")
    if not sel:
        return "—"
    return (f"{'★' * sel['bintang']} ({sel['bintang']}/5) · skor {sel['skor']} · n {sel['n']} · "
            f"PF {sel['pf']} · Exp {sel['exp']}R · DD {sel['dd']}R · fold {sel['fold']} · WR {sel['wr']}%")


def _lvl(x):
    if not x:
        return "tidak ada dalam jarak"
    return f"{x['harga']} ({x['jarak_atr']} ATR, {x['sentuhan']} bar sentuh)"


def _cad_block(r):
    cad = r.get("cadangan")
    if not cad:
        return []
    out = [f"- **{r['pair']}** ({r['label']})"]
    for key in ("h1", "m15"):
        t = cad.get(key)
        if t is None:
            out.append(f"  - {key.upper()}: tidak tersedia")
        else:
            out.append(f"  - {key.upper()}: resistance {_lvl(t.get('resistance'))} · "
                       f"support {_lvl(t.get('support'))}")
    return out


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
         f"- Timeframe sinyal: {C.TF_MAIN} (H1), bias {C.TF_BIAS}",
         f"- Ranking: {ranking_txt}",
         f"- Kalender: {_kalender(market_open, news_bersih, news_err)}",
         "- Spread: BELUM terverifikasi (OANDA belum tersambung), jadi tidak ada ENTRY." if not C.SPREAD_TERSEDIA
         else "- Spread: terverifikasi (OANDA).",
         "- Manajemen risiko §9: BELUM diimplementasi (tidak ada batas 3 trade/pair/hari atau korelasi).",
         f"- Celah waktu (gap): H1 di {gap_h1} pair, H4 di {gap_h4} pair. Biasanya akhir pekan atau libur, diabaikan.",
         ""]

    if rows:
        L += ["| Pair | Regime | Bias H4 | Label | Status | Mode | Arah | Kekuatan sel (backtest) | Harga (mid) "
              "| Entry / SL / TP | Bar H1/H4 | Bar terakhir (UTC) | Catatan |",
              "|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
        for r in rows:
            bar = r.get("bar") or {}
            L.append(f"| {r['pair']} | {r['regime']} | {r['bias']} | {r['label']} | {r.get('status') or '-'} "
                     f"| {r['metode'] or '-'} | {r['arah'] or '-'} | {_sel_cell(r)} "
                     f"| {r['harga'] if r['harga'] is not None else '-'} | {_entry_cell(r)} "
                     f"| {bar.get('h1', '-')}/{bar.get('h4', '-')} | {r.get('bar_terakhir') or '-'} "
                     f"| {'; '.join(r['catatan']) or '-'} |")
    else:
        L.append("Tidak ada pair yang dianalisa.")

    cad_rows = [r for r in rows if r.get("cadangan") and not r["label"].startswith("ENTRY")]
    L += ["", "## Analisa cadangan (BUKAN sinyal, tanpa entry, tanpa SL/TP, tanpa statistik)"]
    if cad_rows:
        L.append("Level S/R terdekat untuk konteks scalping. Tidak mengubah label atau keputusan apa pun.")
        for r in cad_rows:
            L += _cad_block(r)
    else:
        L.append("Tidak ada pair NO TRADE atau WATCHLIST, atau analisa cadangan dimatikan.")

    L += ["", "## Keterangan",
          "- **ENTRY LONG/SHORT**: semua syarat terpenuhi. Entry, SL, dan TP boleh dipakai.",
          "- **WATCHLIST**: metode ada, tetapi BELUM boleh entry. Lihat kolom Status. Tidak ada harga rencana.",
          "  - *Menunggu trigger*: belum ada sinyal dari metode prioritas.",
          "  - *Trigger ada - ditahan*: sinyal sudah muncul, tetapi dihentikan oleh news, kalender, atau spread.",
          "- **NO TRADE**: regime ini belum punya metode prioritas di ranking. Bukan sinyal jual atau beli.",
          "- **DATA INVALID**: candle gagal diambil atau tidak lolos validasi.",
          "- **Mode**: metode entry (FISHER, EMA_TREND, MACD, STOCH_MR, BB_SQUEEZE).",
          "- **Kekuatan sel**: hasil backtest untuk pair + regime + mode + arah ini. ★ = bintang 1 sampai 5 "
          "(skor 0-100). n = jumlah trade, PF = profit factor, Exp = rata-rata R per trade, "
          "DD = penurunan terbesar dalam R, fold = fold yang untung dari 4, WR = win rate.",
          f"- **Harga (mid)**: close candle {C.TF_MAIN} terakhir yang sudah tutup, rata-rata bid dan ask. Bukan harga live.",
          f"- **Bar H1/H4**: jumlah candle {C.TF_MAIN} dan H4 yang diterima dari biquote. EMA200 H4 butuh minimal 200 bar.",
          f"- **Analisa cadangan**: level dari M15 (±{C.CADANGAN_M15_MAX_ATR} ATR) dan H1 (±{C.CADANGAN_H1_MAX_ATR} ATR). "
          "Sentuhan = jumlah bar yang menyentuh area level.",
          ""]
    return "\n".join(L) + "\n"


def build_scanner_json(now, status, rows):
    return {"waktu": C.fmt(now), "status": status, "rows": rows}
