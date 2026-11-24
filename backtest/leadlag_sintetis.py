"""Data sintetis untuk menguji lead-lag. Hubungan yang ditanam sudah diketahui, sehingga hasilnya bisa dicek.

Python -m backtest.leadlag_sintetis   (dari folder proyek) mencetak hasil uji ke layar.
Tidak menulis ke database/ atau state/.
"""
import math
import random

import config as C
import leadlag as LL

# (leader, follower, lag dalam bar M5, beta). Follower = beta x return leader (lag) + noise.
DITANAM = [
    ("GBP_JPY", "NZD_JPY", 3, 0.8),   # lag 15 menit
    ("GBP_CHF", "CHF_JPY", 8, 0.8),   # lag 40 menit
]


def buat_sintetis(n_bar=400, seed=1, sigma=0.001, ditanam=DITANAM):
    """Return {pair_key: [[t, c], ...]} dengan format sama seperti store lead-lag."""
    rng = random.Random(seed)
    keys = C.LEADLAG_PAIRS
    noise = {k: [rng.gauss(0.0, sigma) for _ in range(n_bar)] for k in keys}
    ret = {k: list(noise[k]) for k in keys}
    for leader, follower, lag, beta in ditanam:
        for t in range(lag, n_bar):
            ret[follower][t] = beta * noise[leader][t - lag] + math.sqrt(1 - beta * beta) * noise[follower][t]
    akhir = 1_790_000_000 // C.TF_LEADLAG_SEC * C.TF_LEADLAG_SEC
    awal = akhir - (n_bar - 1) * C.TF_LEADLAG_SEC
    out = {}
    for k in keys:
        c, cs = 100.0, []
        for i in range(n_bar):
            c *= 1.0 + ret[k][i]
            cs.append([awal + i * C.TF_LEADLAG_SEC, c])
        out[k] = cs
    return out


def uji():
    candles = buat_sintetis()
    end = max(cs[-1][0] for cs in candles.values())
    pasangan, _, _, _ = LL.hitung_backtest(candles, end)
    print(f"Pasangan lolos: {len(pasangan)}")
    for p in pasangan[:10]:
        print(f"  {p['leader']} -> {p['follower']}  lag {p['lag_menit']} mnt  r {p['korelasi']}  "
              f"r0 {p['korelasi_lag0']}  n {p['n']}")
    print("Yang ditanam:")
    for lead, fol, lag, beta in DITANAM:
        ditemukan = [p for p in pasangan if p["leader"] == C.disp(lead) and p["follower"] == C.disp(fol)]
        print(f"  {C.disp(lead)} -> {C.disp(fol)} lag {lag * 5} mnt, beta {beta}: "
              f"{'TERDETEKSI ' + str(ditemukan[0]['lag_menit']) + ' mnt r ' + str(ditemukan[0]['korelasi']) if ditemukan else 'TIDAK TERDETEKSI'}")


if __name__ == "__main__":
    uji()
