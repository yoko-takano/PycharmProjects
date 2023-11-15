from conta import ContaCorrente

def metodo1():
    print('inicio do Método 1')
    metodo2()
    print('fim do Método 1')

def metodo2():
    print('inicio do Método 2')
    cc = ContaCorrente('123-4', 'Yoko', 0)
    try:
        for i in range(1,15):
            cc.deposita(i + 1000)
            print(cc.saldo)
            if (i==5):
                cc = None
    except:
        print('erro')
    print('fim do Método 2')


print('início do main')
metodo1()
print('fim do main')