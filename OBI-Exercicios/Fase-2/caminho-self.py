n = int(input("Número de postes: "))
lista = []
for i in range(n):
    pot = int(input(f"Digite a potência da {i+1}° lâmpada: "))
    lista.append(pot)

lista.append(lista[0])
anterior = lista[0]
resultado = []

for i in range(1, n+1):
    print(f"{i}° Interação:")
    posterior = lista[i]
    soma = anterior + posterior
    if soma < 1000:
        resultado.append(1)
    else:
        resultado.append(0)
    anterior = posterior

print(resultado)
contagemAtual = 0
maxContagem = 0
for elemento in resultado:
    if elemento == 1:
        contagemAtual += 1
        maxContagem = max(maxContagem, contagemAtual)
    else:
        contagemAtual = 0

print(maxContagem)