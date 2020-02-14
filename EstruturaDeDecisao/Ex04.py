while True:
    letra = str(input("Digite uma letra: "))
    if letra in "Aa, Ee, Ii, Oo, Uu":
        print("Vogal")
    elif letra.isalpha():
        print("Consoante")
    else:
        print("Não é uma letra")
    cont = int(input("Digite 1 para continuar ou 0 para sair: "))
    if cont == 0:
        break
print("FIM")