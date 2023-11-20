# imputs
tamanho = int(input("Digite o tamanho da sequência: "))
alturas = [int(tamanho) for tamanho in input().split()]

# Desenvolvimento
cont = 0
for i in range(1, tamanho-1):
    anterior = alturas[i-1]
    meio = alturas[i]
    posterior = alturas[i+1]
    if anterior > meio and meio < posterior:
        cont += 1

# Outputs
if cont == 0:
    print("Não")
else:
    print("Sim")
