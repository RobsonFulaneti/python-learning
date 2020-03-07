n1 = float(input("Digite o primeiro numero: "))
n2 = float(input("Digite o segundo numero: "))
n3 = float(input("Digite o terceiro numero: "))
if n1 > n2 and n1 > n3:
    print(f"O maior número é {n1}")
elif n2 > n1 and n2 > n3:
    print(f"O maior número é {n2}")
else:
    print(f"O maior número é {n3}")

if n1 < n2 and n1 < n3:
    print(f"O menor número é {n1}")
elif n2 < n1 and n2 < n3:
    print(f"O menor número é {n2}")
else:
    print(f"O menor número é {n3}")