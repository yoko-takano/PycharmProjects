# modo padrão de resolução
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]

if inverso == junto:
    print('A frase é um palindromo!')
else:
    print('A frase digitada não é um palíndromo.')

print('O inverso de {} é {}'.format(junto, inverso))

# só da pra fazer pelo python
letra = 0
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]

if inverso == junto:
    print('A frase é um palindromo!')
else:
    print('A frase digitada não é um palíndromo.')

print('O inverso de {} é {}'.format(junto, inverso))