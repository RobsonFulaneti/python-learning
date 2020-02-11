num = int(input("Digite um numero na tabuada: "))
for c in range(0, 11):
    tab = num * c
    print("{} x {} = {}".format(num, c, tab))