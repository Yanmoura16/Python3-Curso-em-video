print(' ==== Desafio 44 ==== ')

peso = float(input('Digite seu peso em (kg): '))
altura = float(input('Digite sua altura em (m): '))
imc = peso / (altura**2)

if imc <= 18.5:
    print(f'Seu IMC é: {imc:.1f}, \nVocê está abaixo do seu Peso Ideal')
elif imc <= 25:
    print(f'Seu IMC é: {imc:.1f}, \nVocê está no seu Peso Ideal')
elif imc <= 30:
    print(f'Seu IMC é: {imc:.1f}, \nVocê está com Sobrepeso')
elif imc <= 40:
    print(f'Seu IMC é: {imc:.1f}, \nVocê está com Obesidade')
else:
    print(f'Seu IMC é: {imc:.1f}, \nVocê está com Obesidade Mórbida')
