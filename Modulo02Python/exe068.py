from random import randint
print('Vamos jogar Par ou Ímpar?')
computador = randint(1,10)
cont = 0

while True:
    jogador = int(input('Digite um valor: '))
    escolha = str(input('Par ou Ímpar? [P/I]: ')).strip()[0]
    print(f'Você jogou {jogador} e o computador jogou {computador}.')
    resultado = jogador + computador
    if resultado % 2 == 0:
        print(f'Total foi {resultado} e é par!')
        inf = 'p'
    else:
        print(f'Total foi {resultado} e é ímpar!')
        inf = 'i'
    if inf != escolha:
        print(f'Game over! Você perdeu!\nMas venceu {cont} vezes!')
        break
    cont += 1
    print(f'Parabéns, você ganhou a {cont}° rodada! Vamos jogar mais uma!')
    computador = randint(1, 10)
