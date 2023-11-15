aprov = dict()
listagols = list()
aprov['nome'] = str(input('Nome do jogador: '))
qntd = int(input(f'Quantas partidas {aprov["nome"]} jogou? '))
cont = 0

for i in range(0, qntd):
    gol = int(input(f'Quantos gols na partida {i}? '))
    listagols.append(gol)
    aprov['gols'] = listagols[:]
    cont = cont + gol

aprov['total'] = cont
print('-='*30)
print(aprov)
print('-='*30)

for k, v in aprov.items():
    print(f'O campo {k} tem valor {v}.')

print('-='*20)
print(f'O jogador {aprov["nome"]} jogou {qntd} partidas.')

for x in range(0, qntd):
    print(f'   => Na partida {x}, fez {aprov["gols"][x]} gols.')
print(f'Foi um total de {cont} gols.')

