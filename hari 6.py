import random
import string

def generate_password(panjang):
    karakter = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(karakter) for _ in range(panjang))
    return password

panjang_password = int(input("Masukkan panjang kata sandi: "))
print("Kata sandi yang dihasilkan:", generate_password(panjang_password))
