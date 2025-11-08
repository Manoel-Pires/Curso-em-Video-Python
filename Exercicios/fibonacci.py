print("-" * 25)
print("SEQUÊNCIA DE FIBONACCI ")
print("-" * 25)
termos = int(input("Quantos termos vc quer mostrar? "))
cont = 2
n1 = 0
n2 = 1
print(f"{n1} -> {n2} ", end="")
while cont < termos:
    soma = n1 + n2 
    print(f"-> {soma}",end="" )
    n1 = n2 
    n2 = soma
    cont += 1
print(" ->  FIM")

