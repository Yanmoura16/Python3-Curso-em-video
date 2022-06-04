print(' ===== Desafio 59 ===== ')

import random

cont = 0
num = random.randint(0, 10)

print('\033[7m===== Olá vamos jogar um jogo da adivinhação? ===== \033[m ')
escolha = int(input('Escolha um numero de 0 a 10: '))
print('===================================================')

while escolha != num:
    print('\033[:31m Você escolheu um numero diferente do meu \033[m')
    print(f'Sua escolha foi: {escolha}')
    print(f'Minha escolha foi: {num}')
    print('Vamos jogar novamente')
    print('===================================================')
    cont += 1
    escolha = int(input('Escolha um numero de 0 a 10: '))

print(f'\033[:32m Parabéns você escolheu o mesmo numero que eu, Nossa escolha foi: {escolha}')
print(f' Você acertou na {cont+1}° tentativa')


