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

    while True:
        pessoa['sexo'] = str(input("Digite o sexo (M ou F): ")).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print("\033[0;31mERRO Digite M para masculinho e F para feminino.\033[m")

    pessoa['idade'] = -1

    while pessoa['idade'] != str:
        try:
            pessoa['idade'] = int(input("Digite a idade: "))
            break
        except:
            print("\033[0;31mDigite um número para a idade, \033[m", end='')
            continue
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

print('\033[0;35m=*\033[m' * 30)
print(f'A) As mulheres cadastradas foram: ', end='')

for k in mulher:
    print(f'{k} ', end='')
print(f'\nB) As pessoas acima da média de idade são: ', end='')

for k in acimaMedia:
    print(f'{k} ', end='')

print(f'\nC) O número de pessoas cadastradas foram de {numeroPessoa} pessoas')
print(f"D) A média de idade é de {mediaIdade:.1f} anos")
print('\033[0;35m=*\033[m' * 30)