#---------- Desafio 22 ----------#
nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
lista = nome.split()
#print(lista)
junto = ''.join(lista)
#print(junto)
print('Seu nome tem ao todo {} letras'.format(len(junto)))
print('Seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))
print('Seu primeiro nome é {} e tem {} letras'.format((lista[0]), len(lista[0])))

#---------- Desafio 23 ----------#
numero = str(input('Digite um número de 0 a 9999: '))
qntd = len(numero)
lista = numero.split()
print(qntd, lista)

# u = numero//1%10
# d = numero//10%10
# c = numero//100%10
# m = numero//1000%10

if qntd == 4:
    unidade = numero[3]
    dezena = numero[2]
    centena = numero[1]
    milhar = numero[0]
    print('Unidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}'.format(unidade, dezena, centena, milhar))
elif qntd == 3:
    unidade = numero[2]
    dezena = numero[1]
    centena = numero[0]
    milhar = 0
    print('Unidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}'.format(unidade, dezena, centena, milhar))
elif qntd == 2:
    unidade = numero[1]
    dezena = numero[0]
    centena = 0
    milhar = 0
    print('Unidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}'.format(unidade, dezena, centena, milhar))
elif qntd == 1:
    unidade = numero[0]
    dezena = 0
    centena = 0
    milhar = 0
    print('Unidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}'.format(unidade, dezena, centena, milhar))
else:
    print('Número permitido apenas de 0 a 9999, por favor, revisar.')

