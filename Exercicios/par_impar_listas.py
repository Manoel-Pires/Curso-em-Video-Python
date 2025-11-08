listanum = listapar = listaimpar = []
while True:
    num = int(input("Digite um número: "))
    listanum.append(num)
    resposta = input("Deseja continuar?(S/N) ").strip().upper()[0]
    if resposta == "N":
        break
for v in listanum:
    if num % 2 ==0:
        listapar.append(v)
    else:
        listaimpar.append(v)
print(f"Os números digitados foram {listanum}")
print(f"Os números pares foram {listapar}")
print(f"Os números ímpares foram {listaimpar}")

    