from math import radians, sin, cos, tan
a = int(input('Digite um ângulo: '))
print('O ângulo {} possui seno {:.2f}, cosseno {:.2f} e tangente {:.2f}'.format(a, sin(radians(a)), cos(radians(a)), tan(radians(a))))
