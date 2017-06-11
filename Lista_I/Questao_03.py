'''
 Diêgo C. Oliveira
 Tec. em Informática | IFPI
 Programação para Web | Ritomar Torquato
 Turma 386, Periodo 2017.1

Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total em segundos.
'''
d = int(input('Quantidade de dias: '))
h = int(input('Quantidade de horas: '))
m = int(input('Quantidade de minutos: '))
s = int(input('Quantidade de segundos: '))
total = d * 24 * 60 * 60 + h * 60 * 60 + m * 60 + s
print ("\nTotal em segundos: ",total)