n = 0
total = 0
qtd = 0
while n != 999:
    n = int(input("Digite um numero diferente de 999: "))
    if n == 999:
        break
    total += n
    qtd += 1
print("A soma é {}, foram {} numeros digitados".format(total, qtd))