numeroIlhas = int(input("Número de ilhas: "))
lista = []
for i in range(numeroIlhas):
    coord = [int(i) for i in input().split()]
    lista.append(coord)
alcance = int(input("Alcance: "))
print(lista)

listaDistancia = []
for i in range(len(lista)-1):
    x1 = lista[i][0]
    y1 = lista[i][1]
    x2 = lista[i+1][0]
    y2 = lista[i+1][0]
    dist = (((x2-x1)**2)+((y2-y1)**2))**(1/2)
    listaDistancia.append(dist)

cont = 0
print(listaDistancia)
for i in range(len(listaDistancia)):
    if listaDistancia[i] > 200:
        cont += 1

if cont == 0:
    print("S")
else:
    print("N")