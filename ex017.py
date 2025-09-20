import math
co = float(input('Digite o Cateto oposto: '))
ca = float(input('Digite o Cateto Adjacente: '))
calculo = math.sqrt(co**2 + ca**2)
print('O Comprimento da hipotenusa é {}.'.format(calculo))