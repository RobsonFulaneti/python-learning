temp = []
princ = []
mai = 0
men = 0
while True:
    temp.append(str(input('nome: ')))
    temp.append(float(input('peso: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('quer continuar ? '))
    if resp in 'Nn':
        break
print(f'As pessoas foram {princ}')
print(f'Ao todo foram {len(princ)}')
for p in princ:
    if p[1] == mai:
        print(f'O maior peso foi de {mai}kg. Peso de {p[0]} ')
for p in princ:
    if p[1] == men:
        print(f'O menor peso foi de {men}kg. Peso de {p[0]} ')