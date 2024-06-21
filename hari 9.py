def kelompokkan_kata(daftar_kata):
    kelompok = {}
    for kata in daftar_kata:
        panjang = len(kata)
        if panjang not in kelompok:
            kelompok[panjang] = [kata]
        else:
            kelompok[panjang].append(kata)
    return kelompok

daftar_kata = input("Masukkan daftar kata, pisahkan dengan koma: ").split(',')
hasil_kelompok = kelompokkan_kata(daftar_kata)
for panjang, kata in hasil_kelompok.items():
    print(f"Kata dengan panjang {panjang}: {', '.join(kata)}")