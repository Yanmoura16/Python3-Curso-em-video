print(' ==== Desafio 22 ==== ')

nome = input('Digite seu nome: ').strip()
print(f'Seu nome em MAIÚSCULO:{nome.upper()} ')
print(f'Seu nome em MINÚSCULO:{nome.lower()}')
print(f'Seu nome CAPITALIZADO: {nome.capitalize()}')
print(f"Seu nome tem {len(nome) - nome.count(' ')} letras")

separado = nome.split()
print(f'Seu primeiro nome {separado[0]} tem {len(separado)} letras')