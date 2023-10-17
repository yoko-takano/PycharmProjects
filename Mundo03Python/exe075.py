a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
c = int(input('Digite o terceiro valor: '))
d = int(input('Digite o quarto valor: '))
usuario = (a, b, c, d)

cont9 = 0
cont3 = 0

for c in range(0, len(usuario)):
    if usuario[c] == 9:
        cont9 += 1
    if usuario[c] == 3:
        cont3 = c+1

print(f' >> Você digitou os valores {usuario}')
print(f' >> O valor 9 apareceu {cont9} vezes')

if cont3 == 0:
    print(' >> O valor 3 não foi digitado em nenhuma posição')
else:
    print(f' >> O valor 3 apareceu na {cont3}° posição')

print(f' >> Os valores pares digitados foram', end=' ')

for d in range(0, len(usuario)):
    if usuario[d] % 2 == 0:
        print(f'{usuario[d]}', end=' ')
print('')
print(f'O valor 9 apareceu {usuario.count(9)} vezes')

if 3 in usuario:
    print(f'O valor 3 apareceu na {usuario.index(3)+1}° posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
