import random
num = (1, 2, 3, 4, 5)
escolhido = random.choice(num)
n1 = int(input("Digite um numero de 1 a 5: "))
if n1 == escolhido:
    print("Você acertou o número sorteado")
else:
    print("Você errou o número sorteado foi {}".format(escolhido))
