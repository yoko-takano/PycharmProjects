primeiro = int(input("Primeiro número: "))
segundo = int(input("Segundo número: "))
terceiro = 0
lista = [primeiro, segundo, terceiro]

for i in range(10):
    lista[2] = i
    organizada = sorted(lista)
    media = sum(organizada)/3
    if media == organizada[1]:
        print(i)
        break  # assim que achar o primeiro menor, já para