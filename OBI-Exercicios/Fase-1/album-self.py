N = int(input("Total de figurinhas/espaços no álbum: "))
M = int(input("Número de figurinhas já compradas: "))

# LISTA DAS FIGURINHAS
listaFigs = []
print("Digite as figurinhas figurinhas compradas: ")
for i in range(M):
    valor = int(input())
    listaFigs.append(valor)

# LISTA DO ALBUM
listaAlbum = []
for i in range(N):
    listaAlbum.append(0)

# DESENVOLVIMENTO
for figurinhas in listaFigs:
    listaAlbum[figurinhas-1] = 1

# RESULTADO
totalFigs = N - (sum(listaAlbum))
print(totalFigs)