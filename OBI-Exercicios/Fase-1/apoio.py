
listaDimensao = [1, 3]
tamanho = len(listaDimensao)
listaNumPrint = [2, 1]

listaExterna = []
for i in range(tamanho):
    print(i)
    for j in range(1, listaDimensao[i]+1):
        print(j)
        listaInterna = []
        if j == 1:
            print("Linha cheia")
            for k in range(listaDimensao[i]):
                listaInterna.append(listaNumPrint[i])
        elif j == listaDimensao[i]:
            print("Linha cheia")
            for k in range(listaDimensao[i]):
                listaInterna.append(listaNumPrint[i])
        else:
            print("Acrescenta no começo e no fim")
        listaExterna.append(listaInterna)

print(listaExterna)