import random
n1 = str(input("Digite o primeiro clube: "))
n2 = str(input("Digite o segundo clube: "))
n3 = str(input("Digite o terceiro clube: "))
lista = [n1, n2, n3]
random.shuffle(lista)
print("A Classificação no fim será: {}".format(lista))

from random import shuffle
n1 = str(input("Digite o primeiro clube: "))
n2 = str(input("Digite o segundo clube: "))
n3 = str(input("Digite o terceiro clube: "))
lista = [n1, n2, n3]
shuffle(lista)
print("A Classificação no fim será: {}".format(lista))