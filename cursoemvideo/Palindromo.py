for c in range(1, 4):
    a = str(input("Digite uma palavra: "))
    b = a[::-1]
    if a == b:
        print("é Palindromo ")
    else:
        print("Não é Palindromo ")
print("Fim")