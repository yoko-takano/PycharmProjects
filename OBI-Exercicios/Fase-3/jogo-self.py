from random import randint

x = randint(-10000, 10000)
print(x)

cont = 1
bet = int(input(f"Digite sua {cont}° tentativa: "))
while bet != x:
    if bet < x:
        print("É maior")
    else:
        print("É menor")
    cont += 1
    bet = int(input(f"Digite sua {cont}° tentativa: "))

print(f"Você acertou em {cont} tentativa(s)!")
