# lista é mutável
'''
nome = ['Maria', 'Helena', 'Luiz']
nome0, nome1, nome2 = nome
nome[0] = 'Mara'

print(nome[2])
print(nome2)
print(nome[1:3])
print(nome[0:3])
'''
# tupla é uma lista imutável
nome = 'Maria', 'Helena', 'Luiz'
print(nome[0])
nome[0] = 'Mara' # Não é possivel mudar tupla por ser imutavel
