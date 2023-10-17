def area(a, b):
    c = a*b
    print(f'A área de um terreno {a} x {b} é de {c}m².')


# Programa Principal
print('Controle de Terrenos')
print('-' * 23)
larg = float(input('Largura (m): '))
comp = float(input('Comprimento (m): '))
area(larg, comp)


