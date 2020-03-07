n1 = int(input('Um valor: '))
n2 = int(input('outro valor: '))
d = n1 / n2
s = n1 + n2
m = n1 * n2
di = n1 // n2
e = n1 ** n2
print('a soma vale {} \no produto vale {} \na divisao vale {:.3f}'.format(s, m, d), end=' ')
print('Divisão inteira {} e potência {} '.format(di, e))