# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
print('================== Desafio 12 ======================')
preco = float(input('Digite o preço do produto: '))
print(f'Com o desconto de 5%, o produto fica por: R${preco-(preco/100*5):.2f}')
