# Faça um programa que leia uma frase.
# E mostre quantas vezes aparece a letra "A"
# Em que posição ela aparece a primeira vez.
# Também em que posição ela aparece a última vez.

print('================== Desafio 26 ======================')
frase = str(input('Digite uma frase: ')).strip().upper()
print(f'Possui '
      f'{frase.count("A") + frase.count("Á") + frase.count("Ã") + frase.count("Â") + frase.count("À")} '
      f'letras "a" na frase.')
print(f"A primeira letra fica na {frase.find('A') + 1}ª posição.")
print(f"E a última letra fica na {frase.rfind('A') + 1}ª posição.")

