#Exercício Python 016: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
import math
n = float(input('Digite um número real: '))
inteiro = math.trunc(n)
print('O número {} tem a parte inteira {}.'.format(n, inteiro))
