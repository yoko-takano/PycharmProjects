def dividirPedacos(lista, tamanhoPedaco):
    pedacos = []
    for i in range(0, len(lista), tamanhoPedaco):
        pedacos.append(lista[i:i+tamanhoPedaco])
    return pedacos


qntd = 6
lista = [8, 9, 1, 0, 1, 1]
listaExt = []
for i in range(1, qntd + 1):
    listaInt = dividirPedacos(lista, i)
    numeros = [int(''.join(map(str, sublist))) for sublist in listaInt]
    listaExt.append(numeros)

print(listaExt)