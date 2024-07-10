def cek_palindrom(teks):
    teks_bersih = ''.join(filter(str.isalnum, teks)).lower()
    return teks_bersih == teks_bersih[::-1]

print(cek_palindrom("A man, a plan, a canal, Panama"))
print(cek_palindrom("Python"))
