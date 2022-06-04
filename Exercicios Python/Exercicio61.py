print(' ===== Desafio 61 ===== ')

#from math import factorial
#num = int(input('Digite um numero: '))
#fact = factorial(num)
#print(f'O Fatorial de {num} é {fact}')

n = int(input('Digite um número: '))
c = n
f = 1

while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f)

