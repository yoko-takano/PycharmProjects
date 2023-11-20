import numpy as np
# Entradas
N = int(input("Quantidade de linhas x colunas: "))
matriz = []
print("Digite o tabuleiro inicial: ")
for i in range(N):
    lista = [int(i) for i in input().split()]
    matriz.append(lista)

for i in range(1, N):
    for j in range(1, N):
        diagonal = matriz[i-1][j-1]
        superior = matriz[i-1][j]
        inferior = matriz[i][j-1]
        contador = [diagonal, superior, inferior]
        quantos1 = contador.count(1)
        quantos0 = contador.count(0)
        if quantos1 < quantos0:
            matriz[i][j] = 1
        else:
            matriz[i][j] = 0

#matrizBonita = np.array(matriz)
print(matriz[N-1][N-1])
