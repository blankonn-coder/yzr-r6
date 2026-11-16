"""Pemantauan pair aktif maksimal 60 menit (tanpa cooldown)."""
from . import config as C


def umur(m, now):
    """Umur pemantauan dalam menit (desimal)."""
    return (now - C.parse(m["waktu_mulai"])).total_seconds() / 60


def aktif(state, now):
    """Hanya pair yang umurnya masih di bawah batas pemantauan."""
    return {k: v for k, v in state.items() if umur(v, now) < C.MONITOR_MINUTES}


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
        if e["pair"] not in state:
            state[e["pair"]] = {"pair": e["pair"], "keputusan": e["keputusan"],
                                "harga_awal": e["harga"], "waktu_mulai": C.fmt(now),
                                "signal_id": e["id"], "harga_sekarang": e["harga"]}
    for pair, price in prices.items():
        if pair in state:
            state[pair]["harga_sekarang"] = price
    return state, expired
