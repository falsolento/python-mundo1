#Exercício Python 005: Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.
n = int(input('Digite um número inteiro: '))
a = n - 1
s = n + 1
print('Seu número inteiro é {}, O seu número antecessor é {} e O seu número sucessor é {}'.format(n, a, s ))