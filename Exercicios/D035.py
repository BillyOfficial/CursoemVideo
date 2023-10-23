# Desenvolva um programa que leia o comprimento de três retas
# E diga ao usuário se elas podem ou não formar um triângulo.

print('================== Desafio 35 ======================')

seg1 = float(input('Digite o primeiro seguimento: '))
seg2 = float(input('Digite o segundo seguimento: '))
seg3 = float(input('Digite o terceiro seguimento: '))

if seg1 + seg2 > seg3 and seg1 + seg3 > seg2 and seg2 + seg3 > seg1:
    print('Com essas medidas, PODE fazer um triângulo!')
else:
    print('Com essas medidas, é IMPOSSÍVEL fazer um triângulo!')
