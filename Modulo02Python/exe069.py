cont_idade = 0
cont_homi = 0
cont_mul = 0
while True:
    print('~xx'*20)
    print('Cadastre uma pessoa:')
    idade = int(input('Diga a idade: '))
    sexo = str(input('Digite o sexo [F/M]: ')).strip().upper()[0]
    print('~xx' * 20)
    while sexo != 'F' and sexo != 'M':
        sexo = str(input('Digite o sexo [F/M]: ')).strip().upper()[0]
    if idade > 18:
        cont_idade += 1
    if sexo in 'Mm':
        cont_homi += 1
    if sexo in 'Ff' and idade < 20:
        cont_mul += 1
    flag = input('Quer continuar? [S/N]: ').strip().upper()[0]
    if flag == 'N':
        break
    elif flag != 'S':
        while flag != 'N' and flag != 'S':
            flag = input('Quer continuar? [S/N]: ').strip().upper()[0]

print('~xx' * 20)
print('Fim do programa!')
print(f'Total de pessoas com mais de 18 anos foi {cont_idade}.')
print(f'Total de homens cadastrados foi {cont_homi}.')
print(f'Temos {cont_mul} mulheres com menos de 20 anos.')

# uma ideia:
# while resp not in 'SN'