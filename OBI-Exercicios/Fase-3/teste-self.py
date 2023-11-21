import random
import string

alfabeto = list(string.ascii_lowercase)
minimoRed = int(input("Digite o número mínimo de palavras: "))
maximoRed = int(input("Digite o número máximo de palavras: "))
# Tem 26 letras no alfabeto

qntdPalavras = random.randint(minimoRed, maximoRed)
listaPalavras = []

for i in range(qntdPalavras):
    listaInterna = []
    for j in range(random.randint(1, 10)):
        letra = alfabeto[random.randint(0, 25)]
        print(f"{letra}", end="")
    print(" ", end=" ")
