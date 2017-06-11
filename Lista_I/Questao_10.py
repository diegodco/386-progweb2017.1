'''
 Diêgo C. Oliveira
 Tec. em Informática | IFPI
 Programação para Web | Ritomar Torquato
 Turma 386, Periodo 2017.1

Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a quantidade de cigarros fumados
por dia e quantos anos ele já fumou. Considere que um fumante perde 10 minutos de vida a cada cigarro, calcule quantos
dias de vida um fumante perderá. Exiba o total de dias.
'''
cigarros = int(input('Digite a quantidade de cigarros por dia: '))
anos = int(input('Quantos anos fumando: '))
total_cigarros = anos * 365 * cigarros
dias_perdidos = total_cigarros / 144
print ('\nVocê perdeu aproximadamente %.2f dias' %dias_perdidos)