from random import randint
a = randint(1, 10)
b = randint(1, 10)
c = randint(1, 10)
d = randint(1, 10)
e = randint(1, 10)
aleat = (a, b, c, d, e)

print('Os números sorteados foram:', end=' ')
for d in range(0, len(aleat)):
    print(f'{aleat[d]}', end=' ')

print('')
maior = 0
menor = 0

for c in range(0, len(aleat)):
    if c == 0:
        maior = aleat[c]
        menor = aleat[c]
    else:
        if aleat[c] >= maior:
            maior = aleat[c]
        if aleat[c] <= menor:
            menor = aleat[c]

print(f'O maior valor sorteado foi {maior}.')
print(f'O menor valor sorteado foi {menor}.')

print(f'O maior valor sorteado foi {max(aleat)}.')
print(f'O menor valor sorteado foi {min(aleat)}.')
