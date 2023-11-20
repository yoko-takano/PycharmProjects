idadeMonica = int(input("Digite a idade da dona Mônica: "))
idadeFilho1 = int(input("Digite a idade de um dos filhos: "))
idadeFilho2 = int(input("Digite a idade do outro filho: "))
idadeFilho3 = idadeMonica - idadeFilho1 - idadeFilho2
lista = [idadeFilho1, idadeFilho2, idadeFilho3]
maisVelho = max(lista)

print(f"A idade do filho mais velho é {maisVelho}!")