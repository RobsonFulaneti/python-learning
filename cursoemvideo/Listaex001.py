num = []
mai = 0
men = 0
for cont in range(0, 5):
    num.append(int(input("Digite um numero: ")))
    if cont == 0:
        mai = men = num[cont]
    else:
        if num[cont] > mai:
            mai = num[cont]
    if cont == 0:
        mai = men = num[cont]
    else:
        if num[cont] < men:
            men = num[cont]
print(f"O maior numero é o {mai} e esta na posição: ", end='')
for pos, val in enumerate(num):
    if val == mai:
        print(f"{pos} ", end='')
print(f"\nO menor numero é o {men} e está na posição: ", end='')
for pos, val in enumerate(num):
    if val == men:
         print(f"{pos} ", end='')