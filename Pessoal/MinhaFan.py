print('Bem vindo ao contador de litros da minha Fan 160!')
v_litro = float(input('Digite qual é o preço do litro da gasolina hoje: R$'))
percurso = float(input('Agora digite o percurso em KM a ser percorrido: '))
km_da_fan = 38
litro = percurso / km_da_fan
calculo = v_litro * litro
tanque_cheio = litro / 16
print(f'      * Você gastará {litro:.3f} litros de gasolina.')
print(f'      * E de acordo com o preço atual, você pagara R${calculo:.2f}.')
print(f'      * É necessário encher o tanque {tanque_cheio:.0f} vezes.')
print('      * Para garantir uma viagem segura, eu colocaria 2 litro a mais.')
