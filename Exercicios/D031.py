# Crie um programa que solicite a distância de uma viagem em quilômetros.
# O programa deve calcular o custo da passagem,
# cobrando R$0.50 por quilômetro para viagens de até 200km,
# e R$0.45 por quilômetro para viagens mais longas.

print('================== Desafio 31 ======================')
print('Bem vindo ao programa de cálculo de Quilômetros!')
km = float(input('Digite quantos km serão a viagem: '))
menos200 = km * 0.50
mais200 = km * 0.45

if km < 200:
    print(f'A passagem custa R${menos200:.2f}')
else:
    print(f'A passagem custa R${mais200:.2f}')
