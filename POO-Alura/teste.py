def criaConta(numero, titular, saldo, limite):
    conta = {"numero": numero,
             "titular": titular,
             "saldo": saldo,
             "limite": limite}
    return conta


def deposita(conta, valor):
    conta['saldo'] += valor


def saca(conta, valor):
    conta['saldo'] -= valor


def extrato(conta):
    print(f'numero: {conta["numero"]} \nsaldo: {conta["saldo"]}')


conta1 = criaConta("123-4", "Yoko", 120, 1000)
conta2 = criaConta("431-2", "Renan", 100, 1000)
deposita(conta1, 15)
extrato(conta2)
extrato(conta1)