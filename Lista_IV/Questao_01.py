'''
1. Sorteie 10 inteiros entre 1 e 100 para uma lista e descubra o maior e o menor valor, sem usar as funções max e min.
'''
from random import randint
lista = []
maior = 1
menor = 100
for x in range(10):
    lista.append(randint(1,100))
for y in range(10):
    if lista[y] > maior:
        maior = lista[y]
    if lista[y] < menor:
        menor = lista[y]
print("N's° sorteados: ", lista)
print("Maior valor sorteado:", maior)
print("Menor valor sorteado:", menor)