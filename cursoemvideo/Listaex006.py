geral = [[], []]
valor = 0
for n in range(0, 7):
    valor = int(input("Digite um numero: "))
    if (valor % 2) == 0:
        geral[0].append(valor)
    else:
        geral[1].append(valor)
geral[0].sort()
geral[1].sort()
print(geral)