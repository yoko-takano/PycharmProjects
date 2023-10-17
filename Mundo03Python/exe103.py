def ficha(nome='<desconhecido>', gols=0):
    resposta = f'O jogador {nome} fez {gols} gol(s) no campeonato.'
    return resposta


n = str(input('Nome do jogador: '))
g = str(input('Número de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    print(ficha(gols=g))
else:
    print(ficha(n, g))

