def hitung_kalori(makanan):
    kalori = {
        'apel': 52,
        'pisang': 89,
        'roti': 265,
        'susu': 42
    }
    total_kalori = sum(kalori.get(m, 0) for m in makanan)
    return total_kalori

makanan = ['apel', 'pisang', 'roti']
print(f'Total kalori: {hitung_kalori(makanan)}')