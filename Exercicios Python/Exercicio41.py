print(' ==== Desafio 41 ==== ')

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2

if media < 5:
    print(f'Sua media foi: {media}, Você foi \033[:31mREPROVADO')
elif 5 <= media < 7:
    print(f'Sua media foi: {media}, Você está de \033[:33mRECUPERAÇÃO')
else:
    print(f'Sua media foi: {media}, Parabéns você está \033[:32mAPROVADO!!')
    