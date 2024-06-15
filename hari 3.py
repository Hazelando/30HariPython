def konversi_mata_uang(jumlah, kurs):
    return jumlah * kurs

jumlah = float(input("Masukkan jumlah uang: "))
kurs = float(input("Masukkan kurs mata uang: "))

hasil_konversi = konversi_mata_uang(jumlah, kurs)
print("Hasil konversi:", hasil_konversi)