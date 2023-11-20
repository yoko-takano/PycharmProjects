# ENTRADAS
lista = []
for i in range(16):
    lista.append(0)
mestreKung = int(input("Posição do Mestre Kung: "))
mestreLu = int(input("Posição do Mestre Lu: "))
lista[mestreKung-1] = 1
lista[mestreLu-1] = 1

# DESENVOLVIMENTO
lim = 16
nova = []
x = 0
while x == 0:
    for i in range(0, lim, 2):
        pos1 = lista[i]
        pos2 = lista[i+1]
        final = pos1 + pos2
        if pos1 + pos2 == 2:
            if lim == 16:
                print("Oitavas")
            elif lim == 8:
                print("Quartas")
            elif lim == 4:
                print("Semifinal")
            else:
                print("Final")
            x = 1
            break
        nova.append(final)
    lista = nova
    nova = []
    lim = int(lim/2)
