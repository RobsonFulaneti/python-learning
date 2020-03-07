campeonato = dict()
campeonato['Nome'] = str(input('Informe o nome do jogador: '))
campeonato['Partidas'] = int(input("Quantas partidas ele jogou ? "))
campeonato['Gols'] = 0
for i in range(campeonato['Partidas']):
    gols = int(input(f"Quantos gols ele fez na partida {i+1} ? "))
    campeonato['Gols'] = campeonato['Gols'] + gols

for i, j in campeonato.items():
    print(f'{i}: {j}')
print(f"A média do {campeonato['Nome']}, foi de {campeonato['Gols'] / campeonato['Partidas']:.1f} gols por partida")