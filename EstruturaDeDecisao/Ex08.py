alunos = []
passaram = []
recuperacao = []
reprovados = []
opcao = 0
while opcao != 5:
    print("="*30, " MENU ", "="*30)
    print("[1] Para adicionar alunos\n[2] Para listar quem passou\n"
          "[3] Para listar quem está de recuperação\n"
          "[4] Para listar quem nao passou\n[5] Para sair")
    print("=" * 68)
    opcao = int(input("Digite a opção: "))
    if opcao == 1:
        while True:
            aluno = str(input("Digite o nome do aluno: "))
            alunos.append(aluno)
            nota1 = float(input("Digite a primeira nota: "))
            nota2 = float(input("Digite a segunda nota: "))
            media = (nota1 + nota2) / 2
            if media >= 7:
                print(f"O {aluno} passou com media {media}!")
                passaram.append(aluno)
            elif media >= 3:
                print(f"O {aluno} está de recuperação pois fechou com media {media}")
                recuperacao.append(aluno)
            else:
                print(f"O {aluno} não passou pois fechou com media {media}")
                reprovados.append(aluno)
            sair = str(input("Voltar ao menu principal ? S/N "))
            if sair in 'Ss':
                break
    if opcao == 2:
        print(passaram)
    if opcao == 3:
        print(recuperacao)
    if opcao == 4:
        print(reprovados)
    if opcao == 5:
        break
    if opcao not in range(1, 6):
        print("Opção inválida, digite novamente")
print("Obrigado por utilizar o programa")