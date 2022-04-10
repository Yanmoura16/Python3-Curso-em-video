print('==== Desafio 52 ==== ')

termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razao da PA: '))

for c in range(1, 11):
    print(f'O Termo A{c} é igual á: {termo}')
    termo = termo + razao
