print('----------------------------------------------------')
frase = 'Estudando Python para ser programador'
print(frase[2:15:2])
print('Exemplo 4')
#print('Essa função acima mostra a frase iniciando de uma posição até outra posição pulando de 2 em 2 nesse caso')
print('----------------------------------------------------')
frase = 'Estudando Python para ser programador'
print(frase[:12])
print('Exemplo 5')
#print('Essa função acima inicia da posição 0 até uma posição antes da ultima')
print('----------------------------------------------------')
frase = 'Estudando Python para ser programador'
print(frase[9::3])
print('Exemplo 6')
#print('Essa função acima permite que seja printado a frase da posição 9 até o fim de 3 em 3 nesses caso')
print('----------------------------------------------------')
frase = 'Estudando Python para ser programador'
print(len(frase))
print('Exemplo 7')
#print('Essa função acima conta quantos caracteres tem a frase')
print('----------------------------------------------------')
frase = 'Estudando Python para ser programador'
print(frase.count('o'))
print('Exemplo 8')
#print('Essa função acima procura na frase quantas letras em especifico existem')
print('----------------------------------------------------')
frase = 'Estudando Python para ser programador'
print(frase.count('o', 0, 13))
print('Exemplo 9')
#print('Essa função acima procura na frase quantas letras em especifico existem entre uma posição e outra')
print('----------------------------------------------------')
frase = 'Estudando Python para ser programador'
print(frase.find('prog'))
print('Exemplo 10')
#print('Essa função acima procura a posição da palavra')
print('----------------------------------------------------')
frase = 'Estudando Python para ser programador'
print(frase.find('Qualquer palavra'))
print('Exemplo 11')
#print('quando nao existe a palavra printa -1')
print('----------------------------------------------------')
frase = 'Estudando Python para ser programador'
print('para' in frase)
print('Exemplo 12')
#print('Essa função acima procura a palavra na frase e retorna true se existir')
print('----------------------------------------------------')
frase = 'Estudando Python para ser programador'
print('nao existe' in frase)
print('Exemplo 13')
#print('Essa função acima procura a palavra na frase e retorna false se não existir')
print('----------------------------------------------------')
frase = 'Estudando Python para ser programador'
print(frase.replace('Python', 'java'))
print('Exemplo 14')
#print('Essa função acima altera a palavra por outra')
print('----------------------------------------------------')
frase = 'Estudando Python para ser programador'
print(frase.upper())
print('Exemplo 15')
#print('Essa função acima coloca as letras maiusculas')
print('----------------------------------------------------')
frase = 'Estudando Python para ser programador'
print(frase.lower())
print('Exemplo 16')
#print('Essa função acima coloca as letras minusculas')
print('----------------------------------------------------')
frase = 'Estudando Python para ser programador'
print(frase.capitalize())
print('Exemplo 17')
#print('Essa função acima coloca a primeira maiuscula na frase e as demais minusculas')
print('----------------------------------------------------')
frase = 'Estudando Python para ser programador'
print(frase.title())
print('Exemplo 18')
#print('Essa função acima faz com que toda primeira letra depois do espaço seja maiuscula')
print('----------------------------------------------------')
frase = '     Estudando Python para ser programador     '
print(frase.strip())
print('Exemplo 19')
#print('Essa função acima tira espaços desnecessarios')
print('----------------------------------------------------')
frase = 'Estudando Python para ser programador'
print(frase.split())
print('Exemplo 20')
#print('Essa função acima dividi em espaços')
print('----------------------------------------------------')
frase = 'Estudando Python para ser programador'
print('-'.join(frase))
print('Exemplo 21')
#print('Essa função acima coloca entre os espaços o caracter desejado')
print('----------------------------------------------------')
frase = 'Estudando Python para ser programador'
frase = frase.replace('Python', 'java')
print(frase)
print('Exemplo 22')
#print('Essa função acima altera a palavra por outra de outra forma')
print('----------------------------------------------------')