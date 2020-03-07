n1 = str(input("Digite um nome: ")).upper().strip()
print("A primeira letra A esta na posição {} e a ultima na posição {}".format(n1.find("A")+1, n1.rfind("A")+1))