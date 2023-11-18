lista = []
# Cibele antes de Camila
# Celeste depois de Camila

for i in range(3):
    idade = int(input("Idade de uma irmã: "))
    lista.append(idade)

organizada = sorted(lista)
print(organizada[1])
