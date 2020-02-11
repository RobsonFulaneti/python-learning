num = list()
valor = 0
for c in range(0, 5):
    valor = int(input("Digite um numero: "))
    if c == 0 or valor > num[-1]:
        num.append(valor)
    else:
        pos = 0
        while pos < len(num):
            if valor <= num[pos]:
                num.insert(pos, valor)
                break
            pos += 1
print(num)