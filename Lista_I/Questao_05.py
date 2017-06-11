'''
 Diêgo C. Oliveira
 Tec. em Informática | IFPI
 Programação para Web | Ritomar Torquato
 Turma 386, Periodo 2017.1

Solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar.
'''
mercadoria = float(input('Digite o preço da mercadoria: '))
pdesconto = float(input('Digite a porcentagem de desconto: '))
desconto = mercadoria * pdesconto / 100
novoval = mercadoria - desconto
print('\nTotal do desconto: R$ %.2f' %desconto)
print('Total a pagar: R$ %.2f' %novoval)