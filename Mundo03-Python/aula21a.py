# Exemplo de docstrings:
def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c}', end='')
        c += p
    print('Fim!')


help(contador)

# Exemplo de argumentos opcionais:
def somar(a=0, b=0, c=0):
    """
    -> Faz a soma de três valores e mostra o resultado na tela.
    :param a: o primeiro valor
    :param b: o segundo valor
    :param c: o terceiro valor
    """
    s = a + b + c
    print(f'A soma vale {s}.')


somar(3, 2, 5)
somar(8, 4)
somar(c=3, a=2)


# Escopo de Variáveis
def teste():
    x = 8  # variável local, só funciona dentro da função
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')


n = 2  # variável global
print(f'No programa principal, n vale {n}')
teste()


def teste(b):
    global a
    a = 8
    b += 4
    c = 2
    print(f'"a" dentro vale {a}')
    print(f'"b" dentro vale {b}')
    print(f'"c" dentro vale {c}')


a = 5
teste(a)


# Retorno de Valores
def somar(x=0, y=0, z=0):
    s = x + y + z
    return s


soma1 = somar(3, 2, 5)
soma2 = somar(8, 4)
soma3 = somar(6)
print(f'Meus cálculos deram {soma1}, {soma2} e {soma3}.')
