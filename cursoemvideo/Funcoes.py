def lin():
    print('Def')


lin()

print('*' * 30)


def titulo(txt):
    print('-' * 30)
    print(txt)
    print('-' * 30)


titulo('Curso')
titulo('de')
titulo('Python')

print('*' * 30)


def soma(a, b):
    s = a + b
    print(s)


soma(1, 2)
soma(3, 4)
soma(5, 6)

print('*' * 30)


def segundasoma(c, d):
    print(f'c = {c} e d = {d}')
    resultado = c + d
    print(f'A soma de c + d = {resultado}')


segundasoma(c=4, d=5)
segundasoma(7 ,2)