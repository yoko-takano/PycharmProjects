def fatorial(num=1):  # caso não seja informado
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2} e {f3}.')
n = int(input('Digite um número: '))
print(fatorial(n))
print(f'O fatorial de {n} é igual a {fatorial(n)}.')


def par(x=0):
    if x % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite o número: '))
if par(num):
    print('É par!')
else:
    print('Não é par!')
