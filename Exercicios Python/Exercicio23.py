print(' ==== Desafio 23 ====')
num = int(input('Digite seu número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'Seu número foi: {num}')
print(f'A Unidade é: {u}')
print(f'A Dezena é: {d}')
print(f'A Centena é: {c}')
print(f'O Milhar é: {m}')

