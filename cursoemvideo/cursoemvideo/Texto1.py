nome = str(input('Digite seu nome completo: ')).strip()
print(nome)
print('Nome com todas letras maiusculas: ', nome.upper())
print('Nome com todas letras minusculas: ', nome.lower())
print("A quantidade de letras sem espaços é de:", len(nome) - nome.count(' '))
print("Seu primeiro nome tem {} letras".format(nome.find(" ")))
letras = nome.split()
print("Seu primeiro nome é {} e tem {} letras".format(letras[0], len(letras[0])))