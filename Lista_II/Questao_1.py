'''
 Diêgo C. Oliveira
 Tec. em Informática | IFPI
 Programação para Web | Ritomar Torquato
 Turma 386, Periodo 2017.1

Faça um Programa que peça os três lados de um triângulo. O programa deverá informar se os valores podem ser
um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
'''
a = int(input('Digite o primeiro lado do Triângulo: '))
b = int(input('Digite o segundo lado do Triângulo: '))
c = int(input('Digite o terceiro lado do Triângulo: '))
if a == b and c == a:
    print('\nTriângulo equilátero')
elif a == b or c == a:
    print('\nTriângulo isósceles')
else:
    print('\nTriângulo escaleno')