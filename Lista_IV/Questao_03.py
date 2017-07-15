'''
 Diêgo C. Oliveira
 Tec. em Informática | IFPI
 Programação para Web | Ritomar Torquato
 Turma 386, Periodo 2017.1

3. Faça um programa que crie dois vetores com 10 elementos aleatórios entre 1 e 100. Gere um terceiro vetor de
20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores. Imprima os três
vetores.
'''
from random import randint
vetor1 = []
vetor2 = []
vetor3 = []
for x in range(10):
    vetor1.append(randint(1,100))
    vetor2.append(randint(1,100))
for y in range(10):
    vetor3.append(vetor1[y])
    vetor3.append(vetor2[y])
print("Vetor 1:", vetor1)
print("Vetor 2:", vetor2)
print("Vetor intercalado:", vetor3)