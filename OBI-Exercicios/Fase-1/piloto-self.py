carroA = int(input("Posição do carro A: "))
carroB = int(input("Posição do carro B: "))
carroC = int(input("Posição do carro C: "))

# acelerar (1)
# desacelerar(-1)
# manter a velocidade (0)

distancia1 = carroB - carroA
distancia2 = carroC - carroB
if distancia1 < distancia2:
    print(1)
elif distancia1 > distancia2:
    print(-1)
else:
    print(0)