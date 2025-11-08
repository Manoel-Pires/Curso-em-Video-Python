from datetime import date
hoje = date.today().year
nasc = int(input("Informe o seu ano de nascimento: "))
idade = hoje - nasc
print(f"Quem nasceu em {nasc} tem {idade} anos em {hoje}")
if idade < 18:
    ano = nasc + 18
    alista = ano - hoje
    print(f"Ainda faltam {alista} anos para o seu alistamento")
    print(f"Seu alistamento sera em {ano}")
    
elif idade > 18:
    ano = nasc + 18
    alista = hoje - ano
    print(f"Ja se passaram {alista} anos do seu alisramento")
    print(f"Voce deveria ter se alistado em {ano}")
    
else: 
    print(f"Aliste-se imediatamente!!")

    
            