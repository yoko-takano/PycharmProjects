resumo = {}
resumo['nome'] = str(input('Nome: '))
resumo['media'] = float(input(f'Média de {resumo["nome"]}: '))

if resumo['media'] >= 7:
    resumo['situação'] = 'APROVADO'
elif 5 <= resumo['media'] < 7:
    resumo['situação'] = 'RECUPERAÇÃO'
else:
    resumo['situação'] = 'REPROVADO'

for k, v in resumo.items():
    print(f' >> {k} é igual a {v}.')