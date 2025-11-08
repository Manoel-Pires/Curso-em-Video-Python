while True:
    num = int(input("Quer ver a tabuada de qual número? "))
    if num < 0:
        break
    print("-" * 35)
    for c in range(1,11):
        print(f"{c:2}  x  {num}  =  {c * num}")    
print("PROGRAMA DE TABUADA ENCERRADO. VOLTE SEMPRE.")


 
    