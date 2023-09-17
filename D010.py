# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
# Considere US$1.00 = R$3.27
print('================== Desafio 10 ======================')
p1 = int(input('Quantos reais você quer investir? '))
dolar = 3.27
print(f'Você pode comprar {p1//dolar} dólares seguindo a cotação de US$1.00 = R${dolar}')
