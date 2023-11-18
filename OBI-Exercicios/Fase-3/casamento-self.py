firstNumber = str(input("Digite o primeiro número: "))
secondNumber = str(input("Digite o segundo número: "))
listFirst = list(firstNumber)
listSecond = list(secondNumber)

if len(listFirst) < len(listSecond):
    zeros = len(listSecond) - len(listFirst)
    for i in range(zeros):
        listFirst.insert(0, "0")
elif len(listFirst) > len(listSecond):
    zeros = len(listFirst) - len(listSecond)
    for i in range(zeros):
        listSecond.insert(0, "0")

novaLista1 = []
novaLista2 = []
for i in range(len(listSecond)):
    firstValueFirst = listFirst[i]
    firstValueSecond = listSecond[i]
    if firstValueFirst > firstValueSecond:
        novaLista1.append(firstValueFirst)
    elif firstValueFirst < firstValueSecond:
        novaLista2.append(firstValueSecond)
    else:
        novaLista1.append(firstValueFirst)
        novaLista2.append(firstValueSecond)


if len(novaLista1) != 0:
    numeroFinal1 = int(''.join(novaLista1))
else:
    numeroFinal1 = -1

if len(novaLista2) != 0:
    numeroFinal2 = int(''.join(novaLista2))
else:
    numeroFinal2 = -1

valoresFinais = sorted([numeroFinal1, numeroFinal2])
print(f"{valoresFinais[0]} {valoresFinais[1]}")


