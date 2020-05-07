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


def conta(a, b):
    s = a + b
    print(s)


conta(1, 2)
conta(3, 4)
conta(5, 6)

print('*' * 30)


def segundasoma(c, d):
    print(f'c = {c} e d = {d}')
    resultado = c + d
    print(f'A soma de c + d = {resultado}')


segundasoma(c=4, d=5)
segundasoma(7, 2)


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)


def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')


soma(5, 2)
soma(2, 9, 4)