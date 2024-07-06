def hitung_vokal(teks):
    vokal = 'aeiouAEIOU'
    return sum(1 for char in teks if char in vokal)

print(hitung_vokal("Belajar Python itu menyenangkan"))