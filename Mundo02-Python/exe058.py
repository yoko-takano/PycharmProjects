from random import randint
computador = randint(1,10)

print('Sou seu computador...\nAcabei de pensar em um número entre 0 e 10.\nSerá que você consegue advinhar qual foi?')
jogadas = 1
jogador = int(input('Tente advinhar qual o número: \n{}° Tentativa: '.format(jogadas)))

while computador != jogador:
    if jogador > computador:
        print('Menos... Tente mais uma vez.')
    elif jogador < computador:
        print('Mais... Tente mais uma vez.')
    jogadas += 1
    jogador = int(input('{}° Tentativa: '.format(jogadas)))

print('Parabéns, o número foi {} e você acertou em {} tentativas!'.format(computador, jogadas))
