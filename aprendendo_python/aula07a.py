# Operadores Aritmétricos
# +(adição)  -(subtração) *(multiplicação) /(divisão) **(potencialização)  //(divisão inteira) %(resto da divisão) ==(igual)
# Ordem de Precedência
#        1° () ,           2 ° * * ,           3° * , / , // , % .          4° + , - .
#--------------------------------------------------------------------------------------------------------------------------------------------

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, o produto é {} e a divisão é {:3}.'.format(s, m , d))
print('Divisão inteira {} e potência {}.'.format(di, e))