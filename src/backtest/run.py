"""Jalankan backtest metode A-E untuk pair tertentu (tahap 3).

Contoh:
  python -m src.backtest.run --pairs EUR_USD --start 2026-10-01 --end 2026-10-31
  python -m src.backtest.run --pairs EUR_USD --start 2024-01-01 --end 2026-10-31 --unduh
Hasil: results/backtest/trades.csv, results/ranking/ranking.json, ranking.md, history.jsonl
"""
import argparse
import json
import math
import os
from datetime import datetime, timezone

import numpy as np
import pandas as pd

from ..data.dukascopy import unduh, muat
from ..indicators import build
from ..methods import METODE
from ..regime import classify
from ..resample import resample_ohlc, bias_h4
from ..config import pip_size
from .engine import simulate, PARAMS
from .metrics import ringkas
from .ranking import skor, bintang, kelayakan

FOLDS = 4
SPREAD_MAX_PIP = {"EUR_USD": 2.0}   # batas absolut spread per pair (default 3.0)
SPREAD_MAX_DEFAULT = 3.0
NEWS_WINDOW_MIN = 30


def _samakan(bid_m1, ask_m1):
    m = bid_m1.merge(ask_m1, on="time", suffixes=("_b", "_a"))
    bid = m[["time", "open_b", "high_b", "low_b", "close_b", "volume_b"]].rename(columns=lambda c: c.replace("_b", ""))
    ask = m[["time", "open_a", "high_a", "low_a", "close_a", "volume_a"]].rename(columns=lambda c: c.replace("_a", ""))
    mid = bid[["time"]].copy()
    for c in ("open", "high", "low", "close"):
        mid[c] = (bid[c].to_numpy() + ask[c].to_numpy()) / 2
    mid["volume"] = bid["volume"].to_numpy()
    return bid, ask, mid


def siapkan(pair, start, end, news_times=None):
    bid_m1 = muat(pair, "BID", start, end)
    ask_m1 = muat(pair, "ASK", start, end)
    bid_m1, ask_m1, mid_m1 = _samakan(bid_m1, ask_m1)
    pip = pip_size(pair)
    bid = resample_ohlc(bid_m1, "H1")
    ask = resample_ohlc(ask_m1, "H1")
    mid = resample_ohlc(mid_m1, "H1")
    t = set(bid["time"]) & set(ask["time"]) & set(mid["time"])
    bid, ask, mid = (x[x["time"].isin(t)].sort_values("time").reset_index(drop=True) for x in (bid, ask, mid))
    h4 = bias_h4(resample_ohlc(mid_m1, "H4"))
    ind = build(mid)
    reg = classify(ind)

    spread = (ask["close"] - bid["close"]) / pip
    med = spread.rolling(20).median()
    batas = SPREAD_MAX_PIP.get(pair, SPREAD_MAX_DEFAULT)
    spread_ok = ((spread <= 1.5 * med) | med.isna()) & (spread <= batas)
    entry_ok = np.r_[False, spread_ok.to_numpy()[:-1]]  # keputusan di open bar i memakai spread bar i-1
    if news_times:
        ntimes = pd.to_datetime(pd.Series(news_times), utc=True).to_numpy()
        tb = bid["time"].to_numpy()
        dekat = np.zeros(len(tb), dtype=bool)
        for nt in ntimes:
            dekat |= np.abs((tb - nt) / np.timedelta64(1, "m")) <= NEWS_WINDOW_MIN
        entry_ok &= ~dekat
    return {"bid": bid, "ask": ask, "mid": mid, "ind": ind, "reg": reg, "h4": h4,
            "pip": pip, "entry_ok": entry_ok, "spread_pip": spread}


def jalankan(pair, data, metode_list=None):
    trades_all = []
    n = len(data["mid"])
    for kode in (metode_list or list(METODE)):
        mod = METODE[kode]
        sig = mod.signals(data["mid"], data["pip"], h4_bias=data["h4"])
        sig = sig.reset_index(drop=True)
        tr, _ = simulate(kode, sig, data["bid"], data["ask"], data["mid"], data["ind"], data["pip"],
                         entry_ok=data["entry_ok"])
        for t in tr:
            i0 = t["entry_i"]
            t.update({
                "metode": kode,
                "pair": pair,
                "tf": "H1",
                "waktu_entry": str(data["bid"]["time"].iloc[i0]),
                "waktu_exit": str(data["bid"]["time"].iloc[t["exit_i"]]),
                "regime": data["reg"]["regime"].iloc[t["sig_i"]],
                "squeeze": bool(data["reg"]["squeeze"].iloc[t["sig_i"]]),
                "arah": "LONG" if t["dir"] == 1 else "SHORT",
                "fold": int(min(FOLDS - 1, i0 * FOLDS // n)),
            })
        trades_all.extend(tr)
    return pd.DataFrame(trades_all)


def peringkat(trades, rentang):
    baris = []
    if trades.empty:
        return baris
    for (pair, regime, metode, arah), g in trades.groupby(["pair", "regime", "metode", "arah"]):
        m = ringkas(g["r"].to_numpy(), g["fold"].to_numpy(), FOLDS)
        s = skor(m)
        ok, alasan = kelayakan(m)
        b, status = bintang(s, m["trade"], ok)
        baris.append({
            "pair": pair, "tf": "H1", "regime": regime, "metode": metode, "arah": arah,
            "bintang": b, "skor": s, "pf": m["pf"], "win_rate": m["win_rate"],
            "expectancy_r": m["expectancy_r"], "max_dd_r": m["max_dd_r"], "sampel": m["trade"],
            "status": status, "alasan_tidak_lolos": alasan, "rentang_uji": rentang,
            "tanggal_uji": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        })
    baris.sort(key=lambda x: (-x["bintang"], -x["skor"]))
    return baris


def _json_aman(x):
    """Ganti inf/NaN dengan string/None agar JSON standar."""
    if isinstance(x, float) and not math.isfinite(x):
        return "inf" if x > 0 else None
    if isinstance(x, dict):
        return {k: _json_aman(v) for k, v in x.items()}
    if isinstance(x, list):
        return [_json_aman(v) for v in x]
    return x


def tulis(baris, trades, rentang):
    os.makedirs("results/backtest", exist_ok=True)
    os.makedirs("results/ranking", exist_ok=True)
    if not trades.empty:
        trades.to_csv("results/backtest/trades.csv", index=False)
    with open("results/ranking/ranking.json", "w", encoding="utf-8") as f:
        json.dump(_json_aman({"rentang": rentang, "baris": baris}), f, ensure_ascii=False, indent=2, default=str)
    with open("results/ranking/history.jsonl", "a", encoding="utf-8") as f:
        for b in baris:
            f.write(json.dumps(_json_aman(b), ensure_ascii=False, default=str) + "\n")
    with open("results/ranking/ranking.md", "w", encoding="utf-8") as f:
        f.write("| Pair | TF | Regime | Metode | Arah | Bintang | PF | Win% | Exp R | MaxDD R | Sampel | Status |\n")
        f.write("|---|---|---|---|---|---|---|---|---|---|---|---|\n")
        for b in baris:
            pf = "inf" if b["pf"] == float("inf") else (f"{b['pf']:.2f}" if b["pf"] is not None else "-")
            wr = f"{b['win_rate'] * 100:.1f}" if b["win_rate"] is not None else "-"
            ex = f"{b['expectancy_r']:.3f}" if b["expectancy_r"] is not None else "-"
            dd = f"{b['max_dd_r']:.2f}" if b["max_dd_r"] is not None else "-"
            f.write(f"| {b['pair'].replace('_', '/')} | H1 | {b['regime']} | {b['metode']} | {b['arah']} | "
                    f"{'★' * b['bintang']}{'☆' * (5 - b['bintang'])} | {pf} | {wr} | {ex} | {dd} | {b['sampel']} | {b['status']} |\n")
        f.write(f"\nRentang uji: {rentang}. Parameter tidak dioptimasi; semua fold adalah out-of-sample.\n")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pairs", default="EUR_USD")
    ap.add_argument("--start", required=True)
    ap.add_argument("--end", required=True)
    ap.add_argument("--unduh", action="store_true", help="unduh Dukascopy dulu")
    ap.add_argument("--news", default="", help="daftar waktu UTC news high-impact, dipisah koma (kosong = tanpa filter news)")
    a = ap.parse_args()
    rentang = f"{a.start} s/d {a.end}"
    news = [x.strip() for x in a.news.split(",") if x.strip()]
    semua = []
    for pair in [p.strip() for p in a.pairs.split(",") if p.strip()]:
        if a.unduh:
            unduh(pair, a.start)
        print(f"Menyiapkan {pair} ...")
        data = siapkan(pair, a.start, a.end, news_times=news)
        tr = jalankan(pair, data)
        print(f"  trade: {len(tr)}")
        semua.append(tr)
    trades = pd.concat(semua, ignore_index=True) if semua else pd.DataFrame()
    baris = peringkat(trades, rentang)
    tulis(baris, trades, rentang)
    print(f"Selesai. Trade: {len(trades)}. Hasil di results/ranking/ranking.md")


if __name__ == "__main__":
    main()
