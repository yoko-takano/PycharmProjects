valorFinal = 0

for i in range(2):
    x = int(input('Idade da amiga: '))
    if x <= 17:
        valorFinal += 15
    elif x <= 59:
        valorFinal += 30
    else:
        valorFinal += 20

print(valorFinal)
