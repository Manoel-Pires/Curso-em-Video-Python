valores = []
for c in range(0,5):
    valores.append(int(input(f"Digite um valor para a posição {c}: ")))
print(f"Você digitou os valores {valores}")
maior = max(valores)
menor = min(valores)
print(f"O maior valor foi {maior} na(s) posição ", end="")
for c,v in enumerate (valores):
    if v == maior:
        print(f"{c} ...", end="")
print(f"\nO menor valor digitado foi {menor} na(s) posição ", end="")
for c,v in enumerate (valores):
    if v == menor:
        print(f"{c}...", end="")
