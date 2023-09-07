print('====== DESAFIO 013 ======')
# programa que leia o salário de um funcionário e retorne com 15% de aumento

salario = float(input('Qual o valor do salário? R$'))
new_money = salario + (salario * 15 / 100)
print('O salário é R${:.2f}, com o aumento de 15% ficará R${:.2f}'.format(salario, new_money))
print('-'*25)
