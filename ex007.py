#Exercício Python 007: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
n1 = int(input('Digite a nota 1: '))
n2 = int(input('Digite a nota 2: '))
m = (n1 + n2) / 2
print('A média do seu aluno é {}'.format(m))