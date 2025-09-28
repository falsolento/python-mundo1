#Exercício Python 012: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
p1 = float(input('Qual é o preco do produto: '))
p2 = (5 / 100) * p1
p3 = p1 - p2
print('O valor com desconto é {}'.format(p3))