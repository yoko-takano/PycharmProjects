listaEntrada = []
qntd = int(input("Digite quantos números serão na sequência: "))
print("Digite os valores da sequência:")

for i in range(qntd):
    valor = int(input())
    listaEntrada.append(valor)
print(listaEntrada)

comparativo = 1
seq = 1
for numero in listaEntrada:
    if numero != comparativo:
        comparativo = numero
        seq += 1

print(f"Números em sequência: {seq}")
