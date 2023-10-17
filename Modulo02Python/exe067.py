
while True:
    valor = int(input('Quer ver a tabuada de qual valor? '))
    print('~='*16)
    if valor < 0:
        break
    for c in range(1, 11):
        print(f'{valor} X {c} = {valor*c}')
    print('~=' * 16)
print('Programa da Tabuada encerrado! Volte sempre.')