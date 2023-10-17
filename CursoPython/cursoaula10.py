#------------------- exercicio 28 -------------------#
import random
chute_hum = int(input('Digite o seu chute: '))
chute_pc = random.randint(1, 5)
print(chute_hum, chute_pc)

if chute_hum == chute_pc:
    print('Parabéns, você acertou!')
else:
    print('Errou!')
print('Fim!')

#------------------- exercicio 31 -------------------#
viagem = float(input('Digite a distância da viagem: '))
if viagem <= 200:
    preco = 0.50*viagem
    print('  >> Preço da viagem foi de R$ {:.2f} para {:.2f}m de viagem'.format(preco, viagem))
    print('  >> Preço unitário de R$ 0.50/m de viagem.')
else:
    preco = 0.45*viagem
    print('  >> Preço da viagem foi de R$ {:.2f} para {:.2f}m de viagem.'.format(preco, viagem))
    print('  >> Preço unitário de R$ 0.45/m de viagem.')
print('Fim!')

#------------------- exercicio 35 -------------------#
print('-='*20)
print('Analisador de Triângulos')
print('-='*20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1<r2+r3 and r2<r1+r3 and r3<r1+r2:
    print('Os segmentos acima PODEM FORMAR um triângulo.')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo')
print('Fim! ')