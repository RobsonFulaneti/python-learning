num = 0
while num != 5:
    n1 = int(input('Digite um numero: '))
    n2 = int(input('Digite um numero: '))
    num = int(input(
        "-----ESCOLHA UMA OPERAÇÃO A SER REALIZADA----- \n[1] Somar \n[2] Multiplicar \n[3] Maior \n[4] Novos numeros "
        "\n[5] Sair do programa \nDigite a opção: "))

    if num == 1:
        print("A Soma de {} + {} é de: {}".format((n1), (n2), (n1 + n2)))
    elif num == 2:
        print("A Multiplicação de {} * {} é de: {}".format((n1), (n2), (n1 * n2)))
    elif num == 3:
        if n1 > n2:
            print(("O numero maior é o {}".format(n1)))
        elif n2 > n1:
            print(("O numero maior é o {}".format(n2)))
        else:
            print(("O maior é o {}".format(n1)))
    if num == 4:
        print("Insira os novos numeros")
print("Obrigado por utilizar o programa")