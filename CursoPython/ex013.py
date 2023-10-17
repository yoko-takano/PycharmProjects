import random
nome1 = str(input('Primeiro aluno: '))
nome2 = str(input('Segundo aluno: '))
nome3 = str(input('Terceiro aluno: '))
nome4 = str(input('Quarto aluno: '))
lista = [nome1, nome2, nome3, nome4]
sorteado = random.choice(lista)
print('O aluno escolhido foi {}.\n'.format(sorteado))

random.shuffle(lista)
print('A ordem de apresentação será: ')
print(lista)
