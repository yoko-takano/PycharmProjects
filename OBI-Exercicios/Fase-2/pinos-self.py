import numpy as np

lista = [["-", "-", "o", "o", "o", "-", "-"],
         ["-", "-", "o", "o", "o", "-", "-"],
         ["o", "o", "o", "o", "o", "o", "o"],
         ["o", "o", "o", ".", "o", "o", "o"],
         ["o", "o", "o", "o", "o", "o", "o"],
         ["-", "-", "o", "o", "o", "-", "-"],
         ["-", "-", "o", "o", "o", "-", "-"]]
x = 0
cont = 0
while x < 30:
    for i in range(7):
        for j in range(5):
            if lista[i][j] == "o":
                if lista[i][j+1] == "o":
                    if lista[i][j+2] == ".":
                        lista[i][j] = "."
                        lista[i][j+1] = "."
                        lista[i][j+2] = "o"
                        cont += 1
    x += 1


print(cont)
matriz = np.array(lista)
print(matriz)