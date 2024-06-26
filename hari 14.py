def hitung_kata(kalimat):
    kata = kalimat.split()
    return len(kata)

kalimat = "Belajar Python itu menyenangkan"
print(f'Jumlah kata: {hitung_kata(kalimat)}')