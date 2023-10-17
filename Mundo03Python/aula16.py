lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
print(lanche)
print(sorted(lanche))
print(lanche[1:3])
print(lanche[-3:])

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

(print('\n'))

for comida in lanche:
    print(f'Eu vou comer {comida}...')

(print('\n'))

for pos, comida in enumerate(lanche):
    print(f"Eu vou comer {comida} na posição {pos}")

print('Comi pra caramba!')
('\n')

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(c)
print(c.count(9))
print(c.index(2))
print(c.index(2, 4))

pessoa = ('Gustavo', 39, 'M', 99.88) # aceita mais um tipo
del pessoa  # tuplas são imutáveis, porém dá pra deletar tudo



