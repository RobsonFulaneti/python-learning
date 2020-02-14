cont = ('Zero', 'Um', 'Dois', "Três", "Quatro", "Cinco", "Seis", "Sete", "Oito", "Nove", "Dez")
print(f"A ordem alfabetica é: {sorted(cont)}")
print(f"Os Seis primeiros são: {cont[:6]}")
print(f"Os Cinco ultimos são: {cont[-5:]}")
print(f"O numero 7 está na {cont.index('Sete')}ª posição")
while True:
    num = int(input("Digite um numero entre 0 e 10: "))
    if 0 <= num <= 10:
        break
    print("Tente novamente, ", end='')
print(f'Voce digitou o número {cont[num]}')