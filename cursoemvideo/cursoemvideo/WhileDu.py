a = 80000
b = 200000
c = 0
while a < b:
    a = a + (a * 3/100)
    b = b + (b * 1.5/100)
    c += 1
print(f"A População de A irá ultrapassar a de B em {c} anos")