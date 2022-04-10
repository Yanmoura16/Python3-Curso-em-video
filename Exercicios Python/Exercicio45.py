print(' ==== Desafio 45 ==== ')

prod = float(input('Digite o valor do produto: R$'))
print(''' OPÇÕES DE PAGAMENTO: 
[1] à vista dinheiro/cheque 
[2] à vista cartão 
[3] 2x no cartão 
[4] 3x ou mais no cartão ''')
opcao = int(input('Digite sua opção de pagamento: '))

if opcao == 1:
    preco = prod*0.90
    print(f'Sua opção de pagamento foi: [{opcao}] - à vista dinheiro/cheque')
    print(f'Sua compra no valor de R${prod}, vai custar R${preco}')
elif opcao == 2:
    preco = prod*0.95
    print(f'Sua opção de pagamento foi: [{opcao}] - à vista cartão')
    print(f'Sua compra no valor de R${prod}, vai custar R${preco}')
elif opcao == 3:
    preco = prod/2
    print(f'Sua opção de pagamento foi: [{opcao}] - 2x no cartão')
    print(f'O valor das parcelas será: R${preco:.2f}, totalizando: R${prod} ')
elif opcao == 4:
    parcelas = int(input('Digite a quantidade de parcelas: '))
    preco = prod/parcelas
    print(f'Sua opção de pagamento foi: [{opcao}] - 3x ou mais no cartão')
    print(f'O valor das {parcelas} parcelas será: R${preco:.2f}, totalizando: R${prod}')
else:
    print('\033[:31mOPÇÃO INVÁLIDA, TENTE NOVAMENTE!!!')