n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))
if (n1 > n2) and (n1 > n3) and (n2 < n3):
    print("O Maior número é {}, e o menor é {}".format(n1, n2))
elif (n1 > n2) and (n1 > n3) and (n3 < n2):
    print("O Maior número é {}, e o menor é {}".format(n1, n3))
elif (n2 > n1) and (n2 > n3) and (n3 < n1):
    print("O Maior número é {}, e o menor é {}".format(n2, n3))
elif (n2 > n1) and (n2 > n3) and (n1 < n3):
    print("O Maior número é {}, e o menor é {}".format(n2, n1))
elif (n3 > n2) and (n3 > n1) and (n1 < n2):
    print("O Maior número é {}, e o menor é {}".format(n3, n1))
else:
    print("O Maior número é {}, e o menor é {}".format(n3, n2))