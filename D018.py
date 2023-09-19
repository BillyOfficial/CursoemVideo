import math
print('================== Desafio 18 ======================')
angulo = float(input('Digite o ângulo desejado: '))

radiano = angulo*3.14/180
seno = math.sin(radiano)
cosseno = math.cos(radiano)
tangente = math.tan(radiano)

print(f'Seno:.......{seno:.2f}\n'
      f'Cosseno:....{cosseno:.2f}\n'
      f'Tangente:...{tangente:.2f}')
