#Faça um Programa que peça dois números e imprima o maior deles.
numero1 = int(input("Digite o primeiro numero: "))
numero2 = int(input("Digite o segundo numero: "))
if numero1 > numero2:
    print("O Primeiro número é o maior")
elif numero2 > numero1:
    print("O segundo número é o maior")
else:
    print("Os números são iguais")