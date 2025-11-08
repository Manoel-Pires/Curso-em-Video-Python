from time import sleep 
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
opção= 0
while opção != 5:
    print("""        [1] Somar
        [2] Multiplicar
        [3] Maior
        [4] Outros números 
        [5] Sair do programa""")
    opção = int(input(">>>>Qual a sua opção? "))
    print("=-" * 15)
    if opção == 1:
        soma = n1 + n2
        print (f"A soma entre {n1} e {n2} é igual a {soma}") 
    elif opção == 2:
        produto = n1 * n2 
        print(f"O produto entre {n1} e {n2} é {produto}")    
    elif opção == 3:
        maior = n1
        if n2 > maior:
            maior = n2 
            print(f"Entre {n1} e {n2} o maior é {maior}") 
    elif opção == 4:
        print("Informe os números novamente ")
        n1 = int(input("Digite o primeiro número: "))
        n2 = int(input("Digite o segundo número: "))
    elif opção == 5:
        print("SAINDO...")
    else:
        print("Opção inválida. Tentei novamente ")
    sleep(2)
print("Fim do programa.  Volte sempre.")






    