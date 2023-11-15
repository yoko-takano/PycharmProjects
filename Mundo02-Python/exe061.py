print('='*20)
print('10 termos de uma PA')
print('='*20)

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
c = 1

while c != 11:
    print(primeiro, end=' → ')
    primeiro = primeiro + razao
    c += 1

print('Fim!')
