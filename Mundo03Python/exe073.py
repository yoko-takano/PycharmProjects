# 20 primeiros colocados das webtoons que eu gosto
cont1 = ('Botafogo', 'Palmeiras', 'Gremio', 'Red Bull Bragantino', 'Fluminence')
cont2 = ('CA Paranaense', 'Flamengo', 'Fortaleza', 'Atlético Mineiro', 'Cuiabá Esporte Clube')
cont3 = ('Cruzeiro', 'Internacional', 'Sao Paulo FC', 'Corinthians', 'Goiás EC')
cont4 = ('Bahia', 'Santos FC', 'Vasco Gama', 'América FC', 'Coritiba')
contagem = cont1 + cont2 + cont3 + cont4

print('~~x'*20)
print(f'Lista de times do Brasileirão: {contagem}')
print('~~x'*20)
print(f'Os cinco primeiros são: {contagem[0:5]}')
print('~~x'*20)
print(f'Os 4 últimos são: {contagem[-4:]}')
print('~~x'*20)
print(f'Times em ordem alfabética: {sorted(contagem)}')
print('~~x'*20)
for pos, time in enumerate(contagem): # pos - posição na tupla | time - nome do time
    if contagem[pos] == 'Flamengo':
        print(f'O time {time} está na {pos+1}° posição.')

print(f'O Flamengo está na {contagem.index("Flamengo")+1}° posição')