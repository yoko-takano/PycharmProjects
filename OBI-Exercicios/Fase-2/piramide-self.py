dimPiramide = 3
listaDimensao = []
listaNumPrint = []
cont = dimPiramide
seq = 1
while cont > 0:
    listaDimensao.append(cont)
    listaNumPrint.append(seq)
    cont -= 2
    seq += 1

listaDimensao.reverse()
listaNumPrint.reverse()
print(listaDimensao)
print(listaNumPrint)



listaInterna = []
listaExterna = []
for camada in listaDimensao:
    for i in range(1, camada+1):
        if i == 0:
            for j in range(camada):
                valor = 1
                listaInterna.append(valor)
            listaExterna.append(listaInterna)
        elif i == camada:
            for j in range(camada):
                valor = 2
                listaInterna.append(valor)
            listaExterna.append(listaInterna)
        else:
            listaExterna.append(3)
            listaExterna.insert(0, 3)
