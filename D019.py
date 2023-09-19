from random import choice
print('================== Desafio 19 ======================')
prialuno = str(input('Digite o nome do primeiro aluno: '))
segaluno = str(input('Digite o nome do segundo aluno: '))
teraluno = str(input('Digite o nome do terceiro aluno: '))
quaaluno = str(input('Digite o nome do quarto aluno: '))
print(f'O aluno escolhido foi {choice([prialuno, segaluno, teraluno, quaaluno])}')
