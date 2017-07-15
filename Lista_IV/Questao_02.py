'''
 Diêgo C. Oliveira
 Tec. em Informática | IFPI
 Programação para Web | Ritomar Torquato
 Turma 386, Periodo 2017.1

2. Sorteie 20 inteiros entre 1 e 100 numa lista. Armazene os números pares na lista PAR e os números ímpares na lista
IMPAR. Imprima as três listas.
'''
from random import randint
lista_geral = []
lista_par = []
lista_impar = []
for x in range(20):
    lista_geral.append(randint(1,100))
    if lista_geral[x] % 2 == 0:
        lista_par.append(lista_geral[x])
    else:
        lista_impar.append(lista_geral[x])
print("Lista geral:", lista_geral)
print("Lista de pares:", lista_par)
print("Lista de ímpares:", lista_impar)
