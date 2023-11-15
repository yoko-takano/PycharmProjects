n = 0
cont = 0
soma = 0
maior = 0
menor = 0
resp = 'S'
while resp in 'Ss':
    valor = int(input('Digite o valor: '))
    if cont == 0:
        menor = valor
        maior = valor
    else:
        if valor >= maior:
            maior = valor
        elif valor <= menor:
            menor = valor
    cont += 1
    soma += valor
    resp = str(input('Continuar? [S/N]: ')).upper().strip()[0]

print('Fim!')
print('Você digitou {} números.'.format(cont))
print('A média de todos os valores é {}.'.format(soma/cont))
print('O maior valor é {} e o menor valor é {}.'.format(maior, menor))
