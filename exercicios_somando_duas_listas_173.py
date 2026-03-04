'''
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com valores somados:

Se uma lista for maior que a outra, a soma só vai considerar o tamanho da ModuleNotFoundError
Ex:
lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]

resultado = [2, 4, 6, 8]
'''

def soma_num(lista1, lista2):
    # ou resultado = [x + y for x, y in zip(lista1, lista2)]
    resultado = list(map(sum, zip(lista1, lista2)))
    return resultado

lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]
soma = soma_num(lista_a, lista_b)
print(soma)