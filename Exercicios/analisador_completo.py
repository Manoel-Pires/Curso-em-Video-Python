soma = 0
mais_velho = 0
nome_velho = ""
cont_mulher = 0
for p in range(1, 5):
    print(f"====== {p}ª PESSOA =====")
    nome = str(input("NOME: "))
    idade = int(input("IDADE: "))
    sexo = str(input("SEXO(M/F): ")).strip().upper()
    soma += idade
    if p == 1 and sexo == "M":
        mais_velho = idade
        nome_velho = nome
    elif p != 1 and sexo == "M":
        if idade > mais_velho:
            mais_velho = idade
            nome_velho = nome
    elif idade < 20 and sexo == "F":
        cont_mulher += 1
print("=" * 15)
media = soma / 4
print(f"A média de idade do grupo foi de {media} anos")
print(f"O homem mais velho tem {mais_velho} anos e se chama {nome_velho}")
print(f"Ao todo são {cont_mulher} mulheres com menos de 20 anos")