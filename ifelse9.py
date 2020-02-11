sal = float(input("Digite seu salário: R$"))
if sal > 1250:
    print("seu salario com aumento de 10% ficou: R${:.2f}".format((sal * 10/100) + sal))
else:
    print("seu salario com aumento de 15% ficou: R${:.2f}".format((sal * 15 / 100) + sal))