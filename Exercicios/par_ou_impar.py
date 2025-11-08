from random import randint
print("=" * 25)
print("VAMOS JOGAR PAR OU ÍMPAR ")
print("=" * 25)
valor_computador = randint(1,10)
perdeu = False
cont = 0
while True:
    valor = int(input("Digite um valor: "))
    par_impar= str(input("Par ou ímpar [P/I]")).strip().upper()[:1]
    print("-" * 25)
    soma = valor + valor_computador 
    if soma % 2 == 0 and par_impar == "P":
            perdeu = False
            cont += 1
            print(f"Você jogou {valor} e o computador {valor_computador}. Total de {valor + valor_computador}. Deu par.\nVOCE VENCEU\nVamos jogar Novamente")
            print("_" * 40)
    elif soma % 2 != 0 and par_impar == "I" :
            perdeu = False 
            cont += 1
            print(f"Você jogou {valor} e o computador {valor_computador}. Total de {valor + valor_computador}. Deu impar.\nVOCE VENCEU\nVamos jogar Novamente")
    else:
            perdeu = True
    if perdeu == True:
            break 
print("Você PERDEU")
print(f" Gama Over. Você venceu {cont} vez(es)")
print("=" * 25)


            
            
    
            
    