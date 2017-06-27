'''
 Diêgo C. Oliveira
 Tec. em Informática | IFPI
 Programação para Web | Ritomar Torquato
 Turma 386, Periodo 2017.1

 3. Verifique se um inteiro positivo n é primo.
'''
n = int(input("Digite um número inteiro positivo: "))

i = 2
e_primo = True

while i < n and e_primo:
    e_primo = not ((n % i) == 0)
    i += 1

if (e_primo):
    print("O número %d é primo"%n)
else:
    print("O número %d não é primo"%n)