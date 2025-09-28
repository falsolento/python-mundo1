#Exercício Python 015: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
dias = int(input('Quantos dias vc ficou com o carro? '))
km = float(input('Quantos Kms vc percorreu com o carro? '))
d = dias * 60
k = km * 0.15
total = d + k
print('Vc andou por {} dias e percorreu por {}, o valor total ficou R$:{:.2f}. '.format(dias, km, total))
