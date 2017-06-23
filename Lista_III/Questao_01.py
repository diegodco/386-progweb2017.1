'''
 Diêgo C. Oliveira
 Tec. em Informática | IFPI
 Programação para Web | Ritomar Torquato
 Turma 386, Periodo 2017.1

1. Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue
pedindo até que o usuário informe um valor válido.
'''
nota = float(input("Digite uma nota (0 a 10): "))
while nota < 0 or nota > 10:
    print("Nota inválida!")
    n = float(input("Digite uma nota (0 a 10): "))
print("\nNota:", nota)