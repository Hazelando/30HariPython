def kalkulator(a, b, operasi):
    if operasi == 'tambah':
        return a + b
    elif operasi == 'kurang':
        return a - b
    elif operasi == 'kali':
        return a * b
    elif operasi == 'bagi':
        return a / b
    else:
        return 'Operasi tidak dikenali'

print(kalkulator(10, 5, 'kali'))