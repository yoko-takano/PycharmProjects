a = float(input('Digite o primeiro valor: '))
b = float(input('Digite o segundo valor: '))
print('''
Temos as seguintes opções:
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do programa''')
cond = 0

while cond != 5:
    cond = int(input('Qual operação você quer? '))
    if cond == 1:
        print('Vamos somar! \n     >> {} + {} = {}'.format(a, b, a + b))
    elif cond == 2:
        print('Vamos multiplicar! \n     >> {} x {} = {}'.format(a, b, a*b))
    elif cond == 3:
        if a > b:
            print('Qual é o maior então? {} > {}'.format(a, b))
        elif b > a:
            print('Qual é o maior então? {} > {}'.format(b, a))
        else:
            print('Qual é o maior então? Os dois são iguais!')
    elif cond == 4:
        print('Vamos inserir novos números!')
        a = float(input('Digite o primeiro valor: '))
        b = float(input('Digite o segundo valor: '))
    elif cond == 5:
        print('Vamos finalizar então.')
    else:
        print('Por favor, digite um número válido!')
