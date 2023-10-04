# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
# Considere US$1.00 = R$3.27
print('================== Desafio 10 ======================')
investimento = float(input('Quantos reais você quer investir? R$'))
dolar = 4.87
print(f'Você pode comprar {investimento/dolar:.2f} dólares seguindo a cotação de US$1.00 = R${dolar}')
