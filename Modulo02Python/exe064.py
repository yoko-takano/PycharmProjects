num = 0
cont = 0
soma = 0
num = int(input('Digite um número [999 para parar]: '))

while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número [999 para parar]: '))

print('Totais de números digitados: {}.'.format(cont))
print('Soma total dos números: {}.'.format(soma))
