numero = int(input('Digite um numero de 1 a 9999: '))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print("Milhar {} Centena {} Dezena {} unidade {}".format(m, c, d, u))