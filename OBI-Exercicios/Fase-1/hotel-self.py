d = int(input("Valor da diária com desconto: "))
a = int(input("Valor de acréscimo na diária: "))
n = int(input("Dia de chegada no hotel: "))


if n < 16:
    d = d + (a*(n-1))
else:
    d = d + (a*14)

valorFinal = d*(31-(n-1))
print(valorFinal)
