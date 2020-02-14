num = list()
valor = 0
for c in range(0, 5):
    valor = int(input("digite um numero: "))
    if valor not in num:
        num.append(valor)
    else:
        valor = int(input("Esse número ja foi adicionado, informe outro número: "))
        if valor not in num:
            num.append(valor)
num.sort()
print(f"O número das listas são: {num}")