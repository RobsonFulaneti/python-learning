alunos = []
passaram = []
recuperacao = []
reprovados = []
opcao = 0


def mostraLinha():
    print("=" * 68)


def mostraMenu():
    print("="*30, " MENU ", "="*30)
    print("[1] Para adicionar alunos\n"
          "[2] Para listar quem passou\n"
          "[3] Para listar quem está de recuperação\n"
          "[4] Para listar quem nao passou\n"
          "[5] Para alunos cadastrados\n"
          "[6] Para sair")


def valorMedia(valor1, valor2):
    calculo = (valor1 + valor2) / 2
    return calculo


def processaMedia(media):
    if media >= 7:
        print(f"{aluno} passou com media {media}!")
        passaram.append([aluno, media])
    elif media >= 3:
        print(f"{aluno} está de recuperação pois fechou com media {media}")
        recuperacao.append([aluno, media])
    else:
        print(f"{aluno} não passou pois fechou com media {media}")
        reprovados.append([aluno, media])


while opcao != 6:
    mostraMenu()
    mostraLinha()

    opcao = int(input("Digite a opção: "))
    if opcao == 1:
        while True:
            mostraLinha()

            aluno = str(input("Digite o nome do aluno: "))
            alunos.append(aluno)
            nota1 = float(input("Digite a primeira nota: "))
            nota2 = float(input("Digite a segunda nota: "))

            media = valorMedia(nota1, nota2)
            processaMedia(media)

            mostraLinha()
            sair = str(input("Voltar ao menu principal ? S/N "))
            if sair in 'Ss':
                break
    if opcao == 2:
        mostraLinha()
        print("Os alunos aprovados foram:", end=''"\n")
        for i, j in passaram:
            print(i, "com nota",j)
    if opcao == 3:
        mostraLinha()
        print("Os alunos de recuperacao foram:", end=''"\n")
        for i, j in recuperacao:
            print(i, "com nota",j)
    if opcao == 4:
        mostraLinha()
        print("Os alunos reprovados foram:", end=''"\n")
        for i, j in reprovados:
            print(i, "com nota",j)
    if opcao == 5:
        mostraLinha()
        print("Os alunos cadastrados foram:", end=''"\n")
        for i in alunos:
            print(i)
    if opcao == 6:
        break
    if opcao not in range(1, 7):
        print("Opção inválida, digite novamente")
print("Obrigado por utilizar o programa")