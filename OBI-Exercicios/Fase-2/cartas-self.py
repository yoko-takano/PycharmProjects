# Inputs
A = int(input("Digite 1° carta: "))
B = int(input("Digite 2° carta: "))
C = int(input("Digite 3° carta: "))

# Desenvolvimento
lista = [A, B, C]
retorno = []
for i in range(3):
    cont = 0
    for j in range(3):
        if lista[i] == lista[j]:
            cont += 1
    retorno.append(cont)

# Outputs
for k in range(3):
    if retorno[k] == 1:
        print(lista[k])
