import copy
# copy, sorted, produtos.sort
# Exercícios
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]
print(f'Tabela original',*produtos, sep='\n')
print()
print('\n Exercício 1')
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
novos_produtos = [
    {**p, 'preco': round(p['preco'] * 1.1, 2)}
    for p in copy.deepcopy(produtos)
]
print(*novos_produtos, sep='\n')
print('\n Exercício 2')
# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
produtos_ordenados_por_nome = sorted(copy.deepcopy(produtos), key=lambda x : x['nome'], reverse=True)
print(*produtos_ordenados_por_nome, sep='\n')

print('\n Exercício 3')
# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
produtos_ordenados_por_preco = sorted(copy.deepcopy(produtos), key=lambda x : x['preco'])
print(*produtos_ordenados_por_preco, sep='\n')


#ou assim com list comprehension

