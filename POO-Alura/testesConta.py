from conta import Conta
from conta import Cliente
from modificadores import Pessoa
from conta import ContaCorrente
from conta import ContaPoupanca
from conta import AtualizadorContas
from conta import ContaInvestimento
from excessoes import SaldoInsuficienteError

cc = ContaCorrente('434-1', 'Renan', 1000.0)
cp = ContaPoupanca('111-0', 'Tatsuya', 1000.0)
ci = ContaInvestimento('125-5', 'Tatsuya', 1000.00)

valor = -5000.00

try: 
    cc.saca(valor)
    print(f'Saque de {valor} realizado com sucesso.')
except ValueError:
    print('O valor a ser sacado deve ser um número positivo.')
except SaldoInsuficienteError:
    print('Você não possui saldo suficiente para concluir esta operação.')


try: 
    cc.deposita(valor)
    print(f"Depósito de {valor} realizado com sucesso.")
except ValueError:
    print(f"O valor a ser depositado deve ser um número positivo.")


# cc.atualiza(0.01)
# cp.atualiza(0.01)

# ci.deposita(1000.00)
# ci.atualiza(0.01)

# print(cc.saldo)
# print(cp.saldo)
# print(ci.saldo)

# adc = AtualizadorContas(0.01)
# adc.roda(cc)
# adc.roda(cp)
# print(f"Saldo Total: {adc._saldoTotal}")

# conta1.saldo = -300
# print(conta1.get_total_contas())
# print(conta3.get_total_contas())
# conta1.deposita(100)
# conta1.saca(50)
# conta1.transfere(conta2, 30)
# conta1.extrato()

# conta1._historico.imprime()
# conta2._historico.imprime()
# pessoa = Pessoa(28)
# print(pessoa._Pessoa__idade)
# pessoa._Pessoa__idade = 25
# print(pessoa._Pessoa__idade)
