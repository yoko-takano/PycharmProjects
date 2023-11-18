numero = int(input("Digite a quantidade de números: "))

if numero >= 5:
    maoEsquerda = 'I'*5
    maoDireita = 'I'*(numero - 5)
    print()
elif numero >= 1:
    maoEsquerda = 'I'*numero
    maoDireita = "*"
else:
    maoEsquerda = "*"
    maoDireita = "*"

print(maoEsquerda)
print(maoDireita)