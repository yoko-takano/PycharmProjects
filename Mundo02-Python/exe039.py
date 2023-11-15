ano = int(input('Digite o ano do seu nascimento: '))
idade = 2023-ano

if idade < 18:
    print('   >> Você tem {} anos e ainda irá se alistar.'.format(idade))
    print('   >> Faltam {} anos para você se alistar.'.format(18-idade))
elif idade == 18:
    print('   >> Você tem {} anos e está na hora de se alistar!'.format(idade))
else:
    print('   >> Você tem {} anos, passou da hora de se alistar!'.format(idade))
    print('   >> Você deveria ter se alistado há {} anos.'.format(idade-18))
