# Faça um programa que leia uma frase.
# E mostre quantas vezes aparece a letra "A"
# Em que posição ela aparece a primeira vez.
# Também em que posição ela aparece a última vez.

print('================== Desafio 26 ======================')
frase = str(input('Digite uma frase: ')).strip().upper()
letra_a = str["A", "Á", "À", "Ã", "Â"]
print(f'Possui {frase.count(letra_a)} letras "a" na frase.')
print(f"A primeira letra fica na {frase.find(letra_a) + 1}ª posição.")
print(f"E a última letra fica na {frase.rfind(letra_a) + 1}ª posição.")
