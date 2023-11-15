from exe112.utilidadescev import moeda
from exe112.utilidadescev import dado

p = dado.leiadinheiro('Digite o preço: R$')
moeda.resumo(p, 20, 12)

# Para o caso do usuário escrever (ex.: 123dasd)
# Precisa do tratamento de erro!
