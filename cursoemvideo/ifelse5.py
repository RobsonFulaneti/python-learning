n1 = float(input("Digite quantos KM será a viagem: "))
if n1 <= 200:
    print("O valor da viagem é de R${:.2f}".format(n1 * 0.50))
else:
    print("O valor da viagem é de R${:.2f}".format(n1 * 0.45))