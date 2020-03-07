aluno = dict()
aluno['nome'] = str(input("digite seu nome: "))
aluno['media'] = float(input(f"digite a média do {aluno['nome']}: "))
if aluno['media'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['media'] <7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'

for i, j in aluno.items():
    print(f'{i} = {j}')