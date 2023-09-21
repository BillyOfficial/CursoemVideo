# Faça um programa que leia um número de 0 a 9999.
# E mostre na tela cada um dos dígitos separados.

print('================== Desafio 23 ======================')
number = int(input('Digite um número de 0 a 9999: '))
print(f'Unidade: {number // 1 % 10}\n'
      f'Dezena:  {number // 10 % 10}\n'
      f'Centena: {number // 100 % 10}\n'
      f'Milhar:  {number // 1000 % 10}')
