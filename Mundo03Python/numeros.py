import uteis  # preferencialmente esse para compatibilidade

num = int(input('Digite um valor: '))
fat = uteis.fatorial(num)
print(f'O fatorial de {num} é {fat}.')
print(f'O dobro de {num} é {uteis.dobro(num)}.')
print(f'O tripo de {num} é {uteis.triplo(num)}.')
