print(' === Desafio 10 === ')
real = float(input(' Quanto R$ você tem? '))
dolar = real / 5
euro = real / 5.55
libra = real / 6.61

print(f' Com R${real} é possível comprar ${dolar:.2f} dólares ')
print(f' Com R${real} é possível comprar €{euro:.2f} euros ')
print(f' Com R${real} é possível comprar £{libra:.2f} libras ')