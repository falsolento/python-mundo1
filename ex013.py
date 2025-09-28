#Exercício Python 013: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
sa = float(input('Digite seu salário: '))
cal = (15 / 100) * sa
aum = sa + cal
print('Seu salário ficou {}, pq voce ganhou 15% de aumento'.format(aum))