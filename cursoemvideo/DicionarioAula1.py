pessoas = {'nome': 'Robson', 'sexo': 'M', 'idade': 24}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
for k, v in pessoas.items():
    print(f'{k} = {v}')

del pessoas['sexo']
print(pessoas.items())

pessoas['nome'] = 'Eduardo'
print(pessoas.items())

pessoas['peso'] = 70.5
print(pessoas.items())