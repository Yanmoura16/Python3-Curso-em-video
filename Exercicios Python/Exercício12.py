print(' ==== Desafio 012 ==== ')

prod = float(input('Digite o valor do produto: '))
desc = int(input('Digite o valor do desconto: '))
valor = prod-(prod*desc/100)


print(f'O produto custava: R${prod}, com desconto de {desc}%  seu novo valor é: R${valor}')