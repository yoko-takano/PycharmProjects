resultado = int(input("Digite a pontuação do atleta: "))
recordeMundial = int(input("Digite o recorde mundial: "))
recordeOlimpico = int(input("Digite o recorde olímpico: "))

if resultado >= recordeMundial:
    print("*")
else:
    print("RM")

if resultado >= recordeOlimpico:
    print("*")
else:
    print("RO")