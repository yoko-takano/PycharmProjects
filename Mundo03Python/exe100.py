from random import randint
from time import sleep


def sorteio(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for x in range(0, 5):
        valor = randint(1, 10)
        print(f'{valor}', end=' ')
        sleep(0.5)
        lista.append(valor)
    print('Pronto!')


def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}.')


números = list()
sorteio(números)
somaPar(números)


