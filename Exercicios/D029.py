# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada km acima do limite.

print('================== Desafio 29 ======================')
print('Este é um teste de velocidade.')
speed = int(input('Digite a velocidade do carro: '))

multa = (speed - 80) * 7

if speed <= 80:
    print('Tudo certo! Liberado.')
else:
    print(f'Você foi multado. O valor da multa é de R${float(multa):.2f}')
