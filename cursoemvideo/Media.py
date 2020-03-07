import math
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = ((n1 + n2)/2)
resultado = math.ceil(media)
print('Sua média é {}'.format(resultado))