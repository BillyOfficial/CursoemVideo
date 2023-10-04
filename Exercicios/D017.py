from math import sqrt
print('================== Desafio 17 ======================')
catopo = float(input('Digite o comprimento do cateto oposto:'))
catadj = float(input('Digite o comprimento do cateto adjacente: '))
print(f'O comprimento da hipotenusa é {sqrt(catopo**2+catadj**2):.2f}')
