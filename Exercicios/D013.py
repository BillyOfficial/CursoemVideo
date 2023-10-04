# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
print('================== Desafio 13 ======================')
salario = float(input('Informe o salário: R$'))
print(f'O salário com acréscimo de 15% é de R${salario+(salario/100*15):.2f}')
