peso = float(input('Digite seu peso (kg): '))
altura = float(input('Digite a altura (m): '))
imc = peso/(altura**2)

if imc <= 18.5:
    print('Abaixo do peso, seu IMC é {:.2f}.'.format(imc))
elif 18.5 < imc <= 25:
    print('Peso ideal, seu IMC é {:.2f}.'.format(imc))
elif 25 < imc <= 30:
    print('Sobrepeso, seu IMC é {:.2f}.'.format(imc))
elif 30 < imc <= 40:
    print('Obseidade, seu IMC é {:.2f}.'.format(imc))
elif imc > 40:
    print('Obesidade mórbida, seu IMC é {:.2f}.'.format(imc))
