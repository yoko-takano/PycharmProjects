clientes = int(input("Digite o número de clientes: "))
vagas = []

print("Digite o plano de estacionamento:")
for i in range(clientes):
    plano = int(input())
    vagas.append(plano)

cont = 0
sequencia = []
for numeracao in vagas:
    if numeracao not in sequencia:
        cont += 1
    sequencia.append(numeracao)

print(cont)
# if numero in lista: print("Está aqui)