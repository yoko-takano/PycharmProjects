# Entradas
cidades = 16  # números de cidades
origem = 2  # cidade de origem
destino = 12  # cidade de destino
rotas = [[3, 5], [12, 3], [5, 1], [2, 1], [4, 1], [6, 1],
         [7, 1], [12, 8], [12, 9], [12, 10], [12, 11],
         [3, 13], [13, 14], [15, 13], [15, 16]]


# Desenvolvimento
tamanho = len(rotas)
viagem = 0

for i in range(tamanho):
    nova = [rotas[i][0], rotas[i][1]]
    nova.reverse()
    rotas.append(nova)

tamanho2 = len(rotas)
cont = 0
while origem != destino:
    i = 0
    for i in range(tamanho2):
        print(origem)
        print(rotas[i][0], rotas[i][1])
        if rotas[i][0] == origem:
            origem = rotas[i][1]
            viagem += 1
    cont += 1

#print(viagem)
