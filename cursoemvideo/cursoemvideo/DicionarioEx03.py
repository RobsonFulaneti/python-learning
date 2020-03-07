from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input("Digite o ano de seu nascimento: "))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Numero da carteira de trabalho: '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input("Digite o ano de sua contratação: "))
    dados['salario'] = float(input("Qual o seu salário ? R$ "))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
print('*-' * 30)
for k, v in dados.items():
    print(f'{k} tem o valor de {v}')