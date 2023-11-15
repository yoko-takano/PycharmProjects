num = [2, 5, 9, 1]
print(num)
num[2] = 3
print(num)
num.append(7)
print(num)
num.sort(reverse=True) # do maior para o menor
print(num)
# print(f'Essa lista tem {len(num)} elementos.')
if 5 in num:
    num.remove(5)
else:
    print('Não achei o número 4')
num.insert(2,2)
print(num)
num.remove(2)
print(num)

valores = list() # ou []
valores.append(5)
valores.append(9)
valores.append(4)
print(valores)

for v in valores:
    print(f'{v}...')

for c, d in enumerate(valores):
    print(f'Na posição {c} encontre o valor {d}!')
print('Chegue ao final da lista.')

# Quando se faz uma lista igual a outra, está fazendo uma ligação entre elas:
a = [2, 3, 4, 7]
b = a
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')

# Para desvincular a ligação entre listas:

a1 = [2, 3, 4, 7]
b1 = a1[:]
b1[2] = 8
print(f'Lista A: {a1}')
print(f'Lista B: {b1}')
