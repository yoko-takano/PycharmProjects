n = s = 0
while True:
    n = int(input('Digite um número: [Flag = 999] '))
    if n == 999:
        break
    s += n

print('A soma vale {}.'.format(s))
print(f'A soma vale {s}.')

nome = 'José'
idade = 33
salario = 987.3
print(f'O {nome:^20} tem {idade} anos e ganha R${salario:.2f}.')
#:>20 alinhar a direita
#:<20 alinhar a esquerda