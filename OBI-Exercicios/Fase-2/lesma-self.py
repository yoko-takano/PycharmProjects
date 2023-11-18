altura = int(input("Digite a altura do muro: "))
desloc = int(input("Digite a distância de deslocamento: "))
retorno = int(input("Digite a distância de retorno: "))
final = 0
cont = 0

while final < altura:
    final += desloc
    if final != altura:
        final -= retorno
    cont += 1

print(cont)