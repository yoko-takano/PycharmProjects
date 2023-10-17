casa = float(input('Digite o valor da casa: R$'))
salario = float(input('Digite o seu salário: R$'))
anos = float(input('Em quantos anos gostaria de pagar? '))

prestacao = casa/(anos*12)
porcentagem = salario*0.30

print('A prestação ficou em R${:.2f}, enquanto os 30% de salário é R${:.2f}.'.format(prestacao, porcentagem))

if prestacao >= porcentagem:
    print('Infelizmente, seu financiamento foi negado.')
else:
    print('Financiamento aceito! Parabéns!')
