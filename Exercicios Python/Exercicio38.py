print(' ==== Desafio 38 ==== ')

num = int(input('Digite um número: '))
print('''Escolha uma base para conversão:
[1] - Binário
[2] - Octal
[3] - Hexadecimal  ''')
conversao = int(input('Qual sua base? '))
if conversao == 1:
    print(f'{num} Convertido para Binário é igual a {bin(num)[2:]}')
elif conversao == 2:
    print(f'{num} Convertido para Octal é igual a {oct(num)[2:]}')
elif conversao == 3:
    print(f'{num} Convertido para Hexadecimal é igual a {hex(num)[2:]}')
else:
    print(' \033[:31m Opção inválida, tente novamente!')
