num = [2, 5, 9, 1]
num[2] = 3 #altera, na posição 2 o numero para 3
print(num)
num.append(7)# adiciona o numero na lista
print(num)
num.sort()#coloca na ordem
print(num)
num.sort(reverse=True)#coloca na ordem reversa
print(num)
print(f"Essa lista tem {len(num)} numeros")
print(num)
num.insert(2, 0) #insere o numero 2 na posição 0
print(num)
num.pop(2)# tira o numero da posição
print(num)
num.remove(2)# tira o numero da lista, na primeira vez que encontrar
print(num)
print("------------------------------------------")
valores = list()
for cont in range(0, 5):
    valores.append(int(input("Digite um numero: ")))
for c, v in enumerate(valores):
    print(f"Na posição {c} encontrei o valor {v}")
print("Fim")
print("------------------------------------------")

a = [2, 3, 4, 5]
b = a[:]
b[2] = 8
print(a)
print(b)