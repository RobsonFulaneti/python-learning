def maiorNumero():
    if n1 > n2:
        print(f"O maior numero é {n1}")
    elif n2 > n1:
        print(f'O maior numero é {n2}')
    else:
        print("Os numeros digitados são iguais")


while True:
    n1 = float(input('Digite o primeiro numero: '))
    n2 = float(input('Digite o segundo numero: '))
    maiorNumero()