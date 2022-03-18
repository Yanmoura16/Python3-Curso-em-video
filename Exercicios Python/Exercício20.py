print(' ==== Desafio 20 ==== ')

from random import sample

al1 = input('Digite o nome do primeiro aluno: ')
al2 = input('Digite o nome do segundo aluno: ')
al3 = input('Digite o nome do terceiro aluno: ')
al4 = input('Digite o nome do quarto aluno: ')

escolhidos = [al1, al2, al3, al4]

sorteado = sample(escolhidos,4)

print(f'A ordem de apresenta {sorteado}')

#random.shuffle