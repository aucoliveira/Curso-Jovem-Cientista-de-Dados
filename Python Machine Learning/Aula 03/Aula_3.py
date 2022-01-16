import numpy as np

matriz1d = np.array([1,2,3]) # Matriz com 1 dimensão
matriz2d = np.array([[1,2,3], [4,5,6], [7,8,9]]) # Matriz com 2 dimensões

print(matriz1d * 2)
print(matriz1d + matriz1d)
print(matriz2d.shape)
print([1,2,3] + [4,5,6])
print(np.array([1,2,3]) + np.array([4,5,6]))
print()
print([1,2,3]*3)
print(np.array([1,2,3])*3)
print()
matriz3d = np.array([[[1,2,3], [4,5,6], [7,8,9]],[[10,11,12], [13,14,15], [16,17,18]]]) # Matriz com 3 dimensões
print('Numero de dimensões',matriz1d.ndim)
print('Numero de dimensões',matriz2d.ndim)
print('Numero de dimensões',matriz3d.ndim)
print()
print(matriz1d.shape) # Matriz 1 é um vetor de dimensão 1
matriz2d2 = np.array([[20, 12, 10], [16, 55, 45], [33, 27, 18]])
print(matriz2d + matriz2d2)
print()
print(matriz2d2 - matriz2d)
print()
print(matriz2d*2)
print()
print(np.dot(matriz2d, matriz2d2)) # [[151 203 154] [358 485 373] [565 767 592]]
print(np.dot(matriz2d2, matriz2d)) # [[138 180 222] [551 667 783] [267 345 423]]
matriz23 = np.array([[1, 2, 3], [4, 5, 6]])
print(matriz23.shape) # (2, 3)
print(np.dot(matriz23, matriz2d)) # [[30 36 42] [66 81 96]]
# print(np.dot(matriz2d, matriz23)) # ValueError: shapes (3,3) and (2,3) not aligned: 3 (dim 1) != 2 (dim 0)
print()
ponto_original = np.array([3, 4])
rotacao = np.array([[-1.0, 0.0], [0.0, -1.0]])
ponto_rotacionado = np.dot(rotacao, ponto_original)
print(ponto_rotacionado)
tranlacao = np.array([5.0, 0.0])
ponto_transladado = ponto_original + tranlacao
print(ponto_transladado)
escala = 2
ponto_escalonado = ponto_original * escala
print(ponto_escalonado)
print()
print(np.zeros((1, 3))) # [[0. 0. 0.]]
print(np.ones((2, 2))) # [[1. 1.] [1. 1.]]
print(np.full((1, 2), 3)) # [[3 3]]
print(np.full((2, 1), np.nan)) # [[nan] [nan]]
print()
matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matriz) # [[1 2 3] [4 5 6] [7 8 9]]
print(matriz[1, 1]) # 5
print(matriz[:, 1]) # [2, 5, 8]
print(matriz[0, :]) # [1, 2, 3]
print(matriz[:2, 1:]) # [[2, 3], [5, 6]
print()
vendas_anos = np.array([[149, 499, 112, 430, 115, 390, 187, 316, 361, 483, 353, 400],
[258, 222, 461, 263, 384, 210, 452, 372, 417, 364, 468, 397],
[259, 329, 417, 132, 318, 256, 362, 496, 232, 132, 306, 174],
[117, 148, 480, 201, 160, 292, 146, 209, 298, 215, 358, 234],
[169, 229, 381, 119, 225, 270, 379, 272, 167, 332, 144, 359],
[358, 434, 228, 300, 122, 247, 142, 127, 191, 356, 450, 308],
[105, 251, 317, 147, 214, 280, 289, 338, 498, 133, 304, 225],
[156, 165, 299, 461, 290, 123, 451, 450, 353, 191, 167, 451],
[149, 377, 389, 176, 103, 439, 269, 132, 200, 391, 426, 175],
[137, 107, 229, 227, 198, 206, 432, 169, 323, 141, 155, 233]])
print(vendas_anos.shape)
# Calculando a média de uma matriz
print(np.mean(vendas_anos))
print(vendas_anos.mean())
primeiro_ano = vendas_anos[0, :]
print(primeiro_ano)
print(primeiro_ano.shape)
print(primeiro_ano.mean())
print(primeiro_ano.mean(axis=0)) # Calculando a media do ano passado no parametro da linha 72
# Calculando a média por anos e meses
media_ano = vendas_anos.mean(axis=1)
print(media_ano)
print(media_ano.shape)
media_meses = vendas_anos.mean(axis=0) # Calculando a média dos meses
print(media_meses)
print(media_meses.shape)
print()
# Calculando a soma de todas as vendas de todos os anos e obtendo a maior venda
soma_ano = vendas_anos.sum(axis=1)
print(soma_ano.shape)
print(soma_ano)
maximo_vendas_anuais = soma_ano.max()
print(maximo_vendas_anuais)
# Encontrando o indice que tem o maior valor no array ultilizando o argmax()
indice_max = soma_ano.argmax()
print(indice_max)
print(soma_ano[indice_max])
print()
vendas_mes = vendas_anos.sum(axis=0)
print(vendas_mes.shape)
maximo_vendas_mes = vendas_mes.max()
print(maximo_vendas_mes)
indice_mes_max = vendas_mes.argmax()
print(vendas_mes[indice_mes_max])
print()
# Exemplo do curso 
import locale
from datetime import datetime
#locale.setlocale(locale.LC_ALL, 'pt_BR')
anos = np.arange(2011, 2021)
meses = list(map(lambda x: datetime.strptime(str(x), "%m"), np.arange(1, 13)))
meses = list(map(lambda x: x.strftime("%B").title(), meses))
print(anos)
print(meses)

for i in range(len(anos)):
    indice_max_ano = vendas_anos[i, :].argmax()
    maior_venda_ano = vendas_anos[i, indice_max_ano]

print(f"A maior venda de {anos[i]} ocorreu no mês de {meses[indice_max_ano]} e foi de {maior_venda_ano} computadores")
print()
# ultilizando máscara
import numpy.ma as ma
dados_invalidos = np.array([1, 2, 3, np.nan, 5])
dados_mascarados = ma.masked_array(dados_invalidos, mask=[False, False, False, True, False])
print(dados_mascarados)

