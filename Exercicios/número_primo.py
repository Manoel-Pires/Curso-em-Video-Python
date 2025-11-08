total = 0
num = int(input("Digite um número: "))
for c in range(1, num + 1):
    print (c, end=" ")
    if num % c == 0:
        total += 1
print(f"O número {num} foi divisível {total} vezes")
if total > 2:
    print(" Por isso ele NÃO É PRIMO")
else:
    print("Por isso ele é primo")
    