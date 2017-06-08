'''
 Diêgo C. Oliveira
 Tec. em Informática | IFPI
 Programação para Web | Ritomar Torquato
 Turma 386, Periodo 2017.1

Faça um Programa que leia três números e mostre o maior deles.
'''
a = int(input('Primeiro nº: '))
b = int(input('Segundo nº: '))
c = int(input('Terceiro nº: '))
if a > b and a > c:
    print('O Primeiro nº "%d", é maior.'%a)
elif b > c:
    print('O Segundo nº "%d", é maior.'%b)
elif c > b:
    print('O Terceiro nº "%d", é o maior.'%c)
else:
    print('Todos os números são iguais!!')
