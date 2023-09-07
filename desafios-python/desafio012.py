print('====== DESAFIO 012 ======')
# programa que lê o preço de um produto e calcula 5% de desconto sobre o mesmo.

price = float(input('Qual o preço do produto? R$'))
new_valor = price - (price * 5 / 100)
print('O produto que custava R${:.2f}, na promoção de 5% de desconto vai custar R${:.2f}.'.format(price, new_valor))