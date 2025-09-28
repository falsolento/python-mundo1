#Exercício Python 034: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
limite_salarial = 1250.00
salario_atual = float(input('Qual é o salário atual do funcionário (R$)? '))
percentual_aumento = 0
valor_aumento = 0
if salario_atual > limite_salarial:
    percentual_aumento = 10
    valor_aumento = salario_atual * 0.10
else:
    percentual_aumento = 15
    valor_aumento = salario_atual * 0.15
novo_salario = salario_atual + valor_aumento
print('O NOVO SALÁRIO é de R${}'.format(novo_salario))