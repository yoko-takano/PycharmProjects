teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)

galera2 = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera2[0][0])
print(galera2[1][1])

for p in galera2:
    print(f'{p[0]} tem {p[1]} anos de idade.')

galera3 = list()
dado = list()
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera3.append(dado[:])
    dado.clear()

print(galera3)
totmai = 0
totmen = 0
for x in galera3:
    if x[1] >= 21:
        print(f'{x[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{x[0]} é menor de idade.')
        totmen += 1

print(f'Temos {totmai} maiores e {totmen} menores de idade.')