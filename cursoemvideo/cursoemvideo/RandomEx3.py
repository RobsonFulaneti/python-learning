import random
j1 = str(input("Digite o jogador para seu clube: "))
j2 = str(input("Digite o jogador para seu clube: "))
j3 = str(input("Digite o jogador para seu clube: "))
lista = [j1, j2, j3]
escolhido = random.choice(lista)
print(f"O melhor para seu time é o {escolhido}")
