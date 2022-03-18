print(' ==== Desafio 33 ==== ')

a = int(input('Digite o primeiro numero: '))
b = int(input('Digite o segundo numero: '))
c = int(input('Digite o terceiro numero: '))

maior = a

if b > a and b > c:
    maior = b
if c > b and c > a:
    maior = c

menor = a

if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

print(f'O maior numero é: {maior}')
print(f'O Menor numero é: {menor}')