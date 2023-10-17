def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')


# Programa Soma
soma(4, 5)
soma(8, 9)
soma(2, 1)
soma(b=4, a=5)


# Empacotamento + Tuplas
def contador(* núm):
    tam = len(núm)
    print(f'Recebi os valores {núm} e são ao todo {tam} números.')


contador(5, 7, 3, 1, 4)
contador(8, 4, 7)

# Lista (não precisa de empacotamento)
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)

# Programa Soma Melhorado
def soma2(* val):
    s = 0
    for num in val:
        s += num
    print(f'Somando os valores {val} temos {s}.')


soma2(5, 2)
soma2(2, 9, 4)
