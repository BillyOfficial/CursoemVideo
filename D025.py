# Crie um programa que leia o nome de uma pessoa.
# E diga se ela tem "SILVA" no nome.

print('================== Desafio 25 ======================')
nome = (str(input('Digite um nome completo: '))).strip().title()
nome2 = nome.find('Silva') + 1
print(f'Você tem o sobrenome Silva? {bool(nome2)}')
