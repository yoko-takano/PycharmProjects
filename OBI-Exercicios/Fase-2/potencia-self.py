qntd = int(input("Quantos números serão? "))

soma = 0
for i in range(qntd):
    entrada = int(input(f"Digite o {i}° número: "))
    numero = entrada // 10
    potencia = entrada % 10
    resultado = numero**(potencia)
    soma += resultado


print(f"Resultado {soma}")