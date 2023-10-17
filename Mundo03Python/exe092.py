ficha = dict()

ficha['nome'] = str(input('Nome: '))
ano = int(input('Ano de Nascimento: '))
ficha['idade'] = 2018 - ano
ficha['ctps'] = int(input('Carteira de Trabalho (0 se não houver): '))

if ficha['ctps'] != 0:
    contrat = int(input('Ano de Contratação: '))
    ficha['contratação'] = contrat
    ficha['salario'] = float(input('Salário: '))
    ficha['aposentadoria'] = (contrat + 35) - ano

print(ficha)
for k, v in ficha.items():
    print(f'  >> {k} tem valor {v}')
