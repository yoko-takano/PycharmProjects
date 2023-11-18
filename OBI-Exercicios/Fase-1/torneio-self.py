# Venceram 5 ou 6 jogos = Grupo 1
# Venceram 3 ou 4 jogos = Grupo 2
# Venceram 1 ou 2 jogos = Grupo 1
# Só perderam, retorna -1

vencidas = 0
perdidas = 0
for i in range(6):
    resultado = str(input("Venceu ou Perdeu? [V/P] ")).lower().strip()[0]
    if resultado == "v":
        vencidas += 1
    else:
        perdidas += 1

if vencidas >= 5:
    print(" >> Grupo 1")
elif vencidas >= 3:
    print(" >> Grupo 2")
elif vencidas >= 1:
    print(" >> Grupo 3")
else:
    print(" >> Só perdeu!")
