#Exercício Python 022: Crie um programa que leia o nome completo de uma pessoa e mostre: 
#- O nome com todas as letras maiúsculas e minúsculas.
#- Quantas letras ao todo (sem considerar espaços).
#- Quantas letras tem o primeiro nome.
nome = str(input('Digite seu nome completo: '))
nome_maiuscula = nome.upper()
print('Seu nome em maisculo é: {}'.format(nome_maiuscula))
nome_minuscula = nome.lower()
print('Seu nome em minusculo é: {}'.format(nome_minuscula))
nome_letras = len(nome.replace(" ", ""))
print('Seu nome tem o total de letras: {}'.format(nome_letras))
nome_primeiro = nome.split()[0]
nome_primeiro_letras = len(nome_primeiro)
print('Seu primeiro nome tem {} letras.'.format(nome_primeiro_letras))