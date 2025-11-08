from random import randint 
from time import sleep
palpite = []
print("=" * 30)
print(".    JOGO DA MEGA-SENA")
print("=" * 30)
quant = int(input("Quantos jogos você quer que eu soteie? "))
for c in range(1, quant + 1):
    while len(palpite) < 6:
        n = randint(1, 60)
        if n not in palpite:
            palpite.append(n)
        palpite.sort()      
    print(f"{c}° palpite: {palpite}")
    sleep(1)
    palpite.clear()
    

    
