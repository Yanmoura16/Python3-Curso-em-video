print(' ==== Desafio 14 ==== ')

dia = int(input(' Digite a quantidade de dias alugados: '))
km = float(input(' Digite a quantidade de KM rodados: '))
valor = dia*60 + km*0.15

print(f'O valor total a pagar será: R${valor:.2f}')