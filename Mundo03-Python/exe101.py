def voto(nasc):
    # from datetime import date
    # atual = date.today().year
    resposta = 'None'
    atual = 2018
    idade = atual - nasc
    if 18 <= idade <= 70:
        resposta = f'Com {idade} anos: Voto Obrigatório'
    elif idade == 16 or idade == 17:
        resposta = f'Com {idade} anos: Voto Opcional'
    elif idade < 16:
        resposta = f'Com {idade} anos: Voto Negado'
    elif idade > 70:
        resposta = f'Com {idade} anos: Voto Opcional'
    else:
        print('Caiu aqui!')
    return resposta


entrada = int(input('Digite o ano de nascimento: '))
print(voto(entrada))