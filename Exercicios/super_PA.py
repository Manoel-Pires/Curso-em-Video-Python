print("GERADOR DE PA")
print("=-" * 10)
termo = int(input("Primeiro termo: "))
razão = int(input ("Qual a razão? "))
cont = 0
total = 0
mais = 10
print(f"{termo} -> ", end="")
while mais != 0:
    total +=  mais
    while cont < total:
        termo += razão 
        print(f"{termo}", end=" ")
        cont += 1
        print("-> ", end ="")
    print("Pausa")
    mais = int(input ("Quantos números vc quer mostrar a mais? "))
print("FIM ")
print(f"A progressão foi finalizada com {total} termos mostrados")

        