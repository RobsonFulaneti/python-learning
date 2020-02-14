nome = str(input("Digite seu nome: "))
if nome == "Fulaneti":
   print("Que nome lindo!!!")
print("Bom dia, {}".format(nome))

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
m = (n1+n2)/2
if m >= 5.0:
    print("Tu passou")
else:
    print("DP Parsa")