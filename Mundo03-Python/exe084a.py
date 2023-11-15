principal = []
dado = []

while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    principal.append(dado[:])
    dado.clear()
    parar = str(input('Continuar? [S/N] ')).lower().strip()[0]
    if parar in 'n':
        break

(print(principal))
maior = 0
menor = 0
cont = 0
for c in principal:
    if cont == 0:
        maior = c[1]
        menor = c[1]
    else:
        if c[1] >= maior:
            maior = c[1]
        if c[1] <= menor:
            menor = c[1]
    cont += 1

print(f'O maior peso foi de {maior} kg. Peso de ', end='')

for x in principal:
    if x[1] == maior:
        print(f'{x[0]}', end=' ')
print('')
print(f'O menor peso foi de {menor} kg. Peso de ', end='')

for y in principal:
    if y[1] == menor:
        print(f'{y[0]}', end=' ')

print('')
print(f'Ao todo, você cadastrou {len(principal)} pessoas.')

