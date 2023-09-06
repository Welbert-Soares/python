print('====== DESAFIO 011 ======')
#programa que calcula a área de uma parede e quantos litros serão gastos.

largura = float(input('Qual a largura da parede? '))
altura = float(input('Qual a altura da parede? '))
area = largura * altura
litros = area / 2
print('A área é {} metros quadrados, já a quantidade de tinta será {:.2f} litros.'.format(area, litros))
