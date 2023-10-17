acum = 0
maior = 0
cont = 1
precobarato = 0
prodbarato = 0

while True:
    nome = str(input('Nome do produto: '))
    preco = float(input('Preço do produto: R$'))
    acum += preco
    if preco >= 1000:
        maior += 1
    if cont == 1:
        prodbarato = nome
        precobarato = preco
    else:
        if preco < precobarato:
            precobarato = preco
            prodbarato = nome
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
    cont += 1

print(f'O total da compra foi R${acum:.2f}')
print(f'Temos {maior} produtos custando acima de R$1000.00')
print(f'O produto mais barato foi o/a {prodbarato} que custou R${precobarato:.2f}.')
