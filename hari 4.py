pengeluaran = []

while True:
    pilihan = input("Tambah pengeluaran (y/n)? ")
    if pilihan.lower() == 'y':
        nominal = float(input("Masukkan nominal pengeluaran: "))
        pengeluaran.append(nominal)
    elif pilihan.lower() == 'n':
        total_pengeluaran = sum(pengeluaran)
        print("Total pengeluaran bulan ini:", total_pengeluaran)
        break
    else:
        print("Pilihan tidak valid.")