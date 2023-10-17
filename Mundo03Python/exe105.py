
def notas(* num, show=True):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param num: uma ou mais notas dos alunos (aceita várias)
    :param show: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma
    """
    maior = 0
    menor = 0
    cont = 0
    for pos, x in enumerate(num):
        cont += x
        if pos == 0:
            maior = x
            menor = x
        else:
            if x > maior:
                maior = x
            if x < menor:
                menor = x
    media = round(cont/(len(num)), 3)
    resultado = {'total': len(num), 'maior': maior, 'menor': menor, 'média': media}
    if show:
        if media >= 7:
            resultado['situação'] = 'boa'
        elif media < 5:
            resultado['situação'] = 'razoável'
        else:
            resultado['situação'] = 'ruim'
    return resultado


print(notas(5.5, 9.5, 10, 6.5, show=True))
print(notas(3, 1, 2.5, show=False))
print(notas(4, 8.3, 0, 5.8, 2.3, show=False))
help(notas)


def notas2(*n, sit=False):  # Modo mais fácil de resolver!
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
