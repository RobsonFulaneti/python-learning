produto = str(input("Informe o produto que voce deseja comprar: "))
preco1 = float(input("Digite o preço do produto: "))
loja1 = str(input("Digite o nome da loja: "))
preco2 = float(input("Digite o preço do produto: "))
loja2 = str(input("Digite o nome da loja: "))
preco3 = float(input("Digite o preço do produto: "))
loja3 = str(input("Digite o nome da loja: "))
if preco1 < preco2 and preco1 < preco3:
    print(f"A/O {produto} de preço é {preco1} da loja {loja1}")
elif preco2 < preco1 and preco2 < preco3:
    print(f"A/O {produto} de menor preço é {preco2} da loja {loja2}")
else:
    print(f"A/O {produto} de menor preço é {preco3} da loja {loja3}")