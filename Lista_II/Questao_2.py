'''
 Diêgo C. Oliveira
 Tec. em Informática | IFPI
 Programação para Web | Ritomar Torquato
 Turma 386, Periodo 2017.1

Determine se um ano é bissexto. Verifique no Google como fazer isso...
'''
ano = int(input('Digite um ano: '))
if ano % 4 == 0 or ano % 400 == 0:
    print('\nO ano "%d" é bissexto'%ano)
else:
    print('\nO ano "%d" não é bissexto'%ano)