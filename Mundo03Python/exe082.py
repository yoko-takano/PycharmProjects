parar = 0
lista = []

while parar != 's':
    valor = int(input('Digite um valor: '))
    lista.append(valor)
    parar = str(input('Você quer parar? [S/N] ')).lower().strip()[0]

pares = []
impares = []

for c in range(0, len(lista)):
    if lista[c] % 2 == 0:
        pares.append(lista[c])

for d in range(0, len(lista)):
    if lista[d] % 2 != 0:
        impares.append(lista[d])

print(f'A lista completa é {lista}.')
print(f'A lista de pares é {pares}.')
print(f'A lista de ímpares é {impares}.')