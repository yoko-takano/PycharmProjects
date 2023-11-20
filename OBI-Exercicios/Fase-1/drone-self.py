# Inputs
A = int(input("Dimensão A da caixa: "))
B = int(input("Dimensão B da caixa: "))
C = int(input("Dimensão C da caixa: "))
altura = int(input("Altura da janela: "))
largura = int(input("Largura da janela: "))

# Desenvolvimento
dimCaixa = [A, B, C]
dimCaixa = sorted(dimCaixa)
dimJanela = [altura, largura]
dimJanela = sorted(dimJanela)

# Outputs
if dimCaixa[0] <= dimJanela[0] and dimCaixa[1] <= dimJanela[1]:
    print("Sim")
else:
    print("Não")
