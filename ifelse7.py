a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))
menor = a
if b < c and b < a:
    menor = b
if c < b and c < a:
    menor = c
maior = a
if b > a and b > c:
    maior = b
if c > a and c > a:
    maior = c
print("O menor é {}".format(menor))
print("O maior é {}".format(maior))