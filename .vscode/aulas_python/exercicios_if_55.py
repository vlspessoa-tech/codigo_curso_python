'''
Faça um programa que peça ao usuario para digitar um numero inteiro,
informe se este numero é par ou impar, caso o usuario não digite um numero inteiro, informe
que nao é numero inteiro

try:
    numero = int (input("Digite um número inteiro:"))
    calculo = numero / 2 

    if calculo % 2 == 0:
        print("Esse número é par.")

    else: 
        print('Esse número é ímpar') 

except ValueError: 
    print('Esse número não é inteiro') 
'''
'''
Faça um programa que pergunte a hora ao usuario e, baseando-se no 
horario descrito, exiba a saudação apropriada

try:
    hora = int(input("Digite a hora:"))
    minuto = int(input("Digite os minutos:"))
    bom_dia = 0 <= hora <= 11
    boa_tarde = 12 <= hora <= 17
    boa_noite = 18 <= hora <= 23
    if bom_dia:
        print("Bom dia")
    if boa_tarde:
        print("Boa tarde")
    elif boa_noite:
        print("Boa noite")
    else:
        print("Isso não é hora válida")

except ValueError:
    print("Isso não é um número inteiro.")

    

Faça um programa que peça o primeiro nome do usuario. Se o nome tiver 4 etras ou menor, escreva
"Seu nome é curto", se tiver entre 5 e 6 letras, escreva "Seu nome é nomral"
Se tiver mais de 6 escreva que "seu nome é muito grande"

'''

nome = input("Digite seu nome:")
nome_curto = len (nome) <= 4
nome_normal = 5 <= len (nome) <= 6
nome_grande = len (nome) > 6

if nome_curto:
        print("Seu nome é muito curto")
if nome_normal:
        print("Seu nome é normal")
elif nome_grande:
        print("Seu nome é muito grande")
else:
    print("Digite apenas letras")
    