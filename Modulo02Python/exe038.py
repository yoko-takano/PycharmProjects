n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))

if n1 > n2:
    print('    >> O primeiro número é maior que o segundo.')
elif n1 < n2:
    print('    >> O segundo número é maior que o primeiro.')
else:
    print('    >> Não existe valor maior, os dois são iguais.')

print('    >> Sendo o primeiro número {} e o segundo {}.'.format(n1, n2))
