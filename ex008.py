#Exercício Python 008: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
n = int(input('Digite um número para metros: '))
ce = n * 100
mi = n * 1000
print('O Valor do metro digitado {}, em centimetros é {}, e o valor em milimetros é {}'.format(n, ce, mi))
