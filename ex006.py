#Exercício Python 006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
n = int(input('Digite um número: '))
d = n * 2
t = n * 3
r = n ** 0.5
print('O Seu número é {}, Multiplicado por 2 é {}, Multiplicado por 3 é {} e a Raiz quadrada é {}'.format(n, d, t, r))