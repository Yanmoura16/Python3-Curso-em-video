import datetime

print(' ==== Desafio 40 ==== ')

ano = int(input('Digite o ano de nascimento: '))
data = datetime.date.today()
idade = data.year - ano

if idade < 18:
    print(f'Você nasceu no ano de {ano} então possuí apenas {idade} anos, '
        f'Você só precisará se alistar no ano de {ano + 18} daqui {18 - idade} anos')
elif idade == 18:
    print(f'Você nasceu no ano de {ano} então possuí {idade} anos, '
          f'Você precisará se alistar este ano: {data.year}')
else:
    print(f'Você nasceu no ano de {ano} então possuí {idade} anos, '
            f'Já passou o tempo para o alistamento, você deveria ter se alistado no ano {ano + 18} '
          f'a {idade - 18} anos atrás')
