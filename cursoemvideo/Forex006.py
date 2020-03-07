from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for c in range(1, 3):
    ano = int(input("Digite o ano de seu nascimento: "))
    maior = atual - ano
    if maior >= 18:
        totmaior += 1
    else:
        totmenor += 1
print("Alcançou maioridade {}".format(totmaior))
print("Não alcançou maioridade {}". format(totmenor))