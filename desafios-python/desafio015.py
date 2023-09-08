print('====== DESAFIO 015 ======')
# programa que calcule a quantidade de Km e a quantidade de dias que foi alugado. Calcule o preço a pagar. dia= r$60 hora R$ 0.15.
dias = int(input('Digite a quantidade de dias que alugou: '))
km = float(input('Digite a quantidade de quilometros rodados: '))
pagar = (dias * 60) + (km * 0.15)
print('O total a pagar será de R${:.2f}.'.format(pagar))
print('-'*25)
