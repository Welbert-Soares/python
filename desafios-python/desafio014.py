print('====== DESAFIO 014 ======')
# Programa que converta uma temperatura digitada em °C para °F.

celsius = float(input('Digite a temperatura em Celsius: '))
fahrenheit = (celsius * 1.8) + 32
print('O valor em Celsius é {:.1f}°C , em Fahrenheit será {:.1f}°F.'.format(celsius, fahrenheit))