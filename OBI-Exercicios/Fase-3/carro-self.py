import numpy as np
# Inputs
estradaOL, estradaNS = input().split()
cidades, carros = input().split()
cidades = int(cidades)
carros = int(carros)

# Tratamento das entradas
lista = []
for i in range(cidades):
    pontox, pontoy = input().split()
    pontox = int(pontox)
    pontoy = int(pontoy)
    lista.append([pontox, pontoy])

# Criação da matriz binária
listaExt = []
cont = 0
for i in range(cidades):
    listaInt = []
    for j in range(cidades):
        anteX = lista[i][0]
        anteY = lista[i][1]
        postX = lista[j][0]
        postY = lista[j][1]
        distX = abs(postX - anteX)
        distY = abs(postY - anteY)
        distTot = distX + distY
        if distTot <= (carros/100) and distTot != 0:
            unit = 1
            cont += 1
        elif distTot >= (carros/100):
            unit = 2
        else:
            unit = 0
        listaInt.append(unit)
    listaExt.append(listaInt)

# Outputs
qntdCidades = int(cont/2)
viagensTotais = cidades-1
qntdAviao = viagensTotais - qntdCidades
(print(qntdAviao))

#matriz = np.array(listaExt)
#print(matriz)
