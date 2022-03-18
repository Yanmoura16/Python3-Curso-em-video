print(' ==== Desafio 31 ==== ')

km = float(input('Digite a distância da sua viagem: '))

if km >= 200:
    print(f'O valor da passagem é: R${km * 0.45:.2f}')
else:
    print(f'O Valor da passagem é: R${km * 0.50:.2f}')