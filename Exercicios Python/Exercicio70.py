print(' ===== Desafio 70 ===== ')

pessoamaior = 0
mulhermenor = 0
conthomem = 0

while True:
    nome = str(input('Qual seu nome: '))
    idade = int(input('Qual sua idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Qual seu sexo? [F/M] ')).upper().strip()[0]

    if idade >= 18:
        pessoamaior += 1
    if sexo in 'M':
        conthomem += 1
    if idade < 20 and sexo in 'F':
        mulhermenor += 1

        resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Você quer continuar? [S/N] ')).strip().upper()[0]

    if resposta in 'Nn':
        break

print(f'(A) Total de maiores de 18 anos: {pessoamaior}')
print(f'(B) Total Homens cadastrados: {conthomem}')
print(f'(C) Total de mulheres com menos de 20 anos: {mulhermenor}')