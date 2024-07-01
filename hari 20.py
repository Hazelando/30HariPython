from datetime import datetime

def hitung_hari(tanggal1, tanggal2):
    format_tanggal = "%Y-%m-%d"
    t1 = datetime.strptime(tanggal1, format_tanggal)
    t2 = datetime.strptime(tanggal2, format_tanggal)
    return (t2 - t1).days

print(hitung_hari('2023-01-01', '2024-01-01'))