#Exercício Python 025: Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
nome = str(input("Digite seu nome completo: ").upper())
if "SILVA" in nome:
    print("Seu nome tem 'SILVA'.")
else:
    print("Seu nome não tem 'SILVA'.")