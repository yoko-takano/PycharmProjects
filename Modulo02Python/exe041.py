ano = int(input('Digite seu ano de nascimento: '))
idade = 2023-ano

if idade <= 9:
    print('Sua idade é {} e sua categoria é MIRIM.'.format(idade))
elif 9 < idade <= 14:
    print('Sua idade é {} e sua categoria é INFANTIL.'.format(idade))
elif 14 < idade <= 19:
    print('Sua idade é {} e sua categoria é JUNIOR.'.format(idade))
elif 19 < idade <= 20:
    print('Sua idade é {} e sua categoria é SÊNIOR.'.format(idade))
else:
    print('Sua idade é {} e sua categoria é MASTER.'.format(idade))
