#Exercício Python 027: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
nome = str(input('Digite seu nome completo: '))
first_nome = nome.split()[0]
print("Seu primeiro nome é {}".format(first_nome))
last_nome = nome.split()[-1]
print("Seu ultimo nome é {}".format(last_nome))