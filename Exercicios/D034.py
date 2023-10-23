# Elabore um programa que solicite o salário de um funcionário
# e calcule o valor do seu reajuste.
# Para salários que ultrapassam R$1.250,00, o reajuste deve ser de 10%.
# Para aqueles que são iguais ou inferiores a este valor, o reajuste deve ser de 15%.

print('================== Desafio 34 ======================')
salario = float(input('Digite o seu salário: '))

if salario >= 1250:
    print(f'O seu salário de R$ {salario:.2f} terá um reajuste de R$ {(salario/100*10)+salario:.2f}.')
if salario < 1250:
    print(f'O seu salário de R$ {salario:.2f} terá um reajuste de R$ {(salario/100*15)+salario:.2f}.')
