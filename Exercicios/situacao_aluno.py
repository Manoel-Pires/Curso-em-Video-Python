aluno = {}
aluno["Nome"] = str(input("Nome: "))
aluno["Média"] = float(input(f"Qual a média de {aluno['Nome']}? "))
if aluno["Média"] < 5:
    aluno["Situação"] = 'Reprovado'
elif aluno["Média"] >= 7:
    aluno["Situação"] = "Aprovado"
else:
    aluno["Situação"] = "Recuperação"
print("=" * 30)
for k,v in aluno.items():
    print(f"{k} = {v}")
