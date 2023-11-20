qntd = int(input("Quantidade de caixas: "))
print("Digite o peso das caixas: ")
lista = [int(qntd) for qntd in input().split()]

desce = 0
cont = 0
for i in range(qntd):
    sobe = lista[i]
    if sobe - desce < 0:
        desce = 0
        delta = sobe - desce
    else:
        delta = sobe - desce
    if delta > 8:
        cont += 1
    print(f"   >> Sobe {sobe}, desce {desce} = {delta}")
    desce = sobe

if cont != 0:
    print("N")
else:
    print("S")
