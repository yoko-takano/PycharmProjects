# ENTRADAS
movimentos = int(input("Digite a quantidade de movimentos: "))
caractere = str(input("Digite a posição incial da moeda: "))
print("Digite a sequência de movimentos: ")
lista = []
for i in range(movimentos):
    valor = int(input())
    lista.append(valor)

# PRINCIPAL
posicoes = [0, 0, 0]
if caractere == "A":
    posicoes[0] = 1
elif caractere == "B":
    posicoes[1] = 1
else:
    posicoes[2] = 1

for movs in lista:
    if movs == 1:
        posicoes[0], posicoes[1] = posicoes[1], posicoes[0]
    elif movs == 2:
        posicoes[1], posicoes[2] = posicoes[2], posicoes[1]
    else:
        posicoes[2], posicoes[0] = posicoes[0], posicoes[2]

# SAIDA
for i in range(len(posicoes)):
    if posicoes[i] == 1:
        if i == 0:
            print("Posição da moeda: A")
        elif i == 1:
            print("Posição da moeda: B")
        else:
            print("Posição da moeda: C")
