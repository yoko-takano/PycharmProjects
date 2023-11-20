capsulas = int(input("Número de cápsulas: "))
moedasFan = int(input("Número de moedas: "))
print("Ciclo das cápsulas: ")
lista = [int(capsulas) for capsulas in input().split()]

i = 0
dias = 0
moedas = 0
while moedas < moedasFan:
    dias += 1
    for j in range(capsulas):
        if dias % lista[j] == 0:
            moedas += 1

print(f"{dias} dias: {moedas} moedas")