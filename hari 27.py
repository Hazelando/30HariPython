import random

def acak_list(lst):
    random.shuffle(lst)
    return lst

angka = [1, 2, 3, 4, 5]
print(acak_list(angka))