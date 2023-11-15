parar = 0
lista = []

while parar != 's':
    valor = int(input('Digite um valor: '))
    if valor in lista: # if valor not in lista
        print('Valor duplicado! Não vou adicionar...')
    else:
        lista.append(valor)
    parar = str(input('Você quer parar? [S/N] ')).lower().strip()[0]

print(lista)
lista.sort()
print(f'Você digitou os valores {lista}')
