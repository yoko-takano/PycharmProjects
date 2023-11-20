# ENTRADA
tamanho = int(input("Tamanho do vetor: "))
inicio = int(input("Digite o valor mínimo da soma: "))
fim = int(input("Digite o valor máximo da soma: "))
print("Digite os valores do vetor: ")
vetor = [int(tamanho) for tamanho in input().split()]

# PRINCIPAL
cont = 0
for i in range(tamanho):
    for j in range(tamanho):
        if i != j:
            soma = vetor[i] + vetor[j]
            if inicio <= soma <= fim:
                cont += 1

# SAIDA
if cont > 0:
    print(int(cont/2))
else:
    print(0)
