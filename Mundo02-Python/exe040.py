nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1+nota2)/2

if media < 5:
    print('Sua média foi {} e você está REPROVADO!'.format(media))
elif media > 7:
    print('Sua média foi {} e você está APROVADO!'.format(media))
else:
    print('Sua média foi {} e você está em RECUPERAÇÃO.'.format(media))
