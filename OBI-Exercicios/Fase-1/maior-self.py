n = int(input("Início do intervalo: "))  # menor valor
m = int(input("Fim do intervalo: "))  # maior valor
s = int(input("Valor da soma dos dígitos: "))

achou = 0
for i in range(m, n, -1):
    soma = 0
    tudao = str(i)
    for numero in tudao:
        soma += int(numero)
    if soma == s:
        achou = tudao
        break
    else:
        achou = -1


print(f"{achou} é o maior inteiro no intervalo [{n}][{m}]")
print(f"cuja soma dos digitos é igual a {s}.")
