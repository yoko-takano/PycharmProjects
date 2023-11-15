palavras = ('biscoito', 'chocolate', 'torta', 'bolo', 'pudim')

for c in range(0, len(palavras)):
    div = palavras[c]
    tamanho = len(div)
    print(f'Na palavra {div.upper()} temos', end=' ')
    for d in range(0, len(div)):
        letra = div[d]
        if letra.lower() in 'aeiou':
            print(f'{letra}', end=' ')
    print('')
