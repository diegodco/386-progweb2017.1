'''
 Diêgo C. Oliveira
 Tec. em Informática | IFPI
 Programação para Web | Ritomar Torquato
 Turma 386, Periodo 2017.1

5. Faça um programa que peça um inteiro positivo e o mostre invertido. Ex.: 1234 gera 4321
'''
numero = int(input("Digite um número: "))
invertido = 0
while numero > 0:
  invertido *= 10
  invertido += numero % 10
  numero //= 10
print("Valor invertido: %d"%invertido)
