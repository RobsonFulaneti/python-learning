def aluguelCarro(valor1, valor2):
    calculo = (dias * 60) + (km * 0.15)
    return calculo


dias = int(input('Quantos dias você ficou com o carro ? '))
km = float(input('Quantos Km você rodou com o carro ? '))
preco = aluguelCarro(dias, km)

print('O Total a pagar é de R${:.2f}'.format(preco))