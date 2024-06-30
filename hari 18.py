kamus = {
    'apple': 'apel',
    'banana': 'pisang',
    'bread': 'roti',
    'milk': 'susu'
}

def terjemahkan(kata):
    return kamus.get(kata.lower(), 'Kata tidak ditemukan')

print(terjemahkan('banana'))