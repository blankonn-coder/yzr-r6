"""Scanner live, polling 15 menit: python main.py

Satu siklus per bar M15 yang sudah tutup:
pemantauan -> ambil data (biquote) -> validasi -> analisa -> catat entry -> laporan + Discord.
Kegagalan data menghasilkan DATA INVALID (tanpa entry). Tidak ada error yang keluar dari fungsi ini.
"""
import math
import os
import sys
import time
from concurrent.futures import ThreadPoolExecutor

import requests

import config as C
import engine as E
import pantauan as PT


# ---------------- biquote ----------------

def fetch_candles(pair, interval, count, retry=5):
    """Candle selesai, urut lama -> baru. Bar yang masih berjalan dibuang."""
    url = f"{C.BIQUOTE_HOST}/api/{pair.replace('_', '')}/ohlc"
    delay = 1.0
    for _ in range(retry):
        r = requests.get(url, params={"interval": interval, "limit": count}, timeout=20)
        if r.status_code in (429, 503) or r.status_code >= 500:
            time.sleep(min(delay, 30))
            delay *= 2
            continue
        if r.status_code != 200:
            raise RuntimeError(f"HTTP {r.status_code}")
        out = sorted(({"t": C.to_epoch(b["openTime"]), "o": float(b["open"]), "h": float(b["high"]),
                       "l": float(b["low"]), "c": float(b["close"])}
                      for b in r.json().get("bars", []) if not b.get("isOpen")), key=lambda x: x["t"])
        if len(out) < 60:
            raise RuntimeError(f"bar kurang ({len(out)})")
        return out
    raise RuntimeError("gagal setelah beberapa percobaan (rate limit/server)")


def fetch_news():
    """Waktu epoch event high-impact. ASUMSI: endpoint dan skema JSON belum diverifikasi."""
    r = requests.get(C.BIQUOTE_HOST + C.CALENDAR_PATH, timeout=20)
    if r.status_code != 200:
        raise RuntimeError(f"kalender HTTP {r.status_code}")
    return sorted(C.to_epoch(e["time"]) for e in r.json().get("events", [])
                  if str(e.get("impact", "")).lower() == "high")


def validate(cs):
    """Return daftar error (kosong = lolos). Gap hanya dicatat sebagai peringatan."""
    errs, prev, seen = [], None, set()
    for c in cs:
        vals = [c["o"], c["h"], c["l"], c["c"]]
        if any(v is None or (isinstance(v, float) and math.isnan(v)) for v in vals):
            errs.append("NaN")
            continue
        if c["t"] in seen:
            errs.append("duplikat timestamp")
        seen.add(c["t"])
        if prev is not None and c["t"] < prev:
            errs.append("urutan waktu mundur")
        prev = c["t"]
        if not (c["h"] >= c["l"] and c["l"] <= min(c["o"], c["c"]) and c["h"] >= max(c["o"], c["c"])):
            errs.append("OHLC tidak logis")
    return sorted(set(errs))


def fetch_all():
    """Semua candle dan kalender diambil paralel (satu gelombang request, bukan berurutan).
    Return (raw, h4, news, news_err, gagal). Kegagalan kalender tidak menghentikan siklus."""
    with ThreadPoolExecutor(max_workers=len(C.PAIRS) + 2) as ex:
        m15 = {p: ex.submit(fetch_candles, p, C.TF, C.M15_COUNT) for p in C.PAIRS}
        h4_f = ex.submit(fetch_candles, C.PEMICU, C.TF_H4, C.H4_COUNT)
        news_f = ex.submit(fetch_news)
        raw, gagal = {}, None
        for p, f in m15.items():
            try:
                raw[p] = f.result()
            except Exception as e:
                gagal = gagal or f"{C.disp(p)} M15: {e}"
        try:
            h4 = h4_f.result()
        except Exception as e:
            h4, gagal = None, gagal or f"{C.disp(C.PEMICU)} H4: {e}"
        try:
            news, news_err = news_f.result(), None
        except Exception as e:
            news, news_err = None, type(e).__name__
    return raw, h4, news, news_err, gagal


def check(raw, h4, gagal):
    """Validasi dan persiapan data. Return (prep | None, alasan_gagal | None)."""
    if gagal:
        return None, gagal
    for p in C.PAIRS:
        if validate(raw[p]):
            return None, f"validasi {C.disp(p)} M15 gagal"
    if validate(h4):
        return None, "validasi H4 gagal"
    prep = E.build(raw, h4)
    if not prep["sinkron"]:
        return None, "bar terakhir antar pair tidak sinkron dengan EUR/USD"
    return prep, None


def news_clean(news, now):
    """True = bersih, False = ada news ±30 menit, None = kalender gagal."""
    if news is None:
        return None
    return not any(abs(now.timestamp() - x) <= C.NEWS_MENIT * 60 for x in news)


# ---------------- sesi pasar ----------------

def market_open(now):
    """Forex: Senin 00:00 UTC sampai Jumat 22:00 UTC."""
    wd = now.weekday()
    return wd < 4 or (wd == 4 and now.hour < 22) or (wd == 6 and now.hour >= 22)


# ---------------- laporan dan Discord ----------------

def report_md(now, status, res, pem, news_bersih, news_err):
    lines = ["# Laporan Run Skema Final (EUR/USD pemantik + konfirmasi)", "",
             f"- Waktu: {C.fmt(now)}", f"- Status: {status}",
             f"- Kalender: {_kalender(news_bersih, news_err)}",
             "- Spread: tidak tersedia (filter spread dilewati)", ""]
    if res is None:
        return "\n".join(lines) + "\n"
    lines += ["## Keputusan", "",
              f"- Label: **{res['label']}** · decision: `{res['decision']}`",
              f"- Bar M15: {res['bar_terakhir']} · EUR/USD: {res['harga_pemicu']} · target: {res['target']}"]
    if res.get("entry") is not None:
        lv = res["levels"]
        lines += [f"- Entry / SL / TP: **{res['entry']} / {res['sl']} / {res['tp']}** "
                  f"(SL {lv['sl_pip']} pip, TP {lv['tp_pip']} pip, ATR {lv['atr_pip']} pip)",
                  f"- Risiko {C.RISIKO_PERSEN}% equity (lot tidak dihitung, tidak ada data equity)"]
    lines += [f"- Alasan: {'; '.join(res['alasan']) or '-'}", ""]
    t = res["trigger"]
    lines += ["## Trigger EUR/USD M15", "",
              f"- Arah: {t.get('arah')} · EMA{t.get('ema_len')} {t.get('ema')} (persentil ATR {t.get('persentil_atr')}) · stoch {t.get('stoch')} · "
              f"ATR {t.get('atr')} vs median {t.get('atr_median')}", ""]
    if res.get("skor"):
        s = res["skor"]
        lines += ["## Confirmation score", "",
                  f"- Skor {s['nilai']} · threshold BUY {s['threshold_buy']} / SELL {s['threshold_sell']} · "
                  f"riwayat {s['riwayat']} ({'aktif' if s['threshold_aktif'] else 'warm-up'}) · lulus {s['lulus']}", ""]
    if res.get("bobot"):
        b = res["bobot"]
        lines += ["## Bobot adaptif", "", f"- Rata-rata |corr_50| {b['rata_c50']} · korelasi runtuh {b['kolaps']}", "",
                  "| Pair | corr_50 | corr_200 | corr_500 | adapt | stabilitas | bobot |", "|---|---|---|---|---|---|---|"]
        lines += [f"| {k} | {v['c50']} | {v['c200']} | {v['c500']} | {v['adapt']} | {v['stab']} | {v['w']} |"
                  for k, v in b["pair"].items()]
        lines.append("")
    if res.get("regime"):
        lines += ["## Filter", "", "| Filter | Hasil | Detail |", "|---|---|---|"]
        lines += [f"| {c['nama']} | {'LULUS' if c['lulus'] else 'GAGAL'} | {c['detail']} |" for c in res["regime"]["cek"]]
        lines.append("")
    lines += ["## Pemantauan entry", ""]
    rows = (pem or {}).get("tampil", [])
    if rows:
        lines += ["| Pair | Arah | Entry | Harga sekarang | Hasil | Pip | Umur (menit) |", "|---|---|---|---|---|---|---|"]
        for r in rows:
            pip = "-" if r["pip"] is None else f"{r['pip']:+}"
            lines.append(f"| {r['pair']} | {r['arah']} | {r['entry']} | {r['harga_skrg']} | {r['hasil']} | "
                         f"{pip} | {r['umur_menit']} |")
    else:
        lines.append("Tidak ada catatan yang dipantau.")
    return "\n".join(lines) + "\n"


def _kalender(news_bersih, news_err):
    if news_bersih is None:
        return f"gagal diperiksa ({news_err}), entry ditahan"
    return "bersih" if news_bersih else "ADA news high-impact ±30 menit"


def notify(now, status, res):
    """Kirim ke Discord sesuai DISCORD_NOTIFY_MODE: signal (default) | always | off."""
    mode = os.environ.get("DISCORD_NOTIFY_MODE", "").strip().lower() or "signal"
    url = os.environ.get("DISCORD_WEBHOOK_URL", "").strip()
    if mode == "off" or not url:
        return "Discord: tidak dikirim"
    ada_sinyal = res is not None and res["trigger"]["arah"] != "-"   # ENTRY atau trigger yang ditahan
    if mode == "signal" and not (status.startswith("DATA INVALID") or ada_sinyal):
        return "Discord: tidak ada yang perlu dikirim (mode signal)"
    if res is None:
        color, judul = 0xE74C3C, "DATA INVALID"
    elif res["label"].startswith("ENTRY"):
        color, judul = 0x2ECC71, f"ENTRY {C.disp(C.TARGET)} {res['decision']}"
    elif res["trigger"]["arah"] != "-":
        color, judul = 0xF1C40F, f"Trigger {res['trigger']['arah']} ditahan"
    else:
        color, judul = 0x95A5A6, "Tidak ada sinyal"
    embed = {"title": judul[:250], "color": color, "description": status[:1000], "timestamp": C.fmt(now), "fields": []}
    if res and res["label"].startswith("ENTRY"):
        lv = res["levels"]
        embed["fields"].append({"name": "Entry / SL / TP", "value": f"{res['entry']} / {res['sl']} / {res['tp']}"})
        embed["fields"].append({"name": "SL / TP (pip)", "value": f"{lv['sl_pip']} / {lv['tp_pip']}", "inline": True})
        embed["fields"].append({"name": "Risiko", "value": f"{C.RISIKO_PERSEN}% equity", "inline": True})
    if res and res.get("alasan"):
        embed["fields"].append({"name": "Alasan", "value": "\n".join(f"• {a}" for a in res["alasan"])[:1000]})
    if not embed["fields"]:
        del embed["fields"]
    try:
        r = requests.post(url, json={"embeds": [embed]}, timeout=15)
        return f"Discord: HTTP {r.status_code}"
    except Exception as e:
        return f"Discord: gagal kirim ({type(e).__name__})"


# ---------------- siklus ----------------

def main():
    now = C.utc_now()
    status, res, pem, news_bersih, news_err = "PASAR TUTUP, tidak ada analisa", None, None, None, None
    if market_open(now):
        raw, h4, news, news_err, gagal = fetch_all()
        news_bersih = news_clean(news, now)
        pem = PT.perbarui_state(now, lambda p: (raw or {}).get(p))   # candle yang sudah diambil, tanpa unduh ulang
        prep, gagal = check(raw, h4, gagal)
        if prep is None:
            status = f"DATA INVALID: {gagal}"
        else:
            state = C.load_json(C.SKOR_PATH, {"skor": [], "bar_terakhir": None})
            riwayat = state["skor"]
            posisi = PT.aktif_saat_ini()
            posisi_pair = C.TARGET if any(s["pair"] == C.disp(C.TARGET) for s in posisi) else None
            res, skor = E.analyze(prep, len(prep["t"]) - 1, riwayat, news_bersih, posisi_pair, len(posisi))
            status = f"OK, bar {res['bar_terakhir']}: {res['label']}"
            if skor is not None and state["bar_terakhir"] != res["bar_terakhir"]:
                riwayat = (riwayat + [skor])[-C.SKOR_RIWAYAT_MAKS:]
                C.save_json(C.SKOR_PATH, {"skor": riwayat, "bar_terakhir": res["bar_terakhir"]})
            if res["label"].startswith("ENTRY"):
                PT.tambah(now, [{**res, "pair": C.disp(C.TARGET)}])
        C.append_jsonl(C.SIGNAL_LOG, [_baris_log(now, status, res)])

    os.makedirs(os.path.dirname(C.REPORT_MD), exist_ok=True)
    with open(C.REPORT_MD, "w", encoding="utf-8") as f:
        f.write(report_md(now, status, res, pem, news_bersih, news_err))
    C.save_json(C.REPORT_JSON, {"waktu": C.fmt(now), "status": status, "hasil": res, "pemantauan": pem})
    print(notify(now, status, res))
    print(f"Selesai: {status}")
    return 0 if res is not None or not market_open(now) else 1


def _baris_log(now, status, res):
    """§14C: satu baris per siklus untuk audit."""
    if res is None:
        return {"waktu": C.fmt(now), "status": status, "decision": "DATA_INVALID"}
    s = res.get("skor") or {}
    return {"waktu": C.fmt(now), "bar": res["bar_terakhir"], "trigger": res["trigger"]["arah"],
            "skor": s.get("nilai"), "threshold_buy": s.get("threshold_buy"), "threshold_sell": s.get("threshold_sell"),
            "regime_ok": (res.get("regime") or {}).get("lulus"), "target": res["target"],
            "decision": res["decision"], "reason": "; ".join(res["alasan"]),
            "entry": res["entry"], "tp": res["tp"], "sl": res["sl"]}


if __name__ == "__main__":
    sys.exit(main())
