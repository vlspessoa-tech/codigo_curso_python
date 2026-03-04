''' 
Excicios 1)
nome = "Verônica"
sobrenome = "Luiz de Sousa Pessoa"
idade = 43
ano_nascimento = 2025 - idade
maior_de_idade = ano_nascimento >= 18
altura = 1.68
recolha dados e print
'''
'''
def listas_de_dados ():   
    pessoas = []
    ano_atual = 2026

    while len(pessoas) < 3:
        nome = input('Digite seu nome: ').strip().capitalize()
        if not nome.isalpha():
            print('Digite apenas letras.')
            continue

        sobrenome = input('Digite seu sobrenome: ').strip().capitalize()
        if not sobrenome.isalpha():
            print('Digite apenas letras.')
            continue

        idade_txt = input('Digite sua idade: ').strip()
        if not idade_txt.isdigit():
            print('Digite apenas números inteiros.')
            continue
        idade = int(idade_txt)

        if not (0 <= idade <= 120):
            print('Idade fora do intervalo esperado (0 a 120).')
            continue

        nasc_txt = input('Digite seu ano de nascimento: ').strip()
        if not nasc_txt.isdigit():
            print('Digite apenas números inteiros.')
            continue
        nascimento = int(nasc_txt)

        if not (1900 <= nascimento <= ano_atual):
            print(f'Ano inválido. Digite entre 1900 e {ano_atual}.')
            continue

        # coerência (tolerância de 1 ano)
        if abs((ano_atual - nascimento) - idade) > 1:
            print('Você digitou idade ou ano errado (incoerentes).')
            continue

        pessoas.append({
            'nome': nome,
            'sobrenome': sobrenome,
            'idade': idade,
            'nascimento': nascimento
        })

    return pessoas


def maior_de_idade (pessoa):
    return 'Você é maior de idade.' if pessoa['idade'] >= 18 else 'Você é menor de idade.'


lista = listas_de_dados()
for pessoa in lista:
    print(
        f"Nome completo: {pessoa['nome']} {pessoa['sobrenome']} | "
        f"Idade: {pessoa['idade']} | "
        f"Nascimento: {pessoa['nascimento']} | "
        f"{maior_de_idade(pessoa)}"
    )

'''
'''
----------------------------------------------------------------------------------------------------
Excicios 2)
nome:
sobrenome:
Altura:
imc:
'''
'''
def recebe_dados ():
    pessoa = []
    while len(pessoa) < 3:
        nome = input('Digite seu nome: ').strip().capitalize()
        if not nome.isalpha():
            print('Digite apenas letras.')
            continue
        sobrenome = input('Digite seu sobrenome: ').strip().capitalize()
        if not sobrenome.isalpha():
            print('Digite apenas letras.')
            continue
        altura_txt = input('Digite sua altura (ex: 1.75): ').strip().replace(",", ".")
        try:
            altura = float(altura_txt)
            if not (0.5 <= altura <= 2.5):
                print("Altura fora do intervalo esperado.")
                continue
        except ValueError:
            print('Altura inválida. Digite um número (ex: 1.75).')
            continue

        peso_txt = input('Digite seu peso (kg, ex: 80.5): ').strip().replace(",", ".")
        try:
            peso = float(peso_txt)
            if not (2 <= peso <= 350):
                print("Peso fora do intervalo esperado.")
                continue
        except ValueError:
            print('Peso inválido. Digite um número (ex: 80.5).')
            continue
        pessoa.append({'nome': nome, 'sobrenome': sobrenome, 'peso': peso, 'altura': altura})
    return pessoa

def calculo_imc (pessoa):
    peso = pessoa['peso']
    altura = pessoa['altura']
    return float(peso) / (float(altura ** 2))

def tabela_obesidade (imc):
    imc = float(imc)
    if imc < 18.5:
        return 'Você está muito magro!'
    elif 18.5 <= imc <= 24.9:
        return 'Você está normal!'
    elif 25 <= imc <= 29.9:
        return 'Você está de sobrepeso!'
    elif 30 <= imc <= 39.9:
        return 'Você está com obesidade!'
    else:
        return 'Você está com obesidade grave!'
     
imprime_lista = recebe_dados()
for pessoa in imprime_lista:
    imc = calculo_imc(pessoa)
    resultado = tabela_obesidade(imc)
    print(
         f"Nome completo: {pessoa['nome']} {pessoa['sobrenome']} | "
    f"Peso: {pessoa['peso']} kg | "
    f"Altura: {pessoa['altura']} m | "
    f"IMC: {imc:.1f} | "
    f"{resultado}"
    )

'''
'''
---------------------------------------------------------------------------------------------
Excicios 3)
Calcular uma lista com varios valores recebidos e dizer qual o maior e qual o menor
'''
'''
def lista_valores ():
    lista = []
    while len(lista) < 5:
        valor_txt = input('Digite um número: ').strip()
        try:
            valor_dado = float(valor_txt)
            lista.append(valor_dado)
        except ValueError:
            print('Digite apenas números.')
            continue

    return lista

def maior_menor(lista):
    maior = min(lista)
    menor = max (lista)
    return maior,menor
            
valores = lista_valores()
maior, menor = maior_menor(valores)
print(f"Lista digitada: {valores}")
print(f"Maior número: {maior}")
print(f"Menor número: {menor}")

'''
'''
-------------------------------------------------------------------------------------------------------
Excicios 4)
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
'''
'''
try:
    nome = input('Digite seu nome: ').capitalize()
    idade = int(input('Digite sua idade: '))
    print('Seu nome é: ', nome)
    print('Seu nome inertido é: ', nome[::-1])
    if ' ' in nome:
        print('Seu nome tem espaço.')
    else:
        print('Seu nome não tem espaço')
    print('Seu nome tem ', len(nome), 'letras')
    print('A primeira letra do seu nome é: ', nome[0])
    print('A última letra do seu nome é: ', nome[-1])
except ValueError:
    print('Digite nome (somente letras) e idade (somente números!)')
'''

'''
-------------------------------------------------------------------------------------------------
Excicios 5)
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
'''
'''
try:
    numero_usuario = int(input('Digite um número inteiro: '))
    if numero_usuario % 2 == 0:
      print('Esse número é par!')
    else:
      print('Esse número é ímpar!')
except ValueError:
     print('Digite apenas um número inteiro!')
'''
'''
----------------------------------------------------------------------------------------------------
Excicios 5.1)
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
'''
'''
nome = input('Digite seu nome: ').capitalize()
try:
    hora = int(input('Digite a hora atual:'))
    minuto = int(input('Digite os minutos atuais:'))
    if hora >= 0 and hora < 12:
        print('Bom dia! ', nome)
    elif hora >= 12 and hora < 18:
        print('Boa tarde! ', nome)
    else:
        print('Boa noite, ', nome)
except ValueError:
    print('Digite apenas números inteiros!')
'''
"""
---------------------------------------------------------------------------------------------------
Excicios 5.2)
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
"""
nome = input('Digite seu nome: ').capitalize()
try:
    if len(nome) < 4:
        print('Seu nome é muito curto!')
    if len(nome) >= 4 and len(nome) < 7:
        print('Seu nome é normal!')
    else:
        print('Seu nome é muito grande!')
except ValueError:
    print('Nome errado! Digite seu nome:')
"""
"""
---------------------------------------------------------------------------------------------------
Excicios 6)

Iterando strings com while
"""
'''
#       012345678910
nome = 'Luiz Otávio'  # Iteráveis
#      1110987654321
tamanho_nome = len(nome)
print(nome)
print(tamanho_nome)
print(nome[3])

nova_string = ''
nova_string += '*L*u*i*z* *O*t*á*v*i*o'
'''
'''
frase = 'Veronica Luiz de Sousa Pessoa '
i = 0
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''

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
    'A letra que apareceu mais vezes foi '
    f'"{letra_apareceu_mais_vezes}" que apareceu '
    f'{qtd_apareceu_mais_vezes}x'
)
"""
"""
--------------------------------------------------------------------------------------------------------
Excicios 7)
 Calculadora com while 
while True:
    print('nummmmm')
    #########
    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break
'''
'''
def num_1():
    while True:
        try:
            return float(input('Digite um numero. '))
        except ValueError:
            print('Digite penas apenas números: ')
        
def op():
    while True:    
        try:
            operador = input('Digite um operador: ')
            if operador in ['*', '/', '-', '+']:
                return operador
        except ValueError:
             print('Digite somente: /, *, - ou +')
           
def num_2():
    while True:
        try:
            segundo_numero = float(input('Digite o segundo número:'))
            return segundo_numero
        except ValueError:
            print('Digite apenas números: ')
    
def calculo(primeiro_numero, segundo_numero, operador):
    if operador == '+':
        resultado = primeiro_numero + segundo_numero
    elif operador == '-':
        resultado = primeiro_numero - segundo_numero
    elif operador == '/':
        resultado = primeiro_numero / segundo_numero
    else:
        resultado = primeiro_numero * segundo_numero
    return resultado

while True:
    primeiro_numero = num_1()
    operador = op()
    segundo_numero = num_2()

    resultado = calculo(primeiro_numero, segundo_numero, operador)

    if resultado is not None:
        print(f"{primeiro_numero} {operador} {segundo_numero} = {resultado}")
    
    sair = input('Quer sair? [S]im: ').lower().startswith('s')
    if sair:
        break

'''
'''
----------------------------------------------------------------------------------------------------------
Excicios 8)

Faça um jogo para o usuário adivinhar qual a palavra secreta.
- Você vai propor uma palavra secreta qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na  palavra secreta; exiba a letra;
    - Se a letra digitada não estiver na palavra secreta; exiba *.
Faça a contagem de tentativas do seu usuário.
'''
'''
import os

palavra_secreta = 'perfume'
letras_acertadas = ''
numero_tentativas = 0

while True:
    letra_digitada = input('Digite uma letra: ')
    numero_tentativas += 1

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print('Palavra formada:', palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system('clear')
        print('VOCÊ GANHOU!! PARABÉNS!')
        print('A palavra era', palavra_secreta)
        print('Tentativas:', numero_tentativas)
        letras_acertadas = ''
        numero_tentativas = 0
        break
'''
'''
---------------------------------------------------------------------------------------------------------
Excicios 9)

Exercício
Exiba os índices da lista
0 Maria
1 Helena
2 Luiz

'''
'''
lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')
for i in enumerate(lista):
    print(i)
'''
'''
----------------------------------------------------------------------------------------------------------
Excicios 11)
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
'''
'''
def cpf_nove():
    while True:
        cpf_nove_digitos = input('Digite os 9 números do seu CPF: ').strip()

        if cpf_nove_digitos.isdigit() and len(cpf_nove_digitos) == 9:
            return cpf_nove_digitos
        print("Entrada inválida. Digite exatamente 9 números.")
        break

cpf = cpf_nove()
def soma_cpf(cpf_nove):
    print(f'Os 9 números do CPF digitado foram: ', cpf) 
    cont_regressiva = 10
    soma = 0
    for i in str(cpf):
        soma += int(i) * cont_regressiva
        cont_regressiva -= 1 
    return soma

soma = soma_cpf(cpf_nove)
def cpf_vezes_10():
    print(f'A soma dos 9 dígitos é: ', soma) 
    soma_num_por_dez = soma * 10
    return soma_num_por_dez

mult = cpf_vezes_10()
def resto_divisao():
    print(f'A soma dos 9 dígitos x 10 é: ', mult) 
    resto = mult % 11
    if resto > 9:
        return 0
    return resto

resto = resto_divisao()
print(f'O primeiro dígito do seu CPF é: ', resto)
     
def cpf_dez():
    cpf2 = str(cpf)
    resto2 = str(resto)
    cpf_completo2= cpf2 + resto2
   # cpf_dez_dig = int(cpf_completo2)
    return cpf_completo2

cpf2 = cpf_dez()
def soma_cpf2(cpf_dez):
    print(f'Os 10 números do CPF são: ', cpf2) 
    cont_regressiva1 = 11
    soma1 = 0
    for i in cpf2:
        soma1 += int(i) * cont_regressiva1
        cont_regressiva1 -= 1 
    return soma1

soma2 = soma_cpf2(cpf_dez)
def cpf_vezes_10_2():
    print(f'A soma dos 10 dígitos é: ', soma2) 
    soma_num_por_dez = soma2 * 10
    return soma_num_por_dez

mult2 = cpf_vezes_10_2()
def resto_divisao2():
    print(f'A soma dos 10 dígitos x 10 é: ', mult2) 
    resto1 = mult2 % 11
    if resto1 > 9:
        return 0
    return resto1

resto2 = resto_divisao2()
print(f'O útltimo dígito do seu CPF é: ', resto2)

'''
'''
----------------------------------------------------------------------------------------------------
Excicios 12)
Crie uma função que multiplica todos os argumentos
não nomeados recebidos
Retorne o total para uma variável e mostre o valor
da variável.
'''
'''    
recebido = input('Digite um número: ')
recebido_tratado = []
for i in recebido:
    recebido_tratado += i


def multiplica(*args):
    total = 1
    for numero in args:
        total *= int(numero)
    return (total)

print(multiplica(*recebido_tratado))

-------------------------------------------------------------------------
Excicios 13)
Crie funcçoes que duplicam, triplicam e quadruplicam
o número recebido como parâmentro


numero = int(input('Digite um número: '))

def multiplica():
    duplo = numero * 2
    return duplo
def triplica():
    triplo = numero * 3
    return triplo
def quadriplica():
    quadruplo = numero * 4
    return quadruplo

print(f'O número ',numero, 'duplicado é: ', multiplica())
print(f'O número ',numero, 'triplicado é: ', triplica())
print(f'O número ',numero, 'quadriplicado é: ', quadriplica())


'''
'''
--------------------------------------------------------------------------
Excicios 14)

print('------Quiz de perguntas------')

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]
acertos = 0
erros = 0
for pergunta in perguntas:
    print(f'Pergunta:', pergunta['Pergunta'])

    opcoes = pergunta ['Opções']
    for i, valor in enumerate(opcoes, start=1):
        print(f'{i}) ', valor)
    while True:
        try:
            resposta = int(input('Digite a sua opção: '))
            if resposta not in [1, 2, 3, 4]:
                raise ValueError
        except ValueError:
            print('Digite apenas as opções: 1, 2, 3 ou 4')
        else:
            break
    escolhida = opcoes[resposta - 1]
    validacao = pergunta['Resposta']
   
    if escolhida == validacao:
        acertos += 1
        print('Acertou! 👌')
    else:
        erros += 1
        print('Errou! 🤦‍♀️')

print(f'Você acertou {acertos} e errou {erros}.')
'''
'''
--------------------------------------------------------------------------------
Excicios 15)

Exercício
Crie uma função que encontra o primeiro duplicado considerando o segundo
número como a duplicação. Retorne a duplicação considerada.
Requisitos:
    A ordem do número duplicado é considerada a partir da segunda
    ocorrência do número, ou seja, o número duplicado em si.
    Exemplo:
        [1, 2, 3, ->3<-, 2, 1] -> 1, 2 e 3 são duplicados (retorne 3)
        [1, 2, 3, 4, 5, 6] -> Retorne -1 (não tem duplicados)
        [1, 4, 9, 8, ->9<-, 4, 8] (retorne 9)
    Se não encontrar duplicados na lista, retorne -1
'''
'''
lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]


def primeiro_duplicado(lista):
    visto = set()

    for numero in lista:    
        if numero in visto:
            return numero
        visto.add(numero)
    return -1

for lista in lista_de_listas_de_inteiros:
    print(lista, f'-->',primeiro_duplicado(lista))
'''