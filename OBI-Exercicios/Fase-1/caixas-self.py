caixaA = int(input("Tamanho da primeira caixa: "))
caixaB = int(input("Tamanho da primeira caixa: "))
caixaC = int(input("Tamanho da primeira caixa: "))

if caixaA < caixaB:
    if caixaB < caixaC:
        print(1)
    else:
        print(2)
elif caixaA > caixaB:
    if caixaB < caixaC:
        print(2)
    else:
        print(3)
else:
    if caixaB + caixaA < caixaC:
        print(1)
    else:
        print(2)
