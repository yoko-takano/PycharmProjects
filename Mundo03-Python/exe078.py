lista = [int(input('Digite um valor para a Posição 0: ')),
         int(input('Digite um valor para a Posição 1: ')),
         int(input('Digite um valor para a Posição 2: ')),
         int(input('Digite um valor para a Posição 3: ')),
         int(input('Digite um valor para a Posição 4: '))]

print('~---~'*10)
print(f'Você digitou os valores {lista}')

maior = 0
menor = 0
for c in range(0, len(lista)):
    if c == 0:
        menor = lista[c]
        maior = lista[c]
    else:
        if lista[c] >= maior:
            maior = lista[c]
        if lista[c] <= menor:
            menor = lista[c]

print(f'O maior valor digitado foi {maior} nas posições', end=' ')
for pos, valor in enumerate(lista):
    if valor == maior:
        print(f'{pos}', end='... ')
print('')

print(f'O menor valor digitado foi {menor} nas posições', end=' ')
for pos1, valor1 in enumerate(lista):
    if valor1 == menor:
        print(f'{pos1}', end='... ')
        