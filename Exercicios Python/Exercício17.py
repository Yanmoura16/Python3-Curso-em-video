print(' === Desafio 17 === ')

from math import sqrt

catop = float(input('Digite o cateto oposto: '))
catad = float(input('Digite o cateto adjacente: '))

hipo = (catop**2 + catad**2)
hipo = sqrt(hipo)

print(f'A hipotenusa equivale: {hipo:.1f}')

#math.hypot