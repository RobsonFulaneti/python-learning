import random
n1 = str(input("Digite o primeiro clube: "))
n2 = str(input("Digite o segundo clube: "))
n3 = str(input("Digite o terceiro clube: "))
lista = [n1, n2, n3]
escolhido = random.choice(lista)
print("O campeão 2019 será: {}".format(escolhido))

from random import choice
n1 = str(input("Digite o primeiro clube: "))
n2 = str(input("Digite o segundo clube: "))
n3 = str(input("Digite o terceiro clube: "))
lista = [n1, n2, n3]
escolhido = choice(lista)
print("O campeão 2019 será: {}".format(escolhido))