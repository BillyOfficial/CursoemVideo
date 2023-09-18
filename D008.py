# Escreva um programa que leia um valor em metros a o exiba convertido em centímetros e milímetros.
print('================== Desafio 8 ======================')
metro = int(input('Digite a quantidade de metros que deseja calcular: '))
print(f'O metro informado equivale a:'
      f'\n {metro/1000} quilômetros.'
      f'\n {metro/100} hectômetro.'
      f'\n {metro/10} decâmetro.'
      f'\n {metro} metros.'
      f'\n {metro*10} decímetros.'
      f'\n {metro*100} centímetros.'
      f'\n {metro*1000} milímetros. ')
