import string

alfabeto = list(string.ascii_lowercase)
print(alfabeto)
remover = ['k', 'w', 'y']
for letra in alfabeto:
    if letra in remover:
        alfabeto.remove(letra)
qntd = len(alfabeto)

cont = 0
frase = list(str(input("Digite a frase: ")))
for letra in alfabeto:
    for i in range(len(frase)):
        if letra == frase[i]:
            cont += 1
            break

if qntd == cont:
    print("S")
else:
    print("N")