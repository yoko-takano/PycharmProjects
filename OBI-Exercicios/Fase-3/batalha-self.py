ataque1 = int(input("Player 1 | Ataque: "))
defesa1 = int(input("Player 1 | Defesa: "))
ataque2 = int(input("Player 2 | Ataque: "))
defesa2 = int(input("Player 2 | Defesa: "))

if defesa1 == ataque2 and defesa2 != ataque1:
    print("1")
elif defesa1 != ataque2 and defesa2 == ataque1:
    print("2")
else:
    print("-1")

