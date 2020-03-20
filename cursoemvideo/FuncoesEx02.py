def printaNome(nome):
    print(f"O seu nome tem {len(nome)} letras, {nome}")
    print('-' * len(nome) + '--')
    print('', nome)
    print('-' * len(nome) + '--')


nomeDigitado = str(input("Digite seu nome: "))
printaNome(nomeDigitado)