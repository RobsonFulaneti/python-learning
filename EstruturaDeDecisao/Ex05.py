nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = nota1 + nota2 / 2
if media < 5:
    print(f"Reprovado com nota {media}")
elif media < 10:
    print(f"Aprovado {media}")
else:
    print("Parabéns foi aprovado com 10")