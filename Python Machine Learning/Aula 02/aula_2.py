import random
print(random.random())
print(random.random())
print()

def funcao_random(numero_minimo,numero_maximo):
  diferenca = numero_maximo - numero_minimo
  return diferenca * random.random() + numero_minimo

print(funcao_random(10,20)) 

print(funcao_random(10,20)) 
print()
random.seed(10)

print(random.random()) 

print(random.random()) 

random.seed(10)

print(random.random()) 

print(random.random()) 

random.seed(1234)

print(random.random()) 
print(random.random())
print()

# função uniform ultilizada para gerar números aleatórios de um determinado intervalo
print(random.uniform(10,20))
print()
print(random.normalvariate(0,1)) 
print()
print(random.randint(1, 6))
print()
print(random.randint(1, 6))
dado = [1,2,3,4,5,6]
print(random.choice(dado))
pesos = [1,1,1,1,2,4]
print(random.choices(dado, weights=pesos, k= 10))
print()

baralho = ['Ás de Copas','2 de Copas','3 de Copas','4 de Copas','5 de Copas','6 de Copas','7 de Copas',
'8 de Copas','9 de Copas','10 de Copas','Valete de Copas','Dama de Copas','Rei de Copas']

random.shuffle(baralho)

print(baralho)
print(random.sample(baralho, k = 2))

# Método Monte Carlo, MMC
numero_de_tentativas = 2000000
quantidade_de_acertos = 0

for _ in range(numero_de_tentativas):
  dado_1 = random.randint(1, 6)
  dado_2 = random.randint(1, 6)
  if(dado_1 == dado_2):
    quantidade_de_acertos +=1

print(quantidade_de_acertos/numero_de_tentativas)
print()

import math

print(math.hypot(3, 4))
print()
print(math.dist((1,3),(3,2)))

print(random.choices([1,2,3,4,5,6], k = 10))