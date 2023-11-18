a = int(input("Quantos amigos são? "))
n = int(input("Quantas filas são? "))
m = int(input("Quantos assentos por fila? "))

melhorFila = n+1
for fila in range(n, 0, -1):
    assentos = [int(i) for i in input().split()]
    continuos = 0
    for assento in assentos:
        if assento == 0:
            continuos += 1
            if continuos >= a:
                if fila < melhorFila:
                    melhorFila = fila
                break
        else:
            continuos = 0

if melhorFila == n+1:
    melhorFila = -1
    print(melhorFila)
else:
    print(melhorFila)