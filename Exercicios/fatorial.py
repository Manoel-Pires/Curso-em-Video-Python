num = int(input("Digite um número para calcular o seu fatorial: "))
print(f"Calculando {num}! = {num} x", end=" ")
cont = num
while cont > 0:
    fatorial = num
    cálculo = num * (cont - 1)
    parcial = cálculo 
    num = parcial
    cont -= 1
    if cont > 1:
        print(f"{cont} x ", end="")
    if cont == 1:
        print(f"{cont } =", end="")
print(f" {fatorial}")




    

    