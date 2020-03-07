#Faça um Programa que verifique se uma letra digitada é "F" ou "M".
#Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
while True:
    letra = str(input('Digite a primeira letra do sexo: '))
    if letra in "Ff":
        print("Sexo Feminino")
    elif letra in "Mm":
        print("Sexo Masculino")
    else:
        print("Sexo Invalido")
    cont = str(input("Deseja continuar ? "))
    if cont in "Nn":
        break