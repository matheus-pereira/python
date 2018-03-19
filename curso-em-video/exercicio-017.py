from math import sqrt, pow, hypot
co = int(input('Digite o valor do cateto oposto: '))
ca = int(input('Digite o valor do cateto adjascente: '))
# h = sqrt(pow(co, 2) + pow(ca, 2))
# h = (co ** 2 + ca ** 2) ** (1/2)
print('A comprimento da hipotenusa é {}'.format(hypot(co, ca)))
