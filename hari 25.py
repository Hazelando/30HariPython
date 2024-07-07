def hitung_faktor(n):
    faktor = [i for i in range(1, n+1) if n % i == 0]
    return faktor

print(hitung_faktor(28))
