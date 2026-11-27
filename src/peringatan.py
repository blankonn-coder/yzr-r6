"""Bot peringatan 1 jam. TIDAK membuka entry otomatis.
Membaca CSV 1 jam (time,open,high,low,close), lalu menulis laporan kondisi terkini per pair.
Aturan (belum tervalidasi di luar sampel, hanya untuk dianalisa manual):
- Menyentuh support kemarin: tren kuat -> SELL, tren lemah -> BUY
- Menyentuh resisten kemarin: tren kuat -> BUY, tren lemah -> SELL
- Label OS/OB: searah / berlawanan / netral (berlawanan tetap ditampilkan, tidak dilarang)
- SL di sisi level kemarin (10-30 pip). TP baseline 10 pip, dan TP ke level berlawanan sebagai info.
"""
import sys, os, numpy as np, pandas as pd
import requests

PIP_TOUCH = 3              # jarak menyentuh level (pip)
TP_BASE, SL_MIN, SL_MAX = 10, 10, 30
ER_WIN, ER_Q = 20, 0.6     # efficiency ratio 20 bar, persentil 60 terhadap 1440 bar
ER_HIST = 1440
OS_Q, OB_Q, OSC_HIST = 0.2, 0.8, 500
PAIRS = ["AUDUSD","EURAUD","EURCAD","EURGBP","EURJPY","EURNZD","EURUSD",
         "GBPUSD","NZDUSD","USDCAD","USDCHF","USDJPY"]

def muat(folder, pair):
    f = os.path.join(folder, f"{pair}_1h.csv")
    if not os.path.exists(f):
        return None
    h = pd.read_csv(f, parse_dates=["time"], index_col="time").sort_index()
    h = h[~h.index.duplicated()].dropna()
    h["date"] = h.index.floor("D")
    return h

def analisa(pair, h):
    pip = 0.01 if "JPY" in pair else 0.0001
    g = h.groupby("date")
    dd = pd.DataFrame({"hi": g.high.max(), "lo": g.low.min(), "n": g.size()})
    dd["hi_k"], dd["lo_k"] = dd.hi.shift(1), dd.lo.shift(1)     # level = hari sebelumnya (termasuk hari ini yang masih berjalan)
    dd.loc[dd.n < 20, ["hi_k","lo_k"]] = dd.loc[dd.n < 20, ["hi_k","lo_k"]]
    h = h.join(dd[["hi_k","lo_k"]], on="date")
    last = h.iloc[-1]
    hi_k, lo_k = last.hi_k, last.lo_k
    if np.isnan(hi_k) or np.isnan(lo_k):
        return None
    er = (h.close - h.close.shift(ER_WIN)).abs() / h.close.diff().abs().rolling(ER_WIN).sum()
    strong = er.iloc[-1] > er.shift(1).rolling(ER_HIST, min_periods=300).quantile(ER_Q).iloc[-1]
    ll, hh = h.low.rolling(14).min(), h.high.rolling(14).max()
    k = ((h.close-ll)/(hh-ll)*100).rolling(3).mean()
    os_ = k.iloc[-1] < k.shift(1).rolling(OSC_HIST, min_periods=100).quantile(OS_Q).iloc[-1]
    ob_ = k.iloc[-1] > k.shift(1).rolling(OSC_HIST, min_periods=100).quantile(OB_Q).iloc[-1]
    t = PIP_TOUCH * pip
    sup = (last.low <= lo_k+t) and (last.high >= lo_k-t)
    res = (last.high >= hi_k-t) and (last.low <= hi_k+t)
    if sup == res:                       # tidak menyentuh, atau keduanya (kisaran terlalu sempit)
        return dict(pair=pair, status="tidak ada sentuhan" if not sup else "menyentuh kedua level", waktu=h.index[-1])
    tipe = "support" if sup else "resisten"
    tren = "kuat" if strong else "lemah"
    if sup:
        arah = "SELL" if strong else "BUY"
    else:
        arah = "BUY" if strong else "SELL"
    sl_pip = float(np.clip(((last.close-lo_k) if arah=="BUY" else (hi_k-last.close))/pip, SL_MIN, SL_MAX))
    tp_lawan = float(np.clip((hi_k-last.close)/pip if arah=="BUY" else (last.close-lo_k)/pip, 10, 60))
    if (arah=="BUY" and ob_) or (arah=="SELL" and os_):
        label = "BERLAWANAN OS/OB (peringatan)"
    elif (arah=="BUY" and os_) or (arah=="SELL" and ob_):
        label = "searah OS/OB"
    else:
        label = "netral"
    return dict(pair=pair, status="SENTUH", waktu=h.index[-1], harga=round(last.close,5),
                tipe=tipe, tren=tren, arah=arah, label=label,
                sl_pip=round(sl_pip,1), tp_base=TP_BASE, tp_lawan=round(tp_lawan,1),
                sl_level=round(lo_k if arah=="BUY" else hi_k,5), lvl=round(lo_k if sup else hi_k,5))

def tulis(hasil, out):
    os.makedirs(os.path.dirname(out) or ".", exist_ok=True)
    L = ["# Peringatan 1 jam (belum tervalidasi, bukan sinyal entry)", ""]
    sent = [r for r in hasil if r.get("status")=="SENTUH"]
    if not sent:
        L.append("Tidak ada pair yang menyentuh level kemarin pada jam terakhir.")
    else:
        L += ["| Pair | Waktu (UTC) | Harga | Level | Tipe | Tren | Arah | Label | SL (pip) | TP baseline | TP ke level lawan |",
              "|---|---|---|---|---|---|---|---|---|---|---|"]
        for r in sent:
            L.append(f"| {r['pair']} | {r['waktu']} | {r['harga']} | {r['lvl']} | {r['tipe']} | {r['tren']} | {r['arah']} | {r['label']} | {r['sl_pip']} | {r['tp_base']} | {r['tp_lawan']} |")
    L += ["", "Pair lain tidak menyentuh level kemarin:"]
    for r in hasil:
        if r.get("status")!="SENTUH":
            L.append(f"- {r['pair']}: {r.get('status','data tidak cukup')}")
    open(out,"w",encoding="utf-8").write("\n".join(L)+"\n")
    return "\n".join(L)

def kirim_discord(hasil):
    """Kirim peringatan ke Discord hanya jika ada pair yang menyentuh level. Tanpa DISCORD_WEBHOOK_URL: dilewati."""
    url = os.environ.get("DISCORD_WEBHOOK_URL", "").strip()
    sent = [r for r in hasil if r.get("status") == "SENTUH"]
    if not url:
        return "Discord: tidak dikirim (DISCORD_WEBHOOK_URL kosong)"
    if not sent:
        return "Discord: tidak ada sentuhan, tidak dikirim"
    baris = [f"PERINGATAN 1 jam (belum tervalidasi, bukan sinyal entry)"]
    for r in sent:
        baris.append(f"{r['pair']} | {r['tipe']} {r['lvl']} | tren {r['tren']} | {r['arah']} | {r['label']} | SL {r['sl_pip']} pip | TP {r['tp_base']} pip | TP lawan {r['tp_lawan']} pip")
    isi = "```\n" + "\n".join(baris)[:1900] + "\n```"
    try:
        r = requests.post(url, json={"content": isi}, timeout=15)
        return f"Discord: HTTP {r.status_code}"
    except requests.RequestException as e:
        return f"Discord: gagal kirim ({type(e).__name__})"

if __name__ == "__main__":
    folder = sys.argv[1] if len(sys.argv)>1 else "data/1h"
    out = sys.argv[2] if len(sys.argv)>2 else "reports/peringatan_terbaru.md"
    hasil=[]
    for p in PAIRS:
        h = muat(folder, p)
        if h is None:
            hasil.append(dict(pair=p, status="file tidak ada")); continue
        r = analisa(p, h)
        hasil.append(r or dict(pair=p, status="data tidak cukup"))
    print(tulis(hasil, out))
    print(kirim_discord(hasil))
