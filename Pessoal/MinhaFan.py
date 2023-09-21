print('Bem vindo ao contador de litros da minha Fan 160!')
v_litro = float(input('Por favor, informe-me sobre o valor atual do litro da gasolina: R$'))
percurso = float(input('Por favor, informe-me a distância em quilômetros que você deseja percorrer: '))
km_da_fan = 38
litro = percurso / km_da_fan
calculo = v_litro * litro
tanque_cheio = litro / 16
print(f'      * O consumo de gasolina será de {litro:.3f} litros.')
print(f'      * E com base no preço atual, você pagará R${calculo:.2f}.')
print(f'      * Será necessário abastecer o tanque {tanque_cheio:.0f} vezes.')
print('      * Para garantir uma viagem segura, eu adicionaria 1 litro a mais.')
