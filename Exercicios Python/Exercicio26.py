print(' ==== Desafio 26 ==== ')

nome = input('Digite seu nome: ').strip().upper()
print(f'A letra A aparece {nome.count("A")} vezes')
print(f'A letra A aparece na posição: {nome.find("A")+1}° ')
print(f'A ultima letra A aparece na posição: {nome.rfind("A")+1}°')