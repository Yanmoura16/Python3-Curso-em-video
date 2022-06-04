print(' ===== Desafio 69 ===== ')

from random import randint

while True:
    num = int(input('Digite um numero: '))

    if num < 0:
        break

    escolha = input('PAR ou IMPAR? [P/I] ').strip()
    numpc = randint(0, 9)
    total = num + numpc

    if escolha in 'Ii' and total % 2 != 0:
        print('Você escolheu IMPAR e GANHOU!! ')
        print(f'Eu escolhi: {numpc} e você: {num} \n'
              f'No total deu: {total}')
    elif escolha in 'Ii' and total % 2 == 0:
        print('Você escolheu IMPAR e PERDEU!!')
        print(f'Eu escolhi: {numpc} e você: {num} \n'
              f'No total deu: {total}')
    elif escolha in 'Pp' and total % 2 == 0:
        print('Você escolheu PAR e GANHOU!!')
        print(f'Eu escolhi: {numpc} e você: {num} \n'
              f'No total deu: {total} que é um numero PAR')
    else:
        print('Você escolheu PAR e PERDEU!!')
        print(f'Eu escolhi: {numpc} e você: {num} \n'
              f'No total deu: {total} que é um numero IMPAR')

print('JOGO ENCERRADO')
