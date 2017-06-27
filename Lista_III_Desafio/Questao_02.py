'''
 Diêgo C. Oliveira
 Tec. em Informática | IFPI
 Programação para Web | Ritomar Torquato
 Turma 386, Periodo 2017.1

2. Indique como um troco deve ser dado utilizando-se um número mínimo de notas. Seu algoritmo deve ler o valor da
conta a ser paga e o valor do pagamento efetuado desprezando os centavos. Suponha que as notas para troco sejam as de
50, 20, 10, 5, 2 e 1 reais, e que nenhuma delas esteja em falta no caixa.
'''

preco = int(input("Valor a ser pago: "))
dinheiro = int(input("Pagamento efetuado: "))

troco = (dinheiro - preco)

if troco > 0:
    print("\nTroco: R$ %s\n" %troco)

for p in 50, 20, 10, 5, 2, 1:

    if troco >= p:
        n = troco/p
        r = troco - p*n
        print("%s nota(s) de R$ %s."%(n, p))