num = int(input("Digite um numero: "))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[34m', end='')
    print('{} '.format(c), end='')
print("\033[37m \nnumero {} foi divisivel {} vezes".format(num, tot))
if tot == 2:
    print("Este número é primo")
else:
    print("Este número não é primo")