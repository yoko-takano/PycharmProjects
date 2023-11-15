inicio = int(input('Início: '))
fim = int(input('Fim: '))
p = int(input('Passo: '))

for c in range(inicio, fim+1, p):
    print(c)
print('Fim!')

s = 0
c = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n
print('O somatório de todos os valores foi {}'.format(s))
