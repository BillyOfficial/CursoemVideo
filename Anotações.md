************************************** Atalhos VS Code **************************************



************************************** Tipos Primitivos **************************************


1. int() - Para números inteiros
     - Exemplo: 13, 01, 12, 21, 99

2. float() - Números de ponto flutuante
     - Exemplo: 7.3, -94.1, 2.2, 14.9

3. bool() - Armazena True ou False
     - Exemplo: True ou False

4. str() - Conjunto de caracteres
     - Exemplo: 'Clorofila', 'cacto', 'eletrodoméstico'

5. type() - Indica o tipo primitivo da variável
     - Exemplo 1: 1. a = 'Arthur' / 2. print(type(a)) / 3. `<class 'str'>`
     - Exemplo 2: 1. a = 1999 / 2. print(type(a)) / 3. `<class 'int'>`
     - Exemplo 3: 1. a = 13.9 / 2. print(type(a)) / 3. `<class 'float'>`
     - Exemplo 4: 1. a = True / 2. print(type(a)) / 3. `<class 'bool'>`


************************************** Operadores Aritméticos **********************************


+  - Adição
-  - Subtração
*  - Multiplicação
/  - Divisão
** - Potencia
// - Divisão inteira
%  - Resto da divisão

- O cálculo é realizado na ordem dos operadores listados acima.


************************************** Módulos **************************************


import - Importa uma biblioteca
     - Exemplo: import math

from - Importa somente a função da biblioteca desejada
     - Exemplo: from math import sqrt
 Neste caso, você só importará a função "sqrt" da biblioteca "math", o que economizará memória.


1. math - Biblioteca de operadores aritméticos


- sqrt() - Raiz Quadrada de um número
     - Exemplo: raiz = math.sqrt(numero)

- floor() - Arredonda o número para baixo
     - Exemplo: 5.23 fica 5.00

- ceil() - Retorna um valor inteiro
     - Exemplo: 5.23 fica 5

- hypot() - Retorna a hipotenusa dos catetos
     - Exemplo: math.hypot(co, ca)

- pow() - Potência de um número
     - Exemplo: pow(2, 3) = 2³ = 8

- radians() - Converte em graus radianos
     - Exemplo: print(math.radians(180))

- cos() - Retorne o cosseno em radianos
     - Exemplo: print(math.cos(math.radians(x)))

- sin() - Retorne o seno em radianos
     - Exemplo: print(math.sin(math.radians(x)))

- tan() - Retorne a tangente em radianos
     - Exemplo: print(math.tan(math.radians(x)))


2. random - Biblioteca que gerar números pseudoaleatórios


- randint() - Retorna um número inteiro no intervalo
     - Exemplo: 1. random.randint(0, 10) / 2. 4

- choice()  - Retorna um elemento aleatório da sequência
     - Exemplo: 1. a = 'Arthur' / 2. random.choice(a) / 3. 't'


************************************** Manipulando Textos **************************************


As strings no python possuem um número para cada caractere, começando a contagem pelo 0.

frase = 'Eu amo python'
'E'=0, 'u'=1, ' '=2, 'a'=3, 'm'=4, 'o'=5, ' '=6, 'p'=7, 'y'=8, 't'=9, 'h'=10, 'o'=11, 'n'=12

frase[?] - Pega os caracteres das posições indicadas
     - Exemplo1: 1. print(frase[4]) / 2. "m"
     - Exemplo2: 1. print(frase[6]) / 2. " "
     - Exemplo3: 1. print(frase[0]) / 2. "E"

frase[?:?] - Pega os caracteres das posições indicadas
     - Exemplo1: 1. print(frase[3:]) / 2. "amo python"
     - Exemplo2: 1. print(frase[0:2]) / 2. "Eu"
     - Exemplo3: 1. print(frase[0:5]) / 2. "Eu am"

frase[?:?:?] - Pega os caracteres das posições indicadas pulando 2
     - Exemplo: 1. frase[0:9:2] / 2. "E m y"

len(?) - Mostra quantas caractere tem a frase
     - Exemplo: 1. print(len(frase)) / 2. 13

count(?) - Conta quantas vezes aparece a palavra/letra/número escolhido.
     - Exemplo: print(frase.count('p'))

find(?) - Diz em qual caractere começa a palavra/letra/número.
     - Exemplo: 1. print(frase.find('amo')) / 2. 3

replace(?) - Troca uma palavra por outra na frase
     - Exemplo: 1. print(frase.replace('amo','odeio')) / 2. Eu odeio python

upper(?) - Colocar todas as outras letras em maiúsculo
     - Exemplo: print(frase.upper()) / 2. EU AMO PYTHON

lower(?) - Colocar todas as outras letras em minusculo
     - Exemplo: print(frase.lower()) / 2. eu amo python

capilalize() - Capitaliza a frase.
     - Exemplo: 1. print(frase.capitalize()) / 2. Eu amo python

title() - Todas as palavras começam com letra maiúscula
     - Exemplo: frase.title()

strip() - Tira o espaço do começo e do fim da frase
     - Exemplo: 1. x = '    Carro     ' / 2. print(x.strip()) / 3. "Carro"

lstrip() - Tira o espaço somente do lado esquerdo.
     - Exemplo: 1. x = '    Carro     ' / 2. print(x.lstrip()) / 3. "Carro     "

rstrip() - Tira o espaço somente do lado direito.
     - Exemplo: 1. x = '    Carro     ' / 2. print(x.rstrip()) / 3. "    Carro"

split() - Vai ocorrer uma divisão entre os espaços da frase
     - Exemplo: frase.split()

'?'.join(?) - Adiciona o caractere/palavra desejado entre os caracteres do parênteses
     - Exemplo1: 1. print('-'.join(frase)) / 2. E-u- -a-m-o- -p-y-t-h-o-n
     - Exemplo2: 1. print('.'.join('Amorzinho')) / 2. A.m.o.r.z.i.n.h.o

************************************** X **************************************



************************************** X **************************************



************************************** X **************************************



************************************** X **************************************
