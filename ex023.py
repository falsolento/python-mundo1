#Exercício Python 023: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
numero = input('Digite um numero entre 0 e 9999: ')
numero_completo = numero.zfill(4)
milhar = numero_completo[0]
centena = numero_completo[1]
dezena = numero_completo[2]
unidade = numero_completo[3]
print('Seu numero {} em milhar {}, centena {}, dezena {} e unidade {}'.format(numero, milhar, centena, dezena, unidade))