cidade = str(input('Digite o nome da sua cidade: '))
cidade_maiusculo = cidade.upper()
primeira_cidade = cidade_maiusculo.split()[0]
if primeira_cidade.startswith('SANTO'):
    print('Sua cidade comeca com a palavra Santo.')
else:
    print('Sua cidade nao comeca com a palavra Santo.')
