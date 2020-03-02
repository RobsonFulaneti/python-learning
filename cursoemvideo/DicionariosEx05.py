pessoa = dict()
todos = list()
while True:
    pessoa['nome'] = str(input("Digite o nome da pessoa: "))
    pessoa['sexo'] = str(input("Digite o sexo (M ou F): "))
    pessoa['idade'] = int(input("Digite a idade: "))
    opcao = str(input("Deseja inserir outra pessoa ? S/N "))
    if opcao in 'Nn':
        break