# INPUTS
lia1 = int(input("1° carta da Lia: "))
lia2 = int(input("2° carta da Lia: "))
carol1 = int(input("1° carta da Carolina: "))
carol2 = int(input("2° carta da Carolina: "))
lista = [[lia1, lia2], [carol1, carol2]]

# DESENVOLVIMENTO
resultado = []
for i in range(2):
    carta1 = lista[i][0]
    carta2 = lista[i][1]
    if carta1 == carta2:
        total = (lia1 + lia2)*2
    else:
        maior = max(carta1, carta2)
        menor = min(carta1, carta2)
        if maior == menor + 1:
            total = (carta1 + carta2) * 3
        else:
            total = carta1 + carta2
    resultado.append(total)

# OUTPUTS
if resultado[0] > resultado[1]:
    print("Lia")
elif resultado [0] < resultado[1]:
    print("Carolina")
else:
    print("Empate")