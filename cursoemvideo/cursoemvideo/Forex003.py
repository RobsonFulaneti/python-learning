n1 = 0
for c in range(0, 6):
    num = int(input("Digite um numero: "))
    if num % 2 == 0:
        n1 += num
print("A soma é: {}".format(n1))