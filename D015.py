print('================== Desafio 15 ======================')
kmperc = float(input('Quantos Km percorridos? Km'))
dias = float(input('Quantos dias foram alugados? '))
print(f'Valor a pagar R${(dias*60)+(0.15*kmperc):.2f}')
