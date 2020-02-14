import math
an = float(input('Digite o valor do Angulo: '))
seno = math.sin(math.radians(an))
print('O Angulo {} tem o seno de {:.2f}'.format(an, seno))
cosseno = math.cos(math.radians(an))
print('O Angulo {} tem o cosseno de {:.2f}'.format(an, cosseno))
tangente = math.tan(math.radians(an))
print('O Angulo {} tem o tangente de {:.2f}'.format(an, tangente))

from math import radians, sin, cos, tan
an = float(input('Digite o valor do Angulo: '))
seno = sin(radians(an))
print('O Angulo {} tem o seno de {:.2f}'.format(an, seno))
cosseno = cos(radians(an))
print('O Angulo {} tem o cosseno de {:.2f}'.format(an, cosseno))
tangente = tan(radians(an))
print('O Angulo {} tem o tangente de {:.2f}'.format(an, tangente))