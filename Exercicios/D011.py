# Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta pinta uma área de 2m².
print('================== Desafio 11 ======================')
lar = float(input('Digite a largura: '))
alt = float(input('Digite a altura: '))
print(f'Você tem {lar*alt} metros quadrados para pintar!')
print(f'Você gastaria {lar*alt/2:.2f} litros.')


