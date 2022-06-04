print(' ===== Desafio 64 ===== ')

n = int(input('Digite a quantidade de termos para mostrar na tela: '))
f1 = 0
f2 = 1
c = 3

print(f'{f1}')
print(f'{f2}')

while c <= n:
    f3 = f1 + f2
    print(f'{f3} ')
    f1 = f2
    f2 = f3
    c += 1
print('fim')


