""" while/else 
string = 'Valor qualquer'

i = 0
while i < len(string):
    letra = string[i]

    if letra == ' ':
        break

    print(letra)
    i += 1
else:
    print('Não encontrei um espaço na string.')
print('Fora do while.')
"""
frase = 'aaaa e    aiiiiiiiaaaa uuuuuaaa.'
i = 0
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ' '

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    qtd_apareceu_mais_vezes_atual = frase.count(letra_atual)

    if qtd_apareceu_mais_vezes < qtd_apareceu_mais_vezes_atual:
       qtd_apareceu_mais_vezes = qtd_apareceu_mais_vezes_atual
       letra_apareceu_mais_vezes = letra_atual

    i += 1

print(
    'A letra que apareceu mais vezes foi o '
    f'"{letra_apareceu_mais_vezes}" com '
    f'{qtd_apareceu_mais_vezes} vezes'
)
