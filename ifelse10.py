a = int(input("Digite o primeiro lado do triângulo: "))
b = int(input("Digite o segundo lado do triângulo: "))
c = int(input("Digite o terceiro lado do triângulo: "))
if a < b + c and b < c + a and c < a + b:
    print("Triângulo formado")
else:
    print("Não é possível formar um triângulo")