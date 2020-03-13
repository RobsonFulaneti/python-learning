def área(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg} * {comp} é de {a} metros')


print('Controle de terrenos')
print('-' * 30)
l = float(input('Largura: '))
c = float(input('Comp: '))
área(l, c)