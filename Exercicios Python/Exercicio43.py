print(' ==== Desafio 43 ==== ')

a = float(input('Digite o primeiro segmento: '))
b = float(input('Digite o segundo segmento: '))
c = float(input('Digite o terceiro segmento: '))

if a < b + c and b < a + c and c < a + b:
    print('Os segmentos formam um triângulo ', end='')
    if a == b == c:
        print('EQUILÁTERO')
    elif a != b !=c !=a:
        print('ESCALENO')
    else:
        print('ISÓSCELES')

else:
    print('Os segmentos não formam um triângulo!')
