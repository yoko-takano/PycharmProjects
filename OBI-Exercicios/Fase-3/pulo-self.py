# qntdLajotas = int(input("Digite a quantidade de lajotas: "))
# lista = [int(qntdLajotas) for qntdLajotas in input().split()]
qntdLajotas = 12
# lista = [1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1]
# lista = [1, 0, 1, 1, 0, 1, 1, 0, 1]
# lista = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
lista = [1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1]

pulos = 0
i = 0
safe = 0
while i < qntdLajotas and safe < qntdLajotas:
    if i < qntdLajotas-2:
        if lista[i+2] == 1:
            pulos += 1
            i += 2
        elif lista[i+1] == 1:
            pulos += 1
            i += 1
    else:
        pulos += 1
        i += 1
    safe += 1

print(pulos-1)

