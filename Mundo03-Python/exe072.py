cont1 = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')
cont2 = ('onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
contagem = cont1 + cont2

usuario = int(input('Digite um número entre 0 e 20: '))

while usuario < 0 or usuario > 20:
    usuario = int(input('Tente novamente. Digite um número entre 0 e 20: '))

print(f'Você digitou o número {contagem[usuario]}.')
