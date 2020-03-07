dias = int(input('Quantos dias você ficou com o carro ? '))
km = float(input('Quantos Km você rodou com o carro ? '))
preco = (dias * 60) + (km * 0.15)
print('O Total a pagar é de R${:.2f}'.format(preco))