from random import sample
print('================== Desafio 20 ======================')
aluno1 = str(input('Digite o nome do aluno: '))
aluno2 = str(input('Digite o nome do aluno: '))
aluno3 = str(input('Digite o nome do aluno: '))
aluno4 = str(input('Digite o nome do aluno: '))
print(f'A ordem é {sample([aluno1, aluno2, aluno3, aluno4], k=4)}.')
