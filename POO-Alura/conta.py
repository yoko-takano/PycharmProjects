import datetime
import abc
from excessoes import SaldoInsuficienteError

class Conta(abc.ABC):
    _total_contas = 0
    __slots__ = ['_numero', '_titular', '_saldo', '_limite', '_historico', '_taxa']

    def __init__(self, numero, cliente, saldo, taxa=0, limite=1000):
        Conta._total_contas += 1
        self._numero = numero
        self._titular = cliente
        self._saldo = saldo
        self._limite = limite
        self._taxa = taxa
        self._historico = Historico()

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, saldo):
        if saldo < 0:
            print('Saldo não pode ser negativo')
        else:
            self._saldo = saldo

    @classmethod
    def get_total_contas(cls):
        return cls._total_contas

    def deposita(self, valor):
        if valor < 0:
            raise ValueError('Não existe essa de depositar um valor negativo!')
        else:
            self._saldo += valor

    def saca(self, valor):
        if valor < 0:
            raise ValueError('Você tentou sacar um valor negativo')
        if (self._saldo < valor):
            raise SaldoInsuficienteError('Saldo insuficiente')
        self._saldo -= valor
        print("Saque/transferência realizada com sucesso")

    def extrato(self):
        print(f'Número: {self._numero}\nSaldo: {self._saldo}')
        self._historico.transacoes.append(f'tirou extrato - saldo de {self._saldo}')

    def transfere(self, destino, valor):
        retirou = self.saca(valor)
        if not retirou:
            return False
        else:
            destino.deposita(valor)
            self._historico.transacoes.append(f'transferência de {valor} para conta {destino._numero}.')
            return True

    @abc.abstractmethod
    def atualiza(self, taxa):
        pass

    def __str__(self):
        return f"Dados da Conta: \nNumero: {self._numero}\nTitular: {self._titular}\nSaldo: {self._saldo}\nLimite:{self._limite}"


class TributavelMixIn:
    def getValorImposto(self):
        pass


class Cliente:
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf


class Historico:
    def __init__(self):
        self.data_abertura = datetime.datetime.today()
        self.transacoes = []

    def imprime(self):
        print(f'data abertura: {self.data_abertura}')
        print('transações:')
        for t in self.transacoes:
            print('-', t)


class ContaCorrente(Conta, TributavelMixIn):
    def atualiza(self, taxa):
        self._saldo += self._saldo * 2 * taxa
        return self._saldo
    def deposita(self, valor):
        if valor < 0:
            raise ValueError('Você tentou depositar um valor negativo')
        else:
            self._saldo += (valor - 0.10)
    def getValorImposto(self):
        return self._saldo * 0.01
    def saca(self, valor):
        if valor < 0:
            raise ValueError('Você tentou sacar um valor negativo')
        if self._saldo < valor:
            raise SaldoInsuficienteError('Saldo insuficiente')
        self._saldo -= (valor + .10)


class ContaPoupanca(Conta):
    def atualiza(self, taxa):
        self._saldo += self._saldo * 3 * taxa
        return self._saldo


class SeguroDeVida(TributavelMixIn):
    def __init__(self, valor, titular, numero_apolice):
        self._valor = valor
        self._titular = titular
        self._numeroApolice = numero_apolice

    def getValorImposto(self):
        return 50 + (self._valor * 0.05)

class AtualizadorContas:
    def __init__(self, selic, saldoTotal = 0):
        self._selic = selic
        self._saldoTotal = saldoTotal
    def roda(self,conta):
        print (f"Saldo da Conta: {conta._saldo}")
        self._saldoTotal += conta.atualiza(self._selic)
        print(f"Saldo Final: {self._saldoTotal}")


class ContaInvestimento(Conta):
    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 5