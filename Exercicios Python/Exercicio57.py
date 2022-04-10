print(' ==== Desafio 57 ==== ')

media = 0
idadevelho = 0
velho = ''
mulheridade = 0

for c in range(1, 5):
    print(f' ----- {c}°Pessoa ----- ')
    nome = str(input(f'Digite o nome da {c}° pessoa: ')).strip()
    idade = int(input(f'Digite a idade da {c}°pessoa: '))
    sexo = str(input(f'Digite o sexo da {c}°pessoa: M/F: ')).strip().upper()
    media += idade
    if c == 1 and sexo == 'M':
        idadevelho = idade
        velho = nome
    if sexo == 'M' and idade > idadevelho:
        idadevelho = idade
        velho = nome
    if sexo == 'F' and idade < 20:
        mulheridade += 1

print(f'A Média das idades é: {media/4:.1f} anos ')
print(f'O nome do Homem mais velho é: {velho} ')
print(f'Existe {mulheridade} mulheres com menos de 20 anos de idade ')
