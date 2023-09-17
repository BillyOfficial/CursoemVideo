# Escreva um programa que leia um valor em metros a o exiba convertido em centímetros e milímetros.
print('================== Desafio 8 ======================')
p1 = int(input('Digite a quantidade de metros que deseja calcular: '))
print(f'O metro informado equivale a:'
      f'\n {p1/1000} quilômetros.'
      f'\n {p1/100} hectômetro.'
      f'\n {p1/10} decâmetro.'
      f'\n {p1} metros.'
      f'\n {p1*10} decímetros.'
      f'\n {p1*100} centímetros.'
      f'\n {p1*1000} milímetros. ')
