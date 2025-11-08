pessoas = []
geral = []
maior = menor = 0
while True:
    pessoas.append(str(input("Nome: ")))
    pessoas.append(float(input("Peso: ")))
    resposta = input("Deseja continuar?(S/N) ").strip(). upper()[0] 
    if len(geral) == 0:
        maior = menor = pessoas[1]
    else:
        if pessoas[1] > maior:
            maior = pessoas[1]
        if pessoas[1] < menor:
            menor= pessoas[1]
    geral.append(pessoas[:])
    pessoas.clear()
    if resposta == "N":
        break
print(f"Você cadastrou {len(geral)} pessoas")
print(f"O maior peso foi {maior}. Da (s) pessoa(s) ", end="")
for p in geral:
    if p[1] == maior:
        print(f"{p[0]}... ", end="") 
print()
print(f"O menor peso foi {menor}. ")
for p in geral:
    if  p[1] == menor:
        print(f"{p[0]}...", end="")
    