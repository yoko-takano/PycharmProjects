principal = str(input("Digite a primeira carta: "))
naipe = principal[1]
valorSoma = []

for i in range(2):
    cont = 0
    for j in range(3):
        carta = str(input(f"Digite a {j + 1}° carta do {i + 1}° jogador: "))
        primeiro = carta[0]  # Ás, Valete, Dama e Rei
        segundo = carta[1]  # Naipe

        if primeiro == "A":
            if segundo == naipe:
                cont += 14
            else:
                cont += 10

        elif primeiro == "J":
            if segundo == naipe:
                cont += 15
            else:
                cont += 11

        elif primeiro == "Q":
            if segundo == naipe:
                cont += 16
            else:
                cont += 12
        elif primeiro == "K":
            if segundo == naipe:
                cont += 17
            else:
                cont += 13
    valorSoma.append(cont)

print(valorSoma)
if valorSoma[0] > valorSoma[1]:
    print("Luana")
elif valorSoma[1] < valorSoma[1]:
    print("Edu")
else:
    print("Empate")
