inicial = int(input("Quantidade de megabytes: "))
meses = int(input("Quantidade de meses: "))
acumula = inicial

for i in range(meses):
    gasto = int(input(f"Gasto no {i+1}° mês: "))
    saldo = acumula - gasto
    acumula = inicial + saldo

print(f"No próximo mês, tera {acumula} de saldo!")
