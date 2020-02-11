from random import randint
acertou = False
tentativa = 0
while not acertou:
    computador = randint(0, 5)
    jogador = int(input("Digite um numero de 1 a 5: "))
    tentativa += 1
    if jogador == computador:
        print("Voce Acertou parabens")
        acertou = True
    else:
        if jogador < computador:
            print("Digite um numero maior o numero tinha sido {}".format(computador))
        elif jogador > computador:
            print("Digite um numero menor o numero tinha sido {}".format(computador))
print("Você acertou em {} tentativas".format(tentativa))