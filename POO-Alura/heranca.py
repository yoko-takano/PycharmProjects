import abc

class Funcionario(abc.ABC):

    def __init__(self, nome, cpf, salario):
        self._nome = nome
        self._cpf = cpf
        self._salario = salario

    @abc.abstractmethod
    def getBonificacao(self):
        pass


class AutenticavelMixIn:
    def autentica(self,senha):
        if self._senha == senha:
            print("acesso permitido")
            return True
        else:
            print("acesso negado")
            return False

class Gerente(Funcionario, AutenticavelMixIn):
    def __init__(self, nome, cpf, salario, senha, qntdFuncionarios):
        super().__init__(nome, cpf, salario)
        self._senha = senha
        self._qntdFuncionarios = qntdFuncionarios

    def getBonificacao(self):
        return self._salario * 0.15


class Diretor(Funcionario, AutenticavelMixIn):
    def __init__(self, nome, cpf, salario, senha):
        super().__init__(nome, cpf, salario)
        self._senha = senha

    def getBonificacao(self):
        return "Diretor não ganha bonificação"   


class Cliente(AutenticavelMixIn):
    def __init__(self, nome, cpf, senha):
        self._nome = nome
        self._cpf = cpf
        self._senha = senha


class ControleBonificacoes:
    def __init__(self, totalBonificacoes=0):
        self._totalBonificacoes = totalBonificacoes

    def registra(self, obj):
        try:
            self._totalBonificacoes += obj.getBonificacao()
        except AttributeError as erro:
            print(erro)

    @property
    def totalBonificacoes(self):
        return self._totalBonificacoes


class SistemaInterno:
    def login(self,obj):
        if (hasattr(obj, 'autentica')):
            print("O objeto é autenticável")
            return True
        else:
            print(f"{self.__class__.__name__} não é autenticável") 
            return False
        
