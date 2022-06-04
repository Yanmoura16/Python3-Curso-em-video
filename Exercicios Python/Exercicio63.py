print(' ===== Desafio 63 ===== ')

t = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razao do termo: '))
c = 1
total = 0
mais = 10

while mais != 0:
    total += mais
    while c <= total:
            print(t)
            t += r
            c += 1
    mais = int(input('Quantos termos você quer mostrar mais? '))
print('FIM')
print(f'Total de termos: {total}')

