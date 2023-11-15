from heranca import Gerente
from heranca import Diretor
from heranca import SistemaInterno
from heranca import Cliente
from heranca import Autenticavel

diretor = Diretor('Yoko', '888.333.840-00', 10240.40, '1234')
gerente = Gerente ('Renan', '000.032.022-00', 3500.00, '1235', 3)
cliente = Cliente('Tatsuya', '990.302.854-73', '1236')

senha = Autenticavel()
sistema = SistemaInterno()
sistema.login(diretor)
sistema.login(gerente)
sistema.login(cliente)
