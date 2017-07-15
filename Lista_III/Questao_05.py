'''
 Diêgo C. Oliveira
 Tec. em Informática | IFPI
 Programação para Web | Ritomar Torquato
 Turma 386, Periodo 2017.1

5. Dados dois números inteiros positivos, determinar o máximo divisor comum entre eles usando o algoritmo de Euclides.
'''


def MDC(a, b):
    while (b != 0):
        q = a / b
        r = a % b
        a = b
        b = r
    return a
a = 32
b = 1024
print("MDC de %d e %d é: %d" % (a, b, MDC(a, b)))