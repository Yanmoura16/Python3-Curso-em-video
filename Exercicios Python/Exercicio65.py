print(' ===== Desafio 65 ===== ')

n1 = int(input('Digite um numero [ 999 para parar ]: '))
n2 = n1
c = 0
n3 = 0


while n2 != 999:
    n3 += n2
    n2 = int(input('Digite um numero: '))
    c += 1

print(f'O Total de números inseridos foram: {c}')
print(f'A soma total desses números é: {n3}')
