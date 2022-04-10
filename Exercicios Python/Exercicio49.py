print(' ==== Desafio 49 ==== ')

soma = 0

for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
print(f'A soma de todos os numeros impares divisíveis por 3 é: {soma}')
