print(' ===== Desafio 60 ===== ')

num1 = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))
total = 0

print('''\033[7m ===== MENU ===== \033[m
\033[1m[1]SOMAR
[2]MULTIPLICAR
[3]MAIOR
[4]NOVOS NÚMEROS
[5]SAIR DO PROGRAMA''')

escolha = int(input('Escolha sua opção: '))

while escolha != 5:
    if escolha == 1:
        total = num1 + num2
        print(f'A soma entre {num1} + {num2} = {total}')
        print('''\033[7m ========= MENU ========= \033[m
        \033[1m[1]SOMAR
        [2]MULTIPLICAR
        [3]MAIOR
        [4]NOVOS NÚMEROS
        [5]SAIR DO PROGRAMA''')

        escolha = int(input('Escolha sua opção: '))

    if escolha == 2:
        total = num1 * num2
        print(f'A soma entre {num1} * {num2} = {total}')
        print('''\033[7m ========= MENU ========= \033[m
        \033[1m[1]SOMAR
        [2]MULTIPLICAR
        [3]MAIOR
        [4]NOVOS NÚMEROS
        [5]SAIR DO PROGRAMA''')

        escolha = int(input('Escolha sua opção: '))

    if escolha == 3:
        if num1 > num2:
            print(f'O maior é: {num1}')
        elif num1 == num2:
            print('Os número são iguais!')
        else:
            print(f'O maior é {num2}')

        print('''\033[7m ========= MENU ========= \033[m
        \033[1m[1]SOMAR
        [2]MULTIPLICAR
        [3]MAIOR
        [4]NOVOS NÚMEROS
        [5]SAIR DO PROGRAMA''')

        escolha = int(input('Escolha sua opção: '))

    if escolha == 4:
        print(f'Escolha novos numeros:')
        num1 = int(input('Digite um numero: '))
        num2 = int(input('Digite outro numero: '))
        print('''\033[7m ========= MENU ========= \033[m
        \033[1m[1]SOMAR
        [2]MULTIPLICAR
        [3]MAIOR
        [4]NOVOS NÚMEROS
        [5]SAIR DO PROGRAMA''')

        escolha = int(input('Escolha sua opção: '))

    if escolha > 5:
        print('OPÇÃO INVALIDA, TENTE NOVAMENTE')
        print('''\033[7m ========= MENU ========= \033[m
        \033[1m[1]SOMAR
        [2]MULTIPLICAR
        [3]MAIOR
        [4]NOVOS NÚMEROS
        [5]SAIR DO PROGRAMA''')

        escolha = int(input('Escolha sua opção: '))

print('VOCÊ SAIU DO PROGRAMA')





