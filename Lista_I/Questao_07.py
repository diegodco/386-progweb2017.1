'''
 Diêgo C. Oliveira
 Tec. em Informática | IFPI
 Programação para Web | Ritomar Torquato
 Turma 386, Periodo 2017.1

Converta uma temperatura digitada em Celsius para Fahrenheit. F = 9*C/5 + 32.
'''
tcelsius = float(input('Digite a temperatura (ºC): '))
tfahrenheit = 9*tcelsius/5 + 32
print ('\nTemperatura em Fahrenheit %.2f ºF' %tfahrenheit)