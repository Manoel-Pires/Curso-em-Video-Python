opção = ""
num = []
valor =0
while True:
    valor = int(input("Digite um valor: "))
    if valor not in num:
        num.append(valor)
        print ("Valor adicionado com sucesso!!")
    else:
        print("Valor já existente. Não foi adicionado ")
    opção = str(input("Deseja continuar?[S/N) ")).strip().upper()[0]
    if opção== "N":
        break
num.sort()
print(f"Você digitou os valores: {num}")
    