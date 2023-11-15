def leiadinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.')
        if entrada.isalpha() or entrada.strip() == '':
            print(f'\033[0;31m\"{entrada}\" é um preço inválido!\033[m')
        else:
            valido = True
            return float(entrada)
