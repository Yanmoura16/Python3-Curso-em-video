print(' ===== Desafio 68 ===== ')

cont = 1

num = int(input('Digite um número para saber sua tabuada: '))

while True:
    if num < 0:
        break
    for cont in range(1, 11):
        total = num * cont
        print(f'{num}X{cont} = {total}')
        cont += 1
    num = int(input('\n Digite um número para saber sua tabuada: '))

print('PROGRAMA ENCERRADO.')


