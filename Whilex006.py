n = 0
total = 0
qtd = 0
p = 's'
maior = 0
menor = 0
while p in 's':
    n = int(input("Digite um numero: "))
    total += n
    qtd += 1
    menor = n
    if n > maior:
        maior = n
    if maior > menor:
        menor = n
    p = str(input("Deseja continuar s/n ? "))
print(f"A média dos números é {total/qtd}")
print(f"O maior é {maior}")
print(f"O menor é {menor}")