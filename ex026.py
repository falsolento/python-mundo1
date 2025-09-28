#Exercício Python 026: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
frase = str(input("Digite uma frase: ")).upper().strip()
contagem_a = frase.count('A')
primeiro_a = frase.find('A') + 1
ultimo_a = frase.rfind('A') + 1
print("A letra 'A' aparece {} vezes na frase.".format(contagem_a))
print("A primeira vez que a letra 'A' aparece é na posição {}.".format(primeiro_a))
print("A última vez que a letra 'A' aparece é na posição {}.".format(ultimo_a))