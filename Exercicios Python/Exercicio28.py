print(' ==== Desafio 28 ==== ')
import random

numero = random.randint(0,5)
escolha = int(input('Escolha um número de 0 a 5: '))

if numero == escolha:
    print(f'O número que eu escolhi foi: {numero} e sua escolha também foi: {escolha} \n PARABÉNS VOCÊ ACERTOU!!')
else:
    print(f'O número que eu escolhi foi: {numero} e sua escolha foi: {escolha} \n Infelizmente você perdeu :( ')

