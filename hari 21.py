from datetime import datetime

def hari_dalam_seminggu(tanggal):
    format_tanggal = "%Y-%m-%d"
    t = datetime.strptime(tanggal, format_tanggal)
    return t.strftime("%A")

print(hari_dalam_seminggu('2024-06-3'))