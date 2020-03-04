pessoa = dict()
mulher = list()
acimaMedia = list()
mediaIdade = 0
idade = 0
numeroPessoa = 0
while True:
    pessoa['nome'] = str(input("Digite o nome da pessoa: "))
    numeroPessoa += 1
    pessoa['sexo'] = str(input("Digite o sexo (M ou F): "))

    if pessoa['sexo'] in 'Ff':
        mulher.append(pessoa["nome"])
    pessoa['idade'] = int(input("Digite a idade: "))
    idade = pessoa['idade'] + idade
    mediaIdade = idade/numeroPessoa
    opcao = str(input("Deseja inserir outra pessoa ? S/N "))
    if opcao in 'Nn':
        break
    if pessoa['idade'] > mediaIdade:
        acimaMedia.append(pessoa.copy())
print('=*' * 30)
print(f'O número de pessoas cadastradas foram de {numeroPessoa} pessoas')
print('=*' * 30)
print(f"A média de idade é de {mediaIdade:.1f} anos")
print('=*' * 30)
print(f'As mulheres cadastradas são {mulher}')
print('=*' * 30)
print(f'As pessoas com idade acima da média são: {acimaMedia}')