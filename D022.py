# Desafio 22
# Crie um programa que leia o nome completo de uma pessoa @feito
# e mostre:
# O nome com todas as letras maiúsculas.
# O nome com todas as letras minúsculas.
# Quantas letras no total sem considerar espaços.
# Quantas letras possui no primeiro nome.
print('================== Desafio 22 ======================')
name = str(input('Digite o seu nome completo: ')).strip()
print(name.upper())  # Letra maior
print(name.lower())  # Letra menor
print(len(name)-name.count(' '))  # Contar as letras menos o space
print(len(name.split()[0]))  # Quantas letras no primeiro name
