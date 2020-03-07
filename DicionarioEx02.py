from random import randint
from operator import itemgetter
jogo = {}
for i in range(0, 5):
    jogo[f'Jogador {i+1}'] = randint(0, 6)
ranking = list()
print('Valores sorteados: ')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
# key=itemgetter() se dentro for 0 ele coloca em ordem de chave, se for 1 coloca em ordem de valor
print("=*" * 30)
print("Ordenação: ")
for i, v in enumerate(ranking):
    print(f'{i+1}° lugar {v[0]} com {v[1]}.')