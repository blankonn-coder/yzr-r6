"""Laporan run singkat (tanpa ringkasan 7 hari)."""
from . import config as C


def build_report(now, status, calib, rows, gagal, mon, info_db):
    L = ["# Laporan Run Screening Forex", "",
         f"- Waktu eksekusi: {C.fmt(now)}",
         f"- Status: {status}",
         f"- Kalibrasi: {calib}",
         f"- Pair dianalisa: {len(rows)}"]
    if gagal:
        L.append(f"- Gagal ambil data: {'; '.join(gagal)}")
    L.append("")

    for judul, kep in (("Sinyal BUY", "BUY"), ("Sinyal SELL", "SELL")):
        L.append(f"## {judul}")
        sel = [r for r in rows if r["keputusan"] == kep]
        if sel:
            L += ["| Pair | Keputusan | Skor | Alasan |", "|---|---|---|---|"]
            L += [f"| {r['pair']} | {r['keputusan']} | {r['skor_akhir']} | {'; '.join(r['alasan'])} |"
                  for r in sel]
        else:
            L.append("Tidak ada.")
        L.append("")

    L.append("## Pemantauan (maks 1 jam)")
    if mon:
        L += ["| Pair | Harga Awal | Harga Sekarang | Selisih % | Umur (menit) |",
              "|---|---|---|---|---|"]
        for m in mon.values():
            awal, kini = m["harga_awal"], m["harga_sekarang"]
            pct = (kini - awal) / awal * 100
            umur = (now - C.parse(m["waktu_mulai"])).total_seconds() / 60
            L.append(f"| {m['pair']} | {awal} | {kini} | {pct:+.3f} | {umur:.0f} |")
    else:
        L.append("Tidak ada pair aktif.")
    L.append("")

    netral = [r["pair"] for r in rows if r["keputusan"] == "NETRAL"]
    L += ["## Pair NETRAL", ", ".join(netral) or "-", ""]

    if info_db:
        L += ["## Info Database",
              f"- Total entri: {info_db['total']}",
              f"- Ditambahkan run ini: {info_db['tambah']}",
              f"- Dihapus karena retensi: {info_db['hapus']}",
              f"- File untuk diunduh: {C.DB_PATH}", ""]
    return "\n".join(L) + "\n"
