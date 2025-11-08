print("GERADOR DE PA")
print("=-" * 10)
termo = int(input("Primeiro termo: "))
razão = int(input ("Qual a razão? "))
cont = 10
print(f"{termo} -> ", end="")
while cont > 0:
    termo += razão 
    print(f"{termo}", end=" ")
    cont -= 1
    print("-> ", end ="")
print("FIM")
    