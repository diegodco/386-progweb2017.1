'''
 Diêgo C. Oliveira
 Tec. em Informática | IFPI
 Programação para Web | Ritomar Torquato
 Turma 386, Periodo 2017.1

3. Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que
a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o
número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas
de crescimento
'''
populacao_A = 80000
populacao_B = 200000
taxa_pop_A = 0.030
taxa_pop_B = 0.015
anos =  0
while populacao_A < populacao_B:
    populacao_A *= (1 + taxa_pop_A)
    populacao_B *= (1 + taxa_pop_B)
    anos += 1
print("\n População A: %d\n População B: %d\n\n A população A será igual ou superior a população B em %d anos" % (populacao_A, populacao_B, anos))