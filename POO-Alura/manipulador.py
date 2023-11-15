from conta import ContaCorrente, SeguroDeVida, TributavelMixIn


class ManipuladorDeTributaveis:

    def calculaImpostos(self, listaTributaveis):
        total = 0
        for t in listaTributaveis:
            total += t.getValorImposto()
        
        return total
    

cc1 = ContaCorrente('123-4', 'Yoko', 1000.00)
cc2 = ContaCorrente('132-4', 'Renan', 1000.00)
seguro1 = SeguroDeVida(100.00, 'Renan', '345-77')
seguro2 = SeguroDeVida(200.00, 'Maria', '237-98')

listaTributaveis = []
listaTributaveis.append(cc1)
listaTributaveis.append(cc2)
listaTributaveis.append(seguro1)
listaTributaveis.append(seguro2)
print(listaTributaveis)
manipulador = ManipuladorDeTributaveis()
total = manipulador.calculaImpostos(listaTributaveis)
print(total)