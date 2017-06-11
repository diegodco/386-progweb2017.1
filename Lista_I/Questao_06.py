'''
 Diêgo C. Oliveira
 Tec. em Informática | IFPI
 Programação para Web | Ritomar Torquato
 Turma 386, Periodo 2017.1

Calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média esperada para a viagem.
'''
distancia = float(input('Digite a distância em km: '))
velocidade = float(input('Digite a velocidade média em km/h: '))
tempo = distancia / velocidade
print ('\nTempo aproximado: %.2f h' %tempo)