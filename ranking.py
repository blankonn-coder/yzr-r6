"""Statistik, skor, bintang, dan ranking aktif (§7, §7b)."""
import json
import os

import config as C


def _clamp01(x):
    return max(0.0, min(1.0, x))


def stats(trades):
    """Statistik dari daftar trade (field: r, fold). None jika tidak ada trade."""
    rs = [t["r"] for t in trades]
    n = len(rs)
    if n == 0:
        return None
    wins = sum(r for r in rs if r > 0)
    losses = -sum(r for r in rs if r <= 0)
    if losses > 0:
        pf = wins / losses
    else:
        pf = 99.0 if wins > 0 else 0.0
    pf = min(pf, 99.0)
    eq = peak = dd = 0.0
    for r in rs:
        eq += r
        peak = max(peak, eq)
        dd = max(dd, peak - eq)
    fold_sum = [0.0] * C.N_FOLDS
    for t in trades:
        fold_sum[t["fold"]] += t["r"]
    return {"n": n, "pf": round(pf, 3), "exp": round(sum(rs) / n, 4), "dd": round(dd, 2),
            "fold_pos": sum(1 for x in fold_sum if x > 0),
            "wr": round(100 * sum(1 for r in rs if r > 0) / n, 1)}


def score(st):
    pf_s = 25 * _clamp01(st["pf"] - 1)
    exp_s = 25 * _clamp01(st["exp"] / 0.3)
    dd_s = 20 * _clamp01(1 - st["dd"] / 15)
    fold_s = 15 * st["fold_pos"] / C.N_FOLDS
    samp_s = 10 * _clamp01(st["n"] / 100)
    wr = st["wr"]
    dist = 0 if 35 <= wr <= 65 else (35 - wr if wr < 35 else wr - 65)
    wr_s = 5 * _clamp01(1 - dist / 15)
    return round(pf_s + exp_s + dd_s + fold_s + samp_s + wr_s)


def star(skor):
    if skor >= 90:
        return 5
    if skor >= 80:
        return 4
    if skor >= 70:
        return 3
    if skor >= 60:
        return 2
    return 1


def make_record(pair, regime, metode, arah, trades, meta):
    st = stats(trades)
    gagal = []
    if st["pf"] <= C.RANK_PF_MIN:
        gagal.append("PF<=1")
    if st["exp"] <= C.RANK_EXP_MIN:
        gagal.append("expectancy<=0")
    if st["dd"] > C.RANK_DD_MAX:
        gagal.append("DD>15R")
    provisional = st["n"] < C.RANK_MIN_SAMPLE
    skor = score(st)
    return {"waktu": meta["waktu"], "pair": pair, "regime": regime, "metode": metode, "arah": arah,
            "pf": st["pf"], "exp": st["exp"], "dd": st["dd"], "fold": f"{st['fold_pos']}/{C.N_FOLDS}",
            "n": st["n"], "wr": st["wr"], "skor": skor,
            "bintang": None if provisional else star(skor),
            "lolos": not gagal, "gagal": "; ".join(gagal), "provisional": provisional,
            "news_filter": meta["news_filter"], "periode": meta["periode"]}


def append_history(path, records):
    d = os.path.dirname(path)
    if d:
        os.makedirs(d, exist_ok=True)
    with open(path, "a", encoding="utf-8") as f:
        for r in records:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")


def load_active(path=C.RANKING_HISTORY_PATH):
    """Baris terbaru per (pair, regime, metode, arah). Hanya yang lolos, bukan provisional, bintang >= 3.

    Return {(pair, regime): [ {metode, arah, bintang, skor}, ... ]} urut bintang desc, skor desc.
    """
    if not os.path.exists(path):
        return {}
    latest = {}
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            r = json.loads(line)
            latest[(r["pair"], r["regime"], r["metode"], r["arah"])] = r
    out = {}
    for r in latest.values():
        if r["lolos"] and not r["provisional"] and (r["bintang"] or 0) >= C.RANK_PRIORITY_STARS:
            out.setdefault((r["pair"], r["regime"]), []).append(
                {"metode": r["metode"], "arah": r["arah"], "bintang": r["bintang"], "skor": r["skor"]})
    for lst in out.values():
        lst.sort(key=lambda x: (-x["bintang"], -x["skor"]))
    return out


def render_md(records, meta, warnings):
    L = [f"# Ranking Backtest — {meta['waktu']}", ""]
    L.append(f"- Periode data: {meta['periode']}")
    L.append(f"- Filter news: {'aktif' if meta['news_filter'] else 'tanpa filter news'}")
    if warnings:
        L.append("- Pair dilewati: " + "; ".join(warnings))
    L.append("")
    if not records:
        L.append("Tidak ada hasil (tidak ada trade atau semua pair dilewati).")
        return "\n".join(L) + "\n"
    grup = {}
    for r in records:
        grup.setdefault((r["pair"], r["regime"]), []).append(r)
    for (pair, reg) in sorted(grup):
        L += [f"## {pair.replace('_', '/')} — {reg}", "",
              "| Metode | Arah | Bintang | Skor | PF | Exp | DD | Fold | n | WR | Status |",
              "|---|---|---|---|---|---|---|---|---|---|---|"]
        for r in sorted(grup[(pair, reg)], key=lambda x: (-(x["bintang"] or 0), -x["skor"])):
            bint = "—" if r["bintang"] is None else str(r["bintang"])
            status = "PROVISIONAL" if r["provisional"] else ("lolos" if r["lolos"] else f"gagal ({r['gagal']})")
            L.append(f"| {r['metode']} | {r['arah']} | {bint} | {r['skor']} | {r['pf']} | {r['exp']} "
                     f"| {r['dd']} | {r['fold']} | {r['n']} | {r['wr']}% | {status} |")
        L.append("")
    L += ["Catatan kaki:",
          "- Parameter tidak dioptimasi; semua fold out-of-sample.",
          "- XAU_USD: satuan harga USD, 1 pip = 0.1 USD.",
          "- Bintang kosong (—) = PROVISIONAL (n < 30), tidak dipakai scanner.", ""]
    return "\n".join(L) + "\n"
