print(' ===== Desafio 58 ===== ')

sexo = str(input('Digite o sexo da pessoa [M/F]: ')).strip().upper()

while sexo != 'M' and sexo != 'F':
    print('Sexo inválido, por favor digite novamente!!')
    sexo = str(input('Digite o sexo da pessoa [M/F]: ')).strip().upper()

if sexo == 'M':
    print(f'O sexo da pessoa é: Masculino ')
else:
    print('O Sexo da pessoa é: Feminino ')
