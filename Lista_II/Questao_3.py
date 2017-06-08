'''
João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de
seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do
estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você
faça um programa que leia a variável peso (peso de peixes) e verifique se há excesso. Se houver, gravar na
variável excesso e na variável multa o valor da multa que João deverá pagar. Caso contrário mostrar tais
variáveis com o conteúdo ZERO.
'''
peso = float(input('Digite o peso de Peixes (Kg): '))
if peso <= 50:
    print('\nPeso de Peixes: %.2f Kg\n'%peso)
    print('Você não excedeu o limite de pesca!')
else:
    print('\nPeso de Peixes: %.2f Kg\n' % peso)
    print('Você excedeu o limite de pesca!\n')
    excesso = peso - 50
    multa = excesso * 4
    print('Exesso de peso: %.2f Kg'%excesso)
    print('Valor da multa: R$ %.2f' %multa)