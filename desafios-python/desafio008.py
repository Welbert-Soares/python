print('====== DESAFIO 08 ======')

number_1 = float(input('Qual o valor em metros? '))
centimetros = number_1 * 100
melimetros = number_1 * 1000
print('O valor em metros é {}m, já em centimetros {:.0f}cm e em milímetros {:.0f}mm'.format(number_1, centimetros,melimetros))