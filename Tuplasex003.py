n1 = int(input("Digite um numero: "))
n2 = int(input("Digite um numero: "))
n3 = int(input("Digite um numero: "))
n4 = int(input("Digite um numero: "))

n = (n1, n2, n3, n4)

print(f"O numero 9 apareceu {n.count(9)} vezes")
if 3 in n:
    print(f"O valor 3 apareceu na posição {n.index(3)+1}")
else:
    print("O numero 3 nao apareceu")
print(f"Os numeros pares que apareceram foram ", end='')
for num in n:
    if num % 2 == 0:
        print(num, end=' ')