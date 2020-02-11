vel = float(input("Digite a sua velocidade: "))
if vel <= 80:
    print("Você está na velocidade correta")
else:
    print("Sua velocidade está acima do permitido e você terá que pagar R${:.2f}, de multa!".format((vel - 80) * 7))