print(' ==== Desafio 42 ==== ')

idade = int(input('Digite a idade do Atleta: '))

if idade <= 9:
    print(f'Com {idade} anos de idade, você se encaixa na categoria:\033[:32m MIRIM')
elif idade <= 14:
    print(f'Com {idade} anos de idade, você se encaixa na categoria:\033[:32m INFANTIL')
elif idade <= 19:
    print(f'Com {idade} anos de idade, você se encaixa na categoria:\033[:32m JUNIOR')
elif idade == 20:
    print(f'Com, {idade} anos de idade, você se encaixa na categoria:\033[:32m SÊNIOR')
else:
    print(f'Acima de 20 anos de idade, você se encaixa na categoria:\033[:32m MASTER')