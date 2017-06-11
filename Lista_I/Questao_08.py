'''
 Diêgo C. Oliveira
 Tec. em Informática | IFPI
 Programação para Web | Ritomar Torquato
 Turma 386, Periodo 2017.1

Faça agora o contrário, de Fahrenheit para Celsius.
'''
tfahrenheit = float(input('Digite a temperatura (ºF): '))
tcelsius = (tfahrenheit - 32) * 5 / 9
print ('\nTemperatura em Celsius: %.2f ºC' %tcelsius)