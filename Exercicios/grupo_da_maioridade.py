from datetime import date
hoje = date.today().year
cont_maior= 0
cont_menor =0
for c in range(1, 8):
    nascimento = int(input(f"Em que ano a {c} ª pessoa nasceu? "))
    idade = hoje - nascimento 
    if idade > 18:
        cont_maior += 1
    else:
        cont_menor += 1
print(f"Ao todo tivemos {cont_maior} pessoas maiores de idade")
print(f"E também tivemos {cont_menor} pessoas menores de idade")

        


