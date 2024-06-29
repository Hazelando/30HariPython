import random

def acak_kata(kata):
    kata = list(kata)
    random.shuffle(kata)
    return ''.join(kata)

print(acak_kata("python"))