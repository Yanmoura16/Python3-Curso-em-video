print(' === Desafio 18 === ')

import math

an = float(input('Digite o ângulo: '))
ra = math.radians(an)
seno = math.sin(ra)
cos = math.cos(ra)
tan = math.tan(ra)

print(f'O ângulo de {an}° tem o SENO de: {seno:.2f}')
print(f'O ângulo de {an}° tem o COSSENO de: {cos:.2f}')
print(f'O ângulo de {an}° tem a TANGENTE de: {tan:.2f}')