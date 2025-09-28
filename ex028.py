#Exercício Python 028: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
import random
numero_computador = random.randint(0, 5)
print('Eae! Estou pensando em um número entre 0 e 5.')
tentativa_usuario = int(input('Tenta adivinhar o número: '))
print('O número que eu pensei foi: {} '.format(numero_computador))
if tentativa_usuario == numero_computador:
    print('PARABÉNS! YOU WIN!')
else:
    print('HAHAHAHAHA PERDEU, OTÁRIO!')
    
