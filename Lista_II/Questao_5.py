'''
 Diêgo C. Oliveira
 Tec. em Informática | IFPI
 Programação para Web | Ritomar Torquato
 Turma 386, Periodo 2017.1

Faça um Programa que leia três números e mostre o maior e o menor deles.
'''
a = int(input('Primeiro nº: '))
b = int(input('Segundo nº: '))
c = int(input('Terceiro nº: '))
# Maior
if a > b and a > c:
    maior = ('O Primeiro nº "%d", é maior.'%a)
elif b > c:
    maior = ('O Segundo nº "%d", é maior.'%b)
elif c > b:
    maior = ('O Terceiro nº "%d", é o maior.'%c)
else:
    maior = ('Todos os números são iguais!!')
# Menor
if a < b and a < c:
    menor = ('O Primeiro nº "%d", é o menor.'%a)
elif b < c:
    menor = ('O Segundo nº "%d", é o menor.'%b)
elif c < b:
    menor = ('O Terceiro nº "%d", é o menor.'%c)
print(maior)
print(menor)
