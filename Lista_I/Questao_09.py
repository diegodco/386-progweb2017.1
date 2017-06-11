'''
 Diêgo C. Oliveira
 Tec. em Informática | IFPI
 Programação para Web | Ritomar Torquato
 Turma 386, Periodo 2017.1

Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como a
quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia
e R$ 0,15 por km rodado.
'''
km = float(input('Digite os km rodados: '))
dias = int(input('Quantidade de dias: '))
preço = 60*dias + 0.15*km
print('\nTotal a pagar: R$ %.2f' %preço)