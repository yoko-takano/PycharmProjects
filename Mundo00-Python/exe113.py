def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print('\033[31mErro! Por favor, digite um número inteiro válido.\033[m')
            continue  # retorna ao while
        except KeyboardInterrupt:
            print('\n\033[31mEntrada de dados interrompidas pelo usuário.\033[m')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro! Por favor, digite um número inteiro válido.\033[m')
            continue  # retorna ao while
        except KeyboardInterrupt:
            print('\n\033[31mEntrada de dados interrompidas pelo usuário.\33[m')
            return 0
        else:
            return n


num1 = leiaInt('Digite um inteiro: ')
num2 = leiaFloat('Digite um real: ')
print(f'O valor inteiro digitado foi {num1} e o real foi {num2}.')
