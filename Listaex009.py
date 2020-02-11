from random import randint
mega = list()
jogos = list()
tot = 0
while tot <= 5:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in mega:
            mega.append(num)
            cont += 1
        if cont >= 6:
            break
    mega.sort()
    jogos.append(mega[:])
    mega.clear()
    tot += 1
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')