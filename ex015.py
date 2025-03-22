dias = int(input('Quantos dias vc ficou com o carro? '))
km = float(input('Quantos Kms vc percorreu com o carro? '))
d = dias * 60
k = km * 0.15
total = d + k
print('Vc andou por {} dias e percorreu por {}, o valor total ficou R$:{}. '.format(dias, km, total))