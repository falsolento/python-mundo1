#Exercício Python 011: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
al = float(input('Qual é a altura da sua parede: '))
la = float(input('Qual é a largura da sua parede: '))
ar = al * la
ti = 2
li = ar / ti
print('A área da sua parede é: {} e a quantidade de litros de tinta para pintar é {}'.format(ar, li))
