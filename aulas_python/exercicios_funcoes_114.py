# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

# def multiplica(*args):
#     total = 1
#     for numero in args:
#         total *= numero
#     return (total)

# numeros = 1,2,3,4,5,6
# print(multiplica(*numeros))
# print(1*2*3*4*5*6)



# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

def par_impar(x):
    if x % 2 == 0:
        return f'{x} é par'
    return f'{x} é ímpar'
#----------------------------------------- ou
#         x = 'par'
#         print ('O número é par')
#     else:
#         x = 'ímpar'
#         print ('O número é ímpar')
#     return x
#-------------------------------------------
  

numero = 8

print(par_impar(numero))