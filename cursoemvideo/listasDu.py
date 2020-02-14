numeros = []
maior = 0
menor = 0
for i in range(0, 5):
    num = int(input("Digite um numero para a lista: "))
    numeros.append(num)
    if i == 0:
        menor = num
    if num > maior:
        maior = num
    if num < menor:
        menor = num
print(numeros)
print(maior)
print(menor)

