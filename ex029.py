#Exercício Python 029: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
limite = 80
velocidade = int(input('Qual é a velocidade atual do carro em Km/h? '))
if velocidade > limite:
    km_acima = velocidade - limite
    multa = km_acima * 7
    print('MULTADO! TU ULTRAPASSOU O LIMITE DE 80Km/h!')
    print('SUA MULTA FOI DE R${}'.format(multa))
else:
    print('Ok! tudo certo, boa viagem Doutor!')