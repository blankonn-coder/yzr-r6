"""Backtest dan ranking (§6, §7, §7b). Jalankan lokal:

    python -m backtest.run                 # semua pair
    python -m backtest.run --pairs EUR_USD,XAU_USD

Hasil: append ke database/ranking_history.jsonl dan tulis reports/ranking.md.
"""
import argparse
import json
import os
import sys

import analysis
import config as C
import ranking
from backtest import dukascopy_loader as DL
from backtest.engine import resample, simulate
from data_quality import validate
from strategies import REGISTRY


def load_news_archive():
    """Arsip news high-impact (epoch detik). None jika arsip belum ada -> simulasi tanpa filter news."""
    if not os.path.exists(C.NEWS_ARCHIVE_PATH):
        return None
    out = []
    with open(C.NEWS_ARCHIVE_PATH, encoding="utf-8") as f:
        for line in f:
            if line.strip():
                e = json.loads(line)
                if str(e.get("impact", "high")).lower() == "high":
                    out.append(C.to_epoch(e["time"]))
    return sorted(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pairs", default="", help="dipisah koma; kosong = semua pair")
    args = ap.parse_args()
    pairs = [p.strip().upper().replace("/", "_") for p in args.pairs.split(",") if p.strip()] or C.PAIRS

    news = load_news_archive()
    now = C.utc_now()
    records, warnings, periode = [], [], []
    for pair in pairs:
        try:
            m1 = DL.load_m1(pair)
        except Exception as e:
            warnings.append(f"{C.disp(pair)} ({e})")
            continue
        h1, h4 = resample(m1, 3600), resample(m1, 14400)
        ok1, e1, w1 = validate(h1, 3600, bidask=True)
        ok4, e4, w4 = validate(h4, 14400, bidask=True)
        if not (ok1 and ok4):
            warnings.append(f"{C.disp(pair)} DATA INVALID ({'; '.join(e1 + e4)})")
            continue
        if w1 or w4:
            print(f"{C.disp(pair)} peringatan data: {'; '.join(w1 + w4)}")
        ctx = analysis.build(h1, h4)
        n = len(h1)
        periode.append(f"{h1[0]['t']}-{h1[-1]['t']}")
        meta = {"waktu": C.fmt(now), "news_filter": news is not None,
                "periode": f"{pair} {h1[0]['t']} s.d. {h1[-1]['t']} (epoch)"}
        groups = {}
        for name, method in REGISTRY.items():
            for t in simulate(pair, ctx, method, news):
                t["fold"] = min(C.N_FOLDS - 1, t["entry_idx"] * C.N_FOLDS // n)
                groups.setdefault((t["regime"], name, t["arah"]), []).append(t)
        for (reg, name, arah), trades in sorted(groups.items()):
            records.append(ranking.make_record(pair, reg, name, arah, trades, meta))
        print(f"{C.disp(pair)}: {sum(len(v) for v in groups.values())} trade")

    meta_all = {"waktu": C.fmt(now), "news_filter": news is not None,
                "periode": "; ".join(periode) or "-"}
    if records:
        ranking.append_history(C.RANKING_HISTORY_PATH, records)
    os.makedirs(os.path.dirname(C.RANKING_MD_PATH), exist_ok=True)
    with open(C.RANKING_MD_PATH, "w", encoding="utf-8") as f:
        f.write(ranking.render_md(records, meta_all, warnings))
    print(f"Selesai: {len(records)} baris ranking, {len(warnings)} pair dilewati.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
