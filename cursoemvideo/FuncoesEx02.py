def printaNome(nome):
    print(f"O seu nome tem {len(nome)} letras, {nome}")
    print('-' * len(nome) + '--')
    print('', nome)
    print('-' * len(nome) + '--')


while True:
    nomeDigitado = str(input("Digite seu nome: "))
    printaNome(nomeDigitado)
    sair = str(input("Quer continuar ? S/N "))
    if sair in 'Nn':
        break