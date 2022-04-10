print(' ==== Desafio 37 ====')

casa = float(input('Qual o valor da Casa? '))
salario = float(input('Qual o seu salário? '))
anos = int(input('Em quantos anos você pretende pagar a casa? '))
mensalidade = casa/(anos*12)

if mensalidade >= salario * 0.3 :
    print(f'Para pagar a casa de R${casa:.2f} em {anos} anos a mensalidade será:{mensalidade:.2f}'
          f'\033[:31m EMPRÉSTIMO NEGADO')
else:
    print(f'Para pagar a casa de R${casa:.2f} em {anos}, a mensalidade será: {mensalidade:.2f} '
          f'\033[:32m EMPRÉSTIMO AUTORIZADO ')




