def kalkulator_kredit(pokok_pinjaman, suku_bunga, jangka_waktu):
    suku_bunga_bulanan = suku_bunga / 100 / 12
    jumlah_pembayaran = jangka_waktu * 12
    pembayaran_bulanan = (pokok_pinjaman * suku_bunga_bulanan) / (1 - (1 + suku_bunga_bulanan) ** -jumlah_pembayaran)
    total_pembayaran = pembayaran_bulanan * jumlah_pembayaran
    return pembayaran_bulanan, total_pembayaran

pokok_pinjaman = float(input("Masukkan pokok pinjaman: "))
suku_bunga = float(input("Masukkan suku bunga per tahun (%): "))
jangka_waktu = int(input("Masukkan jangka waktu pinjaman (tahun): "))

pembayaran_bulanan, total_pembayaran = kalkulator_kredit(pokok_pinjaman, suku_bunga, jangka_waktu)
print("Pembayaran bulanan:", round(pembayaran_bulanan, 2))
print("Total pembayaran:", round(total_pembayaran, 2))