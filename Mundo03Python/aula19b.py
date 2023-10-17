brasil1 = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil1.append(estado1)
brasil1.append(estado2)

print(estado1)
print(estado2)
print(brasil1)
print(brasil1[0]['uf'])
print(brasil1[1]['sigla'])

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')
for f in brasil:
    for h in f.values():
        print(h, end=' ')
    print()
