impar = []
par = []
geral = []
while True:
    valor = int(input("Digite um numero: "))
    geral.append(valor)
    if (valor % 2) == 0:
        par.append(valor)
    else:
        impar.append(valor)
    opc = str(input("Deseja continuar n/s ? "))
    if opc == 'n':
        break
print(f"Impares {impar}")
print(f"Pares {par}")
print(f"Geral {geral}")