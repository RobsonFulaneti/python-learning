salario = float(input("Digite qual o seu salário bruto: "))
dias = int(input("Digite quantos dias você trabalha por mês: "))
ir = salario*11/100
inss = salario*8/100
sindicato = salario*5/100
liquido = salario - ir - inss - sindicato
horasab = 0
sabdias = 0
extra = 0

sabado = str(input("Você trabalha de sábado ? "))

if sabado == "sim":
    horasab = float(input("Quantas horas você trabalha no sábado ? "))
    sabdias = float(input("Quantos sábados no mês ? "))

print("Você ganha por hora R${:.2f} ".format(1500/((sabdias * horasab) + (dias * 8))))
print("Salário Bruto: R${:.2f} ".format(salario))
print("IR (11%): R${:.2f} ".format(ir))
print("INSS (8%): R${:.2f} ".format(inss))
print("Sindicato (5%): R${:.2f} ".format(sindicato))
print("Salário Liquido: R${:.2f} ".format(liquido))