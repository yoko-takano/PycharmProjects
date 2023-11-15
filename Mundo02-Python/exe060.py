from math import factorial

fatorial = int(input('Digite o número fatorial: '))
cont = fatorial
resultado = 1

print('\033[34m{}!'.format(fatorial), end='')
print('\033[37m', end = ' = ')

while cont != 0:
    resultado = cont*resultado
    if cont != 0:
        print('\033[37m{}'.format(cont), end='')
        if cont != 1:
            print(' x ', end='')
    cont += -1

print(' = ', end='')
print('\033[33m{}'.format(resultado))
print('\033[m')

print('Fatorial {}! = {} (pelo código).'.format(fatorial, resultado))

automatico = factorial(fatorial)
print('Fatorial {}! = {} (pela biblioteca).'.format(fatorial, automatico))
