from random import randint
from time import sleep
from operator import itemgetter

jogadores = {'jogador1': randint(1, 6),
             'jogador2': randint(1, 6),
             'jogador3': randint(1, 6),
             'jogador4': randint(1, 6)}
ranking = {}

print('Valores sorteados:')
sleep(1)

for i, j in jogadores.items():
    print(f'O {i} tirou {j}')
    sleep(1)
print('-=' * 20)
print(' >> Ranking dos Jogadores <<')
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
for v, k in enumerate(ranking):
    print(f' {v+1}° lugar: {k[0]} com {k[1]}.')
