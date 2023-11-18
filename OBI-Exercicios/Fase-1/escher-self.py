tamanho = int(input("Insira o tamanho da lista: "))
valores = [int(i) for i in input().split()]

if tamanho % 2 == 0:
    metade = len(valores) // 2
    parte1 = valores[:metade]
    parte2 = valores[metade:]
    parte2.reverse()
    print(parte1)
    print(parte2)
    cont = 0
    for i in range(len(parte1)):
        if parte1[i] + parte2[i] != 10:
            cont += 1
    if cont == 0:
        print("S")
    else:
        print("N")
else:
    print("N")
