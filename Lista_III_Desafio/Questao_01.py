'''
 Diêgo C. Oliveira
 Tec. em Informática | IFPI
 Programação para Web | Ritomar Torquato
 Turma 386, Periodo 2017.1
 
1. Dizemos que um número natural é triangular se ele é produto de três números naturais consecutivos. Exemplo: 120
é triangular, pois 4.5.6 = 120. Dado um inteiro não-negativo n, verificar se n é triangular.
'''
n = int(input("Digite um numero: "))
a = 0
b = 1
c = 2
d = 0
while d < n:
    a = a + 1
    b = b + 1
    c = c + 1
    d = a * b * c
if d == n:
    print("\nEsse numero é triangular")
else:
    print("\nEsse numero não é triangular")