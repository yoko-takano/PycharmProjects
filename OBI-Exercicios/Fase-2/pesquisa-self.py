# primeira linha quantidade de pesquisas
# na lista: Estado Preço Alcool Gasolina
pesquisa = int(input("Quantidade de pesquisas: "))
lista = []
for i in range(pesquisa):
    estado, alcool, gasolina = input().split()
    alcool = float(alcool)
    gasolina = float(gasolina)
    limite = gasolina*0.7
    if alcool <= limite:
        lista.append(estado)

if len(lista) == 0:
    print("*")
else:
    for estados in lista:
        print(estados)