"""Pemantauan pair aktif maksimal 60 menit (tanpa cooldown)."""
from . import config as C


def update(state, new_entries, prices, now):
    """state: {pair: {...}}; new_entries: [{pair, id, harga, keputusan}];
    prices: {pair: harga sekarang}. Return (state, daftar_id_signal_yang_expired)."""
    expired = []
    for pair in list(state):
        umur = (now - C.parse(state[pair]["waktu_mulai"])).total_seconds() / 60
        if umur >= C.MONITOR_MINUTES:
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
