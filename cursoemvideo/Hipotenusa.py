co = float(input("O valor do cateto oposto é: "))
ca = float(input('O valor do cateto adjacente é: '))
hi = (co**2 + ca**2) ** (1/2)
print("O valor da Hipotenusa é de {:.2f}".format(hi))

import math
co = float(input("O valor do cateto oposto é: "))
ca = float(input('O valor do cateto adjacente é: '))
hi = math.hypot(co, ca)
print("O valor da Hipotenusa é de {:.2f}".format(hi))

from math import hypot
co = float(input("O valor do cateto oposto é: "))
ca = float(input('O valor do cateto adjacente é: '))
hi = hypot(co, ca)
print("O valor da Hipotenusa é de {:.2f}".format(hi))