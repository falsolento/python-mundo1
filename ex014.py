#Exercício Python 014: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
graus = float(input('Qual é a temperatura em C? '))
fahr = (graus * 1.8) + 32
print('A temperatura em Fahrenhei é {}. '.format(fahr))