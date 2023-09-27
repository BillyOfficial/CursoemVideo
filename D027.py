# Faça um programa que leia o nome completo de uma pessoa
# Mostrando em seguida o primeiro e o último nome separadamente.

print('================== Desafio 27 ======================')
nome = str(input('Digite seu nome completo: ')).strip().title()
print(f'Seu primeiro nome é {nome[0:nome.find(" ")]} e sobrenome {nome[nome.rfind(" ") +1 :50]}.')
