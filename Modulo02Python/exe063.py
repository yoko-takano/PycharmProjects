qntd = int(input('Quantos termos você quer ver da sequência de Fibonacci? '))
primeiro = 1
segundo = 0
cont = 0

while cont <= qntd:
    terceiro = primeiro + segundo
    print('{}'.format(terceiro), end=' → ')
    primeiro = segundo
    segundo = terceiro
    cont += 1
print('Fim!')
