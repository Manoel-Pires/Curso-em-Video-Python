maior_18 = menor_20 = tot_homens = 0
while True:
    print ("=" * 25)
    print("CADASTRAR UMA PESSOA")
    print ("=" * 25)
    idade = int(input("IDADE: "))
    sexo = " "
    while sexo not in "MF":
        sexo = str(input("SEXO [M/F]")).strip().upper()[:1]
    if idade > 18:
        maior_18  += 1
    if sexo == "M":
        tot_homens  += 1
    if sexo == "F" and idade < 20:
        menor_20  += 1
    opção= " "
    while opção not in "SN":
        opção = str(input ("Deseja continuar? [S/N]] ")).strip().upper()[:1]
    if opção == "N":
        break
print(f"Total de pessoas com mais de 18 anos: {maior_18}")
print(f"Ao todo temos {tot_homens} homem(s) cadastrados")
print(f"E temos {menor_20} mulher(s) com menos de 20 anos")


