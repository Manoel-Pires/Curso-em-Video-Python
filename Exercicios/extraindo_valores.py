cont = 0
lista = []
while True:
    n = int(input("Digite um valor: "))
    lista.append(n)
    cont += 1
    resposta = input ("Deseja continuar?[S/N] ").strip(). upper()[0]
    if resposta == "N":
        break
lista.sort(reverse=True)
print(f"Você digitou {cont} valores")
print(f"Os valores em ordem decrescente são {lista}")
if 5 in lista:
    print("O número 5 está presente na lista ")
else:
    print("O número 5 não está presente na lista ")
    
