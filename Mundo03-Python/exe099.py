from time import sleep


def maior(* num):
    mai = 0
    print('-=' * 35)
    print('Analisando os valores passados...')
    tam = len(num)
    for pos, x in enumerate(num):
        sleep(0.5)
        print(f'{x}', end=' ')
        if pos == 0:
            mai = x
        if x > mai:
            mai = x
    print(f'Foram informados {tam} valores ao todo.')
    print(f'O maior valor informado foi {mai}!')


# Programa Principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
