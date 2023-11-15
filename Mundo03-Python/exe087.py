lista = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = 0
terc = 0
mai = 0
men = 0

for n in range(0, 3):
    for x in range(0, 3):
        lista[n][x] = int(input(f'Digite um valor para [{n}, {x}]: '))
        if lista[n][x] % 2 == 0:
            pares = pares + lista[n][x]
        if x == 2:
            terc = terc + lista[n][x]
        if n == 1:
            if x == 0:
                mai = lista[n][x]
                men = lista[n][x]
            else:
                if lista[n][x] > mai:
                    mai = lista[n][x]
                if lista[n][x] < men:
                    men = lista[n][x]

print('~~~x'*10)
for y in range(0, 3):
    for z in range(0, 3):
        print(f'[{lista[y][z]}]', end=' ')
    print('')

print(f'A soma dos valores pares é {pares}.')
print(f'A soma dos valores da terceira coluna é {terc}.')
print(f'O maior valor da segunda linha é {mai}.')
print(f'O menor valor da segunda linha é {men}.')
