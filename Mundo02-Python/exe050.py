soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite o {}° número: '.format(c)))
    ver = num % 2
    if ver == 0:
        soma += num
        cont += 1

print('Você informou {} números pares e a soma foi {}.'.format(cont, soma))