print(' ==== Desafio 29 ==== ')

vel = int(input('Digite a velocidade do carro: '))
multa = int((vel-80)*7)
if vel > 80:
    print(f'VOCÊ FOI MULTADO!! O valor da Multa é: R${multa}')
else:
    print('Você está no limite permitido, tenha uma boa viagem!!')