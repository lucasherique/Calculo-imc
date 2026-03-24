peso = int(input('Digite o seu peso:'))
altura = float(input('Digite sua altura:'))

imc = peso / (altura ** 2)

print(f'Seu imc é de: {imc:.2f}')

if imc < 18.5:
    print('Abaixo do peso')
elif imc >= 18.5 and imc < 25:
    print('Peso normal')
elif imc >= 25 and imc < 30:
    print('Sobrepeso')
elif imc >= 30 and imc < 35:
    print('Obesidade Grau I')
elif imc >= 35 and imc < 40:
    print('Obesidade Grau II')
else:
    print('Obesidade Grau III(Mórbida)')
