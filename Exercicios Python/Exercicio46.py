print(' ==== Desafio 46 ==== ')

import random
from time import sleep

print('-=-=-=-=-=-=-JOKENPÔ-=-=-=-=-=-=-')
print('JOGUE CONTRA MIM!!!')
print('''ESCOLHA UMA OPÇÃO PARA JOGAR!
[1] PEDRA
[2] PAPEL 
[3] TESOURA ''')


jogador = int(input('Faça sua escolha: '))
lista = [1, 2, 3]
oponente = random.choice(lista)

print('JO')
sleep(0.8)
print('KEN')
sleep(0.8)
print('PO!!!')
sleep(0.8)

if jogador == 1:
    if oponente == 1:
        print('\033[:33mAmbos escolheram PEDRA, O JOGO EMPATOU!!!')
    elif oponente == 2:
        print('\033[:31mEu escolhi PAPEL e você PEDRA, EU VENCI!!!')
    else:
        print('\033[:32mVocê escolheu PEDRA e eu TESOURA, VOCÊ VENCEU!!!')

elif jogador == 2:
    if oponente == 1:
        print('\033[:32mVocê escolheu PAPEL e eu PEDRA, VOCÊ VENCEU!!!')
    elif oponente == 2:
        print('\033[:33mAmbos escolheram PAPEL, O JOGO EMPATOU!!!')
    else:
        print('\033[:31mVocê escolheu PAPEL e eu TESOURA, EU VENCI!!!')

elif jogador == 3:
    if oponente == 1:
        print('\033[:31mVocê escolheu TESOURA e eu PEDRA, EU VENCI!!!')
    elif oponente == 2:
        print('\033[:32mVocê escolheu TESOURA e eu PAPEL, VOCÊ VENCEU!!!')
    else:
        print('\033[:33mAmbos escolheram TESOURA, O JOGO EMPATOU!!!')

else:
    print('\033[:31mOPÇÃO INVÁLIDA, TENTE NOVAMENTE!!')
