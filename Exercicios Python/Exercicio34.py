print(' ==== Desafio 34 ===== ')

sal = float(input('Digite o salário do funcionario: '))

if sal > 1250:
    sal = sal + (sal * 0.10)
else:
    sal = sal + (sal * 0.15)

print(f'Seu novo salario é: R${sal:.2f}')