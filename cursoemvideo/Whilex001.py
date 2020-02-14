n = str(input("Digite o sexo: ")).upper()
while n not in 'MF':
    n = str(input("sexo invalido digite novamente: ")).upper()
if n == 'F':
    print("Seu sexo é feminino")
else:
    print("Seu sexo é masculino")
