# Desafio 22
# Crie um programa que leia o nome completo de uma pessoa @feito
# e mostre:
# O nome com todas as letras maiúsculas.
# O nome com todas as letras minúsculas.
# Quantas letras no total sem considerar espaços.
# Quantas letras possui no primeiro nome.

print('================== Desafio 22 ======================')
name = str(input('Digite o seu nome completo: '))
nspace = name.strip()
print(nspace.upper())  # Letra maior
print(nspace.lower())  # Letra menor
print(len(nspace)-nspace.count(' '))  # Contar as letras - space
print(len(nspace.split()[0]))  # Quantas letras no primeiro name

# Arthur da Conceição Ferreira
