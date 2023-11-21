from sympy import symbols, solve

# Entradas
x, y = symbols('x y')
entradas = 5
lista = [int(entradas) for entradas in input().split()]

# Tratamento das entradas com simbólica
contador = 0
for i in range(entradas):
    if lista[i] == -1:
        if contador == 0:
            lista[i] = x
            contador += 1
        else:
            lista[i] = y
            contador += 1

if contador == 1:  # Tem apenas uma incognita x
    if lista[0] == x:
        lista[0] = lista[2] + lista[3] + lista[4]
    if lista[1] == x:
        lista[1] = 3*lista[2] + lista[3]
    if lista[2] == x:
        lista[2] = lista[0] - lista[3] - lista[4]
    if lista[3] == x:
        lista[3] = lista[0] - lista[2] - lista[4]
    if lista[4] == x:
        lista[4] = lista[0] - lista[2] - lista[3]
    print(f"{lista[0]} {lista[1]} {lista[2]} {lista[3]} {lista[4]}")
elif contador == 2:  # Tem duas incógnitas x e y
    expr1 = lista[2] + lista[3] + lista[4] - lista[0]
    expr2 = (3*lista[2]) + lista[3] - lista[1]
    resultado = solve((expr1, expr2), (x, y))
    valueX = abs(resultado[x])
    valueY = abs(resultado[y])
    for i in range(entradas):
        if lista[i] == x:
            print(f"{valueX}", end=" ")
        elif lista[i] == y:
            print(f"{valueY}", end=" ")
        else:
            print(f"{lista[i]}", end=" ")
