mulher = list()
geral = list()
acimaMedia = list()
mediaIdade = 0
idade = 0
numeroPessoa = 0
while True:

    pessoa = dict()
    pessoa['nome'] = str(input("Digite o nome da pessoa: "))
    numeroPessoa += 1

    pessoa['sexo'] = str(input("Digite o sexo (M ou F): "))

    pessoa['idade'] = int(input("Digite a idade: "))
    idade = pessoa['idade'] + idade

    geral.append(pessoa.copy())

    opcao = str(input("Deseja inserir outra pessoa ? S/N "))
    if opcao in 'Nn':
        break

mediaIdade = idade / numeroPessoa

for pessoa in geral:

    if pessoa['idade'] > mediaIdade:
        acimaMedia.append(pessoa['nome'])
    if pessoa['sexo'] in 'Ff':
        mulher.append(pessoa["nome"])
print('=*' * 30)
print(f'\nAs mulheres cadastradas foram: ', end='')
for k in mulher:
    print(f'{k} ', end='')

print(f'\nAs pessoas acima da média de idade são: ', end='')
for k in acimaMedia:
    print(f'{k} ', end='')
print(f'\nO número de pessoas cadastradas foram de {numeroPessoa} pessoas')
print('=*' * 30)
print(f"A média de idade é de {mediaIdade:.1f} anos")
print('=*' * 30)