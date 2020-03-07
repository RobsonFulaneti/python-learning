nome = str(input("Digite seu nome completo: ")).strip()
ult = nome.split()
print(ult[0], ult[len(ult)-1])
print(ult[len(ult)-1], ult[0])