import math
n1 = float(input('Digite o número: '))
n2 = math.trunc(n1)
print('O número {} tem a parte inteira {}.'.format(n1, n2))

cat1 = float(input('Digite o cateto oposto: '))
cat2 = float(input('Digite o cateto adjacente: '))
#hip1 = ((cat1**2)+(cat2**2))**(1/2)
hip1 = math.hypot(cat1, cat2)
print('O comprimento da hipotenusa é {:.2f}.'.format(hip1))

ang1 = float(input('Digite o ângulo: '))
val_sen = math.sin(math.radians(ang1))
val_cos = math.cos(math.radians(ang1))
val_tan = math.tan(math.radians(ang1))
print('O ângulo é {}.\nO valor do seno é {:.2f}\nO valor do cosseno é {:.2f}\nO valor da tangente é {:.2f}.'.format(ang1, val_sen, val_cos, val_tan))

