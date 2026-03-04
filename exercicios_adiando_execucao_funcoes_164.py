# Exercício - Adiando execução de funções
def soma(x, y):

    return x + y


def multiplica(x, y):
    return x * y


def criar_funcao(funcao, *args):
    def nova_funcao (*args_restantes):
        return funcao(*args, *args_restantes)
    return nova_funcao


soma_com_cinco = criar_funcao(soma, 5)
print(soma_com_cinco(10))
multiplica_por_dez = criar_funcao(multiplica, 10)
print(multiplica_por_dez(10))