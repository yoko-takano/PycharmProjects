dimensao = int(input("Dimensão: "))
lista = []
print("Digite a lista: ")
for i in range(dimensao):
    apoio = [int(i) for i in input().split()]
    lista.append(apoio)

linha = 0
coluna = 0
for i in range(dimensao):
    for j in range(dimensao):
        if lista[i][j] == 0:
            linha = i+1
            coluna = j+1
            break

linhasSoma = []
for linhas in lista:
    soma = sum(linhas)
    linhasSoma.append(soma)

maximo = max(linhasSoma)
minimo = min(linhasSoma)
numero = maximo - minimo
print(numero, linha, coluna)
