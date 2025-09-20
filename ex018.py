import math
angulo = int(input('Digite o Angulo: '))
angulo_radianos = math.radians(angulo)
seno = math.sin(angulo_radianos)
cosseno = math.cos(angulo_radianos)
tangente = math.tan(angulo_radianos)
print('o Angulo é {} e os valores do seno {:.2f}, cosseno{:.2f} e da tangente {:.2f}.'.format(angulo, seno, cosseno, tangente))