# Crie um programa que leia três números
# e mostre qual é o maior e qual é o menor.

print('================== Desafio 33 ======================')

numero1 = int(input('Digite o primeiro o número: '))
numero2 = int(input('Digite o segundo o número: '))
numero3 = int(input('Digite o terceiro o número: '))

lista = [numero1, numero2, numero3]
ordem = sorted(lista)

print(f'O menor número é {ordem[0]}')
print(f'O maior número é {ordem[2]}')
