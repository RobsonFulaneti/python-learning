#Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
while True:
    numero = int(input("Digite um numero: "))
    if numero > 0:
        print("Esse número é positivo")
    elif numero < 0:
        print("Esse número é negativo")
    else:
        print("Esse número é 0")
    cont = str(input("Deseja continuar ? S/N: "))
    if cont in "Nn":
        break