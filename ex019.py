import random
aluno1 = str(input('Qual é o nome do Aluno 1: '))
aluno2 = str(input('Qual é o nome do Aluno 2: '))
aluno3 = str(input('Qual é o nome do Aluno 3: '))
aluno4 = str(input('Qual é o nome do Aluno 4: '))
nomes = (aluno1, aluno2, aluno3, aluno4)
sorteio = random.choice(nomes)
print('O Aluno sorteado foi o {}.'.format(sorteio))