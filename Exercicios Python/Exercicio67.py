print(' ===== Desafio 67 ===== ')

cont = 0
soma = 0

while True:
    num = int(input('Digite um número: [999 para parar] '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'Total de números inseridos: {cont} \n'
      f'A soma entre eles foi: {soma}')

