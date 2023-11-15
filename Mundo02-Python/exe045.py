from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('''Suas opções:
[0] Pedra
[1] Papel
[2] Tesoura''')
jogador = int(input('Qual é a sua jogada? '))

print('Então vamos lá! Prepare-se...')
print('Pedra')
sleep(1)
print('Papel')
sleep(1)
print('Tesouraaa!')
sleep(1)

print('~='*20)
print('Computador jogou {}.'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('~='*20)

if computador == 0: #computador jogou pedra
    if jogador == 0: #jogador jogou pedra
        print('Empate! Vamos de novo?')
    elif jogador == 1: #jogador jogou papel
        print('Parabéns! Você venceu!')
    elif jogador == 2: #jogador jogou tesoura
        print('Poxa! Você perdeu...')
elif computador == 1: #computador jogou papel
    if jogador == 0: #jogador jogou pedra
        print('Poxa! Você perdeu...')
    elif jogador == 1: #jogador jogou papel
        print('Empate! Vamos de novo?')
    elif jogador == 2: #jogador jogou tesoura
        print('Parabéns! Você venceu!')
elif computador == 2: #computador jogou tesoura
    if jogador == 0:  # jogador jogou pedra
        print('Parabéns! Você venceu!')
    elif jogador == 1:  # jogador jogou papel
        print('Poxa! Você perdeu...')
    elif jogador == 2:  # jogador jogou tesoura
        print('Empate! Vamos de novo?')
print('~='*20)



