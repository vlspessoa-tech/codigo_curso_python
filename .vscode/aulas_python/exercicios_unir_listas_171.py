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
lista_estado = ['Salvador', 'Ubatuba', 'Belo Horizonte']
lista_sigla = ['BA', 'SP', 'MG', 'RJ']
print(list(zip(lista_estado, lista_sigla)))
print(list(zip_longest(lista_estado, lista_sigla, fillvalue='Sem cidade')))

#ou assim

def zipper (lista1, lista2):
    intervalo = min(len(lista1), len(lista2))
    return [
        (lista1[i], lista2[i]) for i in range(intervalo)
    ]
    

lista_estado = ['Salvador', 'Ubatuba', 'Belo Horizonte']
lista_sigla = ['BA', 'SP', 'MG', 'RJ']

print(zipper(lista_estado, lista_sigla))

