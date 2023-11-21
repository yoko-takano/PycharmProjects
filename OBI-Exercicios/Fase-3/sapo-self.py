M = 5  # matriz j
N = 4  # matriz i

nPedras = 6  # número de células que são pedras
lista = [[1, 1], [2, 2], [1, 4], [3, 4], [3, 5], [4, 5]]

sapo = [1, 1]
sapa = [4, 5]

listaExt = []
for i in range(M):
    listaInt = []
    for j in range(N):
        valor = 0
        listaInt.append(valor)
    listaExt.append(listaInt)

print(listaExt)
for pedras in lista:
    posX = pedras[0]-1
    posY = pedras[1]-1
    print(posX, posY)
    # listaExt[posX][posY] = 1

print(listaExt)
