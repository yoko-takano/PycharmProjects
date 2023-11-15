n1 = 3
s = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        print(c, end=' ')
        s += c #soma = soma + c
        cont += 1

print('\nA soma de todos os {} valores solicitados é {}.'.format(cont,s))
