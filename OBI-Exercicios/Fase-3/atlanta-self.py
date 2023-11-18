import math
quantidadeAzul = int(input("Quantidade de azuis: "))
quantidadeBranco = int(input("Quantidade de brancos: "))


raizBranco = math.sqrt(quantidadeBranco)
compBranco = math.ceil(raizBranco)
largBranco = int(quantidadeBranco/compBranco)
azuisCalculados = (largBranco*2) + (compBranco*2) + 4
if azuisCalculados != quantidadeAzul:
    print(-1, -1)
else:
    print((largBranco+2), (compBranco+2))