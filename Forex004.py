pri = int(input("Digite o primeiro termo: "))
raz = int(input("Digite a razão: "))
decimo = pri + (10-1) * raz
for c in range(pri, decimo + raz, raz):
    print(c, end=' > ')
print("Fim")


pri = int(input("Digite o primeito termo: "))
raz = int(input("Digite a razão: "))
cont = 1
termo = pri;
while cont <=10:
    print("{}".format(termo), end=' ');
    termo += raz
    cont +=1
print("fim")