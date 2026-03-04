# Crie funcçoes que duplicam, triplicam e quadruplicam
# o número recebido como parâmentro

# def duplo (x):
#     return x + x
# def triplo (x):
#     return duplo (x) + x
# def quadruplo (x):
#     return triplo (x) + x

# numero = float(input('Digite um número: '))

# numero_duplicado = duplo(numero)
# numero_triplicado = triplo(numero)
# numero_quadriplicado = quadruplo(numero)

# print(f'O número {numero:.2f} duplicado é: {duplo(numero):.2f}')
# print(f'O número {numero:.2f} triplicado é: {triplo(numero):.2f}')
# print(f'O número {numero:.2f} quadruplicado é: {quadruplo(numero):.2f}')


#ou assim:

numero = float(input('Digite um número: '))

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadriplicar = criar_multiplicador(4)


print(f'O número {numero:.2f} duplicado é: {duplicar(numero):.2f}')
print(f'O número {numero:.2f} triplicado é: {triplicar(numero):.2f}')
print(f'O número {numero:.2f} quadruplicado é: {quadriplicar(numero):.2f}')

