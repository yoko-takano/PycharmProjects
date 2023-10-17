from datetime import date
atual = date.today().year
velho = 0
novo = 0
for c in range(1, 6):
    ano = int(input('Em que ano a {}° pessoa nasceu? '.format(c)))
    idade = atual - ano
    if idade >= 21:
        velho += 1
    elif idade < 21:
        novo += 1
    else:
        print('Erro. Verificar!')

print('Ao todo, tivemos {} pessoas maiores de idade.'.format(velho))
print('E também tivemos {} pessoas menores de idade.'.format(novo))
