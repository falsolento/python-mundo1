#Exercício Python 031: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
distancia = float(input('Qual é a distância total da viagem em Km? '))
tarifa_curta = 0.50
tarifa_longa = 0.45
limite = 200
preco_passagem = 0
if distancia <= limite:
    preco_passagem = distancia * tarifa_curta
    print('Tarifa de R${} foi aplicada por Km.'.format(tarifa_curta))
else:
    preco_passagem = distancia * tarifa_longa
    print('Tarifa de R${} foi aplicada por Km.'.format(tarifa_longa))
print('Sua viagem de {}Km, tem o valor total da passagem de R${}.'.format(distancia,preco_passagem))