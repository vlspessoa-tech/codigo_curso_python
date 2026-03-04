"""
split e join com list e str
split - divide uma string (list)
join - une uma string
strip - corta espaços ddo começo e fim da string
rstrip - corta espaços da direita da string
lstrip - corta espaços da esquerda da string
"""
frase = '   Olha só que   , coisa interessante          '
lista_frases_cruas = frase.split(',')

lista_frases = []
for i, frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i].strip())

# print(lista_frases_cruas)
# print(lista_frases)
frases_unidas = ', '.join(lista_frases)
print(lista_frases)