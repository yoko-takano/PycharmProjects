import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, formato=True)}.')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, formato=True)}.')
print(f'Aumentando 10% temos {moeda.aumentar(p, 10, formato=True)}.')
print(f'Diminuindo 13% temos {moeda.diminuir(p, 13, formato=True)}.')

