def frekuensi_karakter(teks):
    frekuensi = {}
    for char in teks:
        if char in frekuensi:
            frekuensi[char] += 1
        else:
            frekuensi[char] = 1
    return frekuensi

print(frekuensi_karakter("hello world"))
