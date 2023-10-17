preco = float(input('Qual o preço do produto: R$'))
print('Você quer pagar em dinheiro/cheque ou no cartão?')
print('''    [1] Dinheiro/Cheque
    [2] Cartão''')
cond0 = int(input('Digite o número: '))

if cond0 == 1:
    precofim = preco*0.90
    print('Você escolheu pagar no dinheiro/cheque.')
    print('Você ganhou 10% de desconto!')
    print('Valor final de R${:.2f}.'.format(precofim))
elif cond0 == 2:
    cond1 = int(input('Em quantas vezes você quer parcelar? '))
    if cond1 == 1:
        precofim = preco*0.95
        print('Você escolheu pagar a vista no cartão.')
        print('Você ganhou 5% de desconto!')
        print('Valor final de R${:.2f}.'.format(precofim))
    elif cond1 == 2:
        precofim = preco
        print('Você escolheu pagar em até 2x no cartão.')
        print('Sem descontos e sem juros.')
        print('Valor final de R${:.2f}.'.format(precofim))
    elif cond1 >= 3:
        precofim = preco*1.20
        print('Você escolheu parcelar em {}x no cartão.'.format(cond1))
        print('Tem 20% de juros na sua compra.')
        print('Valor final de R${:.2f}, juros totais de R${:.2f}.'.format(precofim, precofim-preco))
        print('As parcelas ficaram em R${:.2f}/mês com juros.'.format(precofim/cond1))
else:
    print('Por favor, digite um número válido!')

#dinheiro/cheque - 10% de desconto
#a vista no cartão - 5% de desconto
#em até 2x no cartão - preço normal
#3x ou mais no cartão - 20% de juros