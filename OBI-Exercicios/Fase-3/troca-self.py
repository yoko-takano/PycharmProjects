# INPUT
qntdCartas = int(input("Quantidade de cartas: "))
qntdTrocas = int(input("Quantidade de trocas: "))

print("Digite as cartas para cima:")
paraCima = [int(qntdCartas) for qntdCartas in input().split()]

print("Digite as cartas para baixo:")
paraBaixo = [int(qntdCartas) for qntdCartas in input().split()]

print("Digite as trocas a serem feitas:")
interTrocas = []
j = 2
for i in range(qntdTrocas):
    apoio = [int(j) for j in input().split()]
    interTrocas.append(apoio)

# DESENVOLVIMENTO
for i in range(qntdTrocas):
    for j in range(interTrocas[i][0]-1, interTrocas[i][1]):
        paraCima[j], paraBaixo[j] = paraBaixo[j], paraCima[j]

# OUTPUT
print(paraCima)
