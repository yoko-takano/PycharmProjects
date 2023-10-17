parar = 0
lista = []

while parar != 's':
    valor = int(input('Digite um valor: '))
    lista.append(valor)
    parar = str(input('Você quer parar? [S/N] ')).lower().strip()[0]

print('~~~x'*10)
print(f'Você digitou {len(lista)} elementos.')
lista2 = lista[:]
lista2.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista2}.')

if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')
