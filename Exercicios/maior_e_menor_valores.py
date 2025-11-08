resposta = ""
soma = cont = média = 0
while resposta in "Ss":
    num = int(input('Digite um num:'))
    cont += 1
    soma += num
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resposta = str(input("Quer continuar? [S/N] ")).strip()[0].upper()
média = soma / cont 
print(f"Você digitou {cont} números e a média foi {média}")
print(f"O maior  número foi {maior} e o menor foi {menor}")
