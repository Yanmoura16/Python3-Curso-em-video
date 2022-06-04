print(' ===== Desafio 66 ===== ')

n = int(input('Digite um valor: '))
resposta = str(input('Quer continuar? [S/N] ')).upper().strip()
cont = 1
total = n
maior = n
menor = n


while resposta != 'N':
    n = int(input('Digite um valor: '))
    resposta = str(input('Quer continuar? [S/N] ')).upper().strip()
    total += n
    cont += 1
    if n > maior:
        maior = n
    elif n < menor:
        menor = n

media = total/cont

print(f'Você digitou {cont}x vezes, a média foi: {media}'
      f'O maior valor foi: {maior} e o menor foi: {menor}')





