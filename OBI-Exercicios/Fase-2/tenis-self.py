lista = []

for i in range(4):
    nivel = int(input(f"Digite o nível do {i+1}° jogador: "))
    lista.append(nivel)

ordenada = sorted(lista)
primeiro = lista[0] + lista[3]
segundo = lista[1] + lista[2]
print(f"A menor diferença é: {abs(primeiro-segundo)}")