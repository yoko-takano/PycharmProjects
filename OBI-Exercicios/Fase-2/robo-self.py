nEstacoes, nComandos, devastada = input().split()
nEstacoes = int(nEstacoes)
nComandos = int(nComandos)
devastada = int(devastada)
listaComandos = [int(i) for i in input().split()]

listaEstacoes = []
for i in range(1, nEstacoes+1):
    listaEstacoes.append(i)

posicao = 0
sequencia = [1]
for comando in listaComandos:
    posicao += comando
    atual = listaEstacoes[posicao]
    sequencia.append(atual)

cont = 0
for estacoes in sequencia:
    if devastada == estacoes:
        cont += 1

print(cont)
