daftar_belanja = []
while True:
    barang = input("Masukkan barang (atau 'selesai' untuk keluar): ")
    if barang.lower() == 'selesai':
        break
    daftar_belanja.append(barang)
print("Daftar belanja:")
for b in daftar_belanja:
    print(f"- {b}")