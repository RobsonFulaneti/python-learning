somaidade = 0
mediaidade = 0
maioridadedehomem = 0
nomevelho = ''
menoridade = 0
for p in range(1, 5):
    print("-------- {} PESSOA --------".format(p))
    nome = str(input("Digite o nome: "))
    sexo = str(input("Digite o sexo: ")).upper()
    idade = int(input("Digite a idade: "))
    somaidade += idade
    if p == 1 and sexo == 'M':
        maioridadedehomem = idade
        nomevelho = nome
    if sexo == 'M' and idade > maioridadedehomem:
        maioridadedehomem = idade
        nomevelho = nome
    if sexo == 'F' and idade < 20:
        menoridade += 1
mediaidade = somaidade / 4
print("\nA media de idade do grupo, é de {:.0f}".format(mediaidade))
print("O homem mais velho é o {}".format(nomevelho))
print("{} garota(s) tem menos de 20 anos de idade".format(menoridade))
