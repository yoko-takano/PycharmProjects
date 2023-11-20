import math
valor = int(input("Valor: "))
parcelas = int(input("Parcelas: "))

repeticaoMaior = valor % parcelas
repeticaoMenor = math.ceil(valor/parcelas) - repeticaoMaior
menorNumero = valor//parcelas


for i in range(repeticaoMaior):
    print(parcelas)

for i in range(repeticaoMenor):
    print(menorNumero)