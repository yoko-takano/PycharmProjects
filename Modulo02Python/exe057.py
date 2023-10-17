#como eu fiz

sexo = str(input('Digite seu sexo [F/M]: ')).strip().upper()

if sexo != 'F' and sexo != 'M':
    while sexo != 'F' and sexo != 'M':
        sexo = str(input('Por favor, digite um sexo válido entre [F/M]: ')).strip().upper()

if sexo == 'F':
    print('Sexo feminino registrado com sucesso!')
elif sexo == 'M':
    print('Sexo masculino registrado com sucesso!')
else:
    print('Erro! Sexo inválido!')

#resolução

sexo2 = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0] #pega a primeira letra
while sexo2 not in 'MmFf':
    sexo2 = str(input('Dados inválidos! Por favor, informe seu sexo: [M/F] ')).strip().upper()[0]
print('Sexo {} registrado com sucesso!'.format(sexo2))