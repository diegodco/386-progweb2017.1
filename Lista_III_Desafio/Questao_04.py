'''
 Diêgo C. Oliveira
 Tec. em Informática | IFPI
 Programação para Web | Ritomar Torquato
 Turma 386, Periodo 2017.1

4. Dado um número inteiro positivo, determine a sua decomposição em fatores primos
calculando também a multiplicidade de cada fator.
'''
numero = int(input("Digite um número: "))
print("Decomposição em fatores primos")
for i in range(2, numero):
  while numero % i == 0:
    print (i)
    numero = numero / i
