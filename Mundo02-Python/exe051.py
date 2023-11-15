print('='*20)
print('10 termos de uma PA')
print('='*20)

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razao

for c in range(primeiro, decimo + razao, razao):
    print(c, end=' → ')

print('Fim!')