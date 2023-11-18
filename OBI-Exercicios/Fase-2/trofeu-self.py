
lista = []
for i in range(1, 6):
    nota = int(input(f"Digite a nota do {i} aluno: "))
    lista.append(nota)

primeiraMaior = lista[0]
segundaMaior = 0
contPrimeira = 0
contSegunda = 0

for nota in lista:
    if nota == primeiraMaior:
        contPrimeira += 1

for nota in lista:
    if primeiraMaior != nota:
        segundaMaior = nota
        break
    else:
        segundaMaior = 0

for nota in lista:
    if nota == segundaMaior:
        contSegunda += 1

print(f"Primeira maior nota foi {primeiraMaior} e ganharam {contPrimeira} troféus.")
print(f"Segunda maior nota foi {segundaMaior} e ganharam {contSegunda} placas.")