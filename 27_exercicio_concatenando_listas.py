# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

from itertools import zip_longest

lista_1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
lista_2 = ['BA', 'SP', 'MG', 'RJ']


def concatena_listas(lista1=[], lista2=[]):
    internal = min(len(lista1), len(lista2))
    return [(lista1[i], lista2[i]) for i in range(internal)]


print(list(zip(lista_1, lista_2)))
print(concatena_listas(lista_1, lista_2))
print(list(zip_longest(lista_1, lista_2)))
