#Exercício Python 017: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
import math
co = float(input('Digite o Cateto oposto: '))
ca = float(input('Digite o Cateto Adjacente: '))
calculo = math.sqrt(co**2 + ca**2)
print('O Comprimento da hipotenusa é {}.'.format(calculo))