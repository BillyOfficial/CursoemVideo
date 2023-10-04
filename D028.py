# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
# E peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import choice
print('================== Desafio 28 ======================')
print("Pensarei em um número de 0 a 5, tente adivinhar!")

aleatorio = choice([1, 2, 3, 4, 5])
tentativa = int(input("Digite um número de 0 a 5: "))

if tentativa > 5:
    print("Por favor, digite um número entre 0 e 5.")
else:
    if aleatorio == tentativa:
        print("Parabéns você acertou!")
    else:
        print(f"Ops, você errou, eu pensei em {aleatorio}")
