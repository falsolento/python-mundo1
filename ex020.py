#Exercício Python 020: O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random
aluno1 = str(input('Qual é o nome do Aluno 1: '))
aluno2 = str(input('Qual é o nome do Aluno 2: '))
aluno3 = str(input('Qual é o nome do Aluno 3: '))
aluno4 = str(input('Qual é o nome do Aluno 4: '))
nomes = (aluno1, aluno2, aluno3, aluno4)
sorteio = random.choice(nomes, 4)
print('O Primeiro Aluno sorteado foi o {}.\n O Segundo Aluno sorteado foi o {}.\n O Terceiro Aluno sorteado foi o {}.\n O Quarto Aluno sorteado foi o {sorteio}.')