# Crie um programa que leia o nome de uma cidade.
# E diga True se ele começa com o nome "SANTO".

print('================== Desafio 24 ======================')
cidade = (str(input('Digite o nome da cidade: '))).strip().capitalize()
print(cidade.find('Santo') == 0)
