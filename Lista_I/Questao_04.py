'''
 Diêgo C. Oliveira
 Tec. em Informática | IFPI
 Programação para Web | Ritomar Torquato
 Turma 386, Periodo 2017.1

Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a porcentagem do aumento.
Exiba o valor do aumento e do novo salário.
'''
salario = float(input('Digite o salário: '))
paumento = float(input('Digite a porcentagem de aumento: '))
aumento = salario * paumento / 100
novos = salario + aumento
print('\nAumento: R$ %.2f' %aumento)
print('Novo salário: R$ %.2f' %novos)