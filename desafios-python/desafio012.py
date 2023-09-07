print('====== DESAFIO 012 ======')
# programa que lê o preço de um produto e calcula 5% de juros sobre o mesmo.

price = float(input('Qual o preço do produto? '))
juros = price * 5 / 100
new_valor = price + juros
print('O juros de cinco por cento sobre o valor R${:.2f}, será R${:.2f}, ao total R${:.2f}.'.format(price, juros, new_valor))