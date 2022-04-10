print(' ==== Desafio 55 ==== ')
from datetime import date

hoje = date.today().year
maior = 0
menor = 0


for c in range(1, 8):
    nascimento = int(input(f'Digite a data de nascimento da {c}° pessoa: '))
    idade = hoje - nascimento
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print(f'Existem {maior} maiores de idade no total')
print(f'Existem {menor} menores de idade no total')

