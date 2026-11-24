"""Pemantauan pair aktif maksimal MONITOR_MINUTES + cooldown screening COOLDOWN_MINUTES.

Aturan: setelah sebuah pair muncul sebagai BUY/SELL, selama COOLDOWN_MINUTES sejak sinyal
pertama pair itu TIDAK boleh muncul lagi di hasil screening dengan arah yang sama
(hanya tetap dipantau). Arah berlawanan boleh masuk screening sebagai sinyal baru."""
import config as C


def umur(m, now):
    """Umur pemantauan dalam menit (desimal)."""
    return (now - C.parse(m["waktu_mulai"])).total_seconds() / 60


def aktif(state, now):
    """Hanya pair yang umurnya masih di bawah batas pemantauan."""
    return {k: v for k, v in state.items() if umur(v, now) < C.MONITOR_MINUTES}


def saring_cooldown(cooldown, mon, rows, now):
    """Pisahkan sinyal baru dari sinyal searah yang masih dalam cooldown.

    cooldown: {pair: {keputusan, waktu_mulai, signal_id}}; mon: state pemantauan;
    rows: hasil evaluasi (dict dengan pair & keputusan). Baris yang ditahan diubah
    keputusannya menjadi "DITAHAN" sehingga tidak tampil di laporan/Discord/database.
    Return (cooldown, jumlah_ditahan)."""
    batas = C.COOLDOWN_MINUTES + C.LATE_MINUTES  # toleransi run yang terlambat
    cooldown = {k: v for k, v in cooldown.items() if umur(v, now) <= batas}
    # Pair yang sedang dipantau tapi belum tercatat (state lama) ikut dilindungi
    for pair, m in aktif(mon, now).items():
        cooldown.setdefault(pair, {"keputusan": m["keputusan"], "waktu_mulai": m["waktu_mulai"],
                                   "signal_id": m["signal_id"]})
    ditahan = 0
    for r in rows:
        cd = cooldown.get(r["pair"])
        if r["keputusan"] in ("BUY", "SELL") and cd and cd["keputusan"] == r["keputusan"]:
            r["keputusan"] = "DITAHAN"
            ditahan += 1
    return cooldown, ditahan


def catat_cooldown(cooldown, new_entries, now):
    """Sinyal baru (pair belum di-cooldown, cooldown habis, atau arah berlawanan) memulai cooldown baru."""
    for e in new_entries:
        cooldown[e["pair"]] = {"keputusan": e["keputusan"], "waktu_mulai": C.fmt(now),
                               "signal_id": e["id"]}
    return cooldown


def teks_gerak(pip, pct):
    """Hasil dalam bentuk PROFIT/RUGI. Pergerakan sudah dibalik tandanya untuk SELL."""
    if round(pip, 1) == 0:
        return "0.0 pip · 0.000%"
    kata = "PROFIT" if pip > 0 else "RUGI"
    return f"{kata} {abs(pip):.1f} pip · {abs(pct):.3f}%"


def update(state, new_entries, prices, now):
    """state: {pair: {...}}; new_entries: [{pair, id, harga, keputusan}];
    prices: {pair: harga sekarang}. Return (state, daftar_id_signal_yang_expired)."""
    expired = []
    for pair in list(state):
        if umur(state[pair], now) >= C.MONITOR_MINUTES:
            expired.append(state[pair]["signal_id"])
            del state[pair]
    for e in new_entries:
        lama = state.get(e["pair"])
        if lama and lama["keputusan"] != e["keputusan"]:
            # Arah berlawanan: sinyal lama ditutup, pemantauan dimulai ulang untuk sinyal baru
            expired.append(lama["signal_id"])
            del state[e["pair"]]
        if e["pair"] not in state:
            state[e["pair"]] = {"pair": e["pair"], "keputusan": e["keputusan"],
                                "harga_awal": e["harga"], "waktu_mulai": C.fmt(now),
                                "signal_id": e["id"], "harga_sekarang": e["harga"]}
    for pair, price in prices.items():
        if pair in state:
            state[pair]["harga_sekarang"] = price
    return state, expired
