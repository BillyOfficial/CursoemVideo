# Desenvolva um programa que solicite a entrada de um ano específico
# e determine se esse ano é bissexto.

print('================== Desafio 32 ======================')

ano = int(input("Digite o ano: "))

if ano % 4 == 0:
    print('É um ano bissexto!')
else:
    print('Não é um ano bissexto!')
