"""Laporan run singkat: sinyal BUY/SELL dan pemantauan aktif (NETRAL tidak ditampilkan)."""
from . import config as C
from .monitor import aktif, umur, teks_gerak


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

    L.append("## Pemantauan (maks 60 menit)")
    pantau = aktif(mon, now)
    if pantau:
        L += ["| Pair | Arah | Harga Awal | Harga Sekarang | Hasil | Umur (menit) |",
              "|---|---|---|---|---|---|"]
        for m in pantau.values():
            awal, kini = m["harga_awal"], m["harga_sekarang"]
            pip, pct = C.gerak(m["pair"], awal, kini, m.get("keputusan", ""))
            L.append(f"| {m['pair']} | {m.get('keputusan', '-')} | {awal} | {kini} "
                     f"| {teks_gerak(pip, pct)} | {int(umur(m, now))} |")
    else:
        L.append("Tidak ada pair aktif.")
    L.append("")

    if info_db:
        L += ["## Info Database",
              f"- Total entri: {info_db['total']}",
              f"- Ditambahkan run ini: {info_db['tambah']}",
              f"- Dihapus karena retensi: {info_db['hapus']}",
              f"- File untuk diunduh: {C.DB_PATH}", ""]
    return "\n".join(L) + "\n"
