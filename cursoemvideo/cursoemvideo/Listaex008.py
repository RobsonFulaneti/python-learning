matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for lin in range(0, 3):
    for col in range(0, 3):
        matriz[col][lin] = int(input(f"Digite a posicão [{col}, {lin}]: "))

for lin in range(0, 3):
    for col in range(0, 3):
        print(f'[{matriz[lin][col]:^5}]', end='')
    print()