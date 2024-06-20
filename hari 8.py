import random

angka_rahasia = random.randint(1, 100)
tebakan = None
upaya = 0

while tebakan != angka_rahasia:
    tebakan = int(input("Tebak angka (1-100): "))
    upaya += 1
    if tebakan < angka_rahasia:
        print("Tebakan terlalu rendah, coba lagi!")
    elif tebakan > angka_rahasia:
        print("Tebakan terlalu tinggi, coba lagi!")

print(f"Selamat! Anda berhasil menebak angka {angka_rahasia} dengan {upaya} upaya.")