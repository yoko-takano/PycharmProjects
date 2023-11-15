lista = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = 0
terc = 0
mai = 0
men = 0

for n in range(0, 3):
    for x in range(0, 3):
        lista[n][x] = int(input(f'Digite um valor para [{n}, {x}]: '))

print('~~~x'*10)
for y in range(0, 3):
    for z in range(0, 3):
        print(f'[{lista[y][z]}]', end=' ')
    print('')
