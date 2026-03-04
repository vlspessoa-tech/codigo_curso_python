"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim

condicao = True

while condicao:
    nome = input('Qual o seu nome: ')
    print(f'Seu nome é {nome}')

    if nome == 'sair':
        break

print('Acabou')



Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim

contador = 0

while contador <= 10:
    contador = contador + 1
    print(contador)

print('Acabou')


contador = 2

while contador <= 10400:
    contador *= 4
    print(contador)

print('Acabou')

contador = 0

while contador <= 100:
    contador += 1
   
    if contador == 6:
     print("Sem o número 6")
     continue

    if contador == 27:
     print("Sem o número 27")
     continue

    if contador >= 90 and contador <= 100:
     print("Sem o número")
     continue

    print(contador)
   
    if contador == 100:
     break
print("Acabou")
"""
qtd_linhas = 5
qtd_colunas = 5
linha = 1
while linha <= qtd_linhas:
    coluna = 1
    

    while coluna <= qtd_linhas:
            print(f'{linha=} {coluna=}')
            coluna += 1
    linha += 1
print("Acabou")