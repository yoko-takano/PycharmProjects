n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1+n2
dim = n1-n2
m = n1*n2
d = n1/n2
di = n1//n2
e = n1**n2
print('A soma vale {} \nA subtração vale {}, \nO produto vale {} \nA divisão é {:.3f}'.format(s, dim, m, d), end='>>>')
print('\nDivisão inteira {} e potência {}'.format(di, e))
