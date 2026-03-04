# 1-Peça um número ao usuário e informe se é par ou ímpar.
# par_impar = (input('Digite um número: '))
# if par_impar % 2 == 0:
#     print('Número par!')
# else:   
#     print('Número ímpar!')

# 2-Peça dois números e uma operação (+ - * /) e retorne o resultado.
# numero1 = (input('Digite um número: '))
# numero2 = (input('Digite outro número: '))
# def soma(x, y):
#     return x + y
# def subtracao(x, y):
#     return x - y
# def multiplicacao(x, y):
#     return x * y
# def divisao(x, y):
#     return x / y

# print(f'Soma de ', numero1, '+', numero2, 'é:', soma(numero1,numero2))
# print(f'Subtração de ', numero1, '-', numero2, 'é:', subtracao(numero1,numero2))
# print(f'Divisão de ', numero1, '/', numero2, 'é:', divisao(numero1,numero2))
# print(f'Multiplicação de ', numero1, '*', numero2, 'é:', multiplicacao(numero1,numero2))

# 3-Leia três números e informe qual é o maior.
# num = []
# num.append((input('Digite um númmero: ')))
# num.append((input('Digite um númmero: ')))
# num.append((input('Digite um númmero: ')))

# num = sorted((num), key=lambda x : x)
# print('O maior número dos 3 é: ', num[2])

# 4-Crie um sistema que só aceita senha com: mínimo 8 caracteres, pelo menos 1 número e 
# pelo menos 1 letra maiuscula

# senha = ''  

# def senha():
#     while True:
#         senha = input('Digite uma senha: ') 
#         maiuscula (char.isupper() for char in senha)
#         tamanho = len(senha) >= 8
#         numero (char.isdigit() for char in senha)
#         if not maiuscula:
#             print('Digite ao menos uma letra maiúscula: ')
#         if not tamanho:
#             print('Digite ao menos 8 caracteres:')
#         if not numero:
#             print('Digite pelo menor um número: ')
#         else:
#             return 'Senha aceita!'
# print(senha())

# 5-Imprintima de 10 até 0 uso while.
# numero = [0,1,2,3,4,5,6,7,8,9,10]
# decr = 11
# incr = 1
# item = 0
# while item < 10:
#     for item in numero:
#         incr += item * decr
#         decr -= 1
#         print(decr)
# 6-Lista de comprintas: Permita que o usuário: adicione itens, remova itens, visualize lista e 
# Use lista e while.

# menu = {
#     'A ': ' Adicionar item',
#     'R ': ' Remover item',
#     'V ': ' Visualizar lista',
#     'S ': ' Sair\n'
# }
    
# lista =[]
# while True:
#     print(f'Selecione uma opção:\n')
#     for chave, valor in menu.items():
#         print(f'{chave.upper()}:{valor}')
    
#     item = input('Digite uma opção: ').upper()
#     if item == 'A':
#         novo_item = input('Digite novo item: ').capitalize()
#         lista.append(novo_item)
#         print('Adicionado', novo_item, 'na lista!')
#         print(lista)
                    
#     elif item == 'R':
#         if not lista:
#             print("⚠️ A lista está vazia.")
#         else:
#             print(lista)
#             remover_item = input('Digite o item a ser removido: ')
#             if remover_item in lista:
#                 lista.remove(remover_item)
#                 print('Removido', remover_item, 'da lista!')
#             else:
#                 print('Item não ncontrado!')
        
#     elif item == 'V':
#         if not lista:
#             print('Lista vazia!')
#         else:
#             for item in lista:
#                 print(item)
#             #continue
        
#     elif item == 'S':
#         print ('Saindo...')
#         break
    
#     else: 
#         print('Opção inválida! Tente novamente!')
       
# 7-Receba várias notas até o usuário digitar "sair" e calcule a média.
# import re
# lista = []

# while True:
#     entrada = input('Digite as notas. Ao terminar, digite "S" para sair.')
#     notas = re.sub(r'[^a-zA-Z0-9.]', "", entrada)
#     try:
#         if notas.upper() != 'S'  not notas.isalpha():
#             lista.append(notas)
#             print(lista)
#             print('Digite nova nota ou "S" para sair.')
#         elif notas == 's':
#             print('Saindo...')
#             break

#     except ValueError:
#         print('Erro ao digitar!')

# lista_espacos = [s for s in lista if s.strip()]
# lista_ = [float(i) for i in lista_espacos]
# soma = sum(lista_)
# media = soma / len(lista_)
# print(f'A média das notas é: ', media)    

# 8-Peça uma frase e: conte palavras, conte letras (sem espaços) e diga qual palavra é maior
# frase_crua = input('Digite uma frase: ').strip()
# conte_palavras = frase_crua.split()
# maior_palavra = max(conte_palavras, key=len)
# frase = [s for s in frase_crua if s.strip()]
# conte_letra = len(frase)
# print(f'A frase digitada foi:',frase_crua.capitalize(), '\nEssa frase contém', len(conte_palavras), 'palavras!',
#     '\nEssa frase contém', conte_letra, 'letras!','\nA maior palavra é: ', maior_palavra)

# 9-Sem usar [::-1], inverta uma string manualmente.
# normal = input('Digite qualquer coisa: ')
# invertida = ''.join(reversed(normal))
# print(invertida)

# 10-Dada uma lista: numeros = [1,2,2,3,3,3,4,4,4,4] Retorne um dicionário com a frequência.
#Uso collections.Counter
# from collections import Counter
# numeros = [1,2,2,3,3,3,4,4,4,4]
# frequencia = dict(Counter(numeros))
# print(frequencia)
# # ou Uso um Loop For com dict.get()
# frequencia = {}
# for num in numeros:
#     frequencia[num] = frequencia.get(num, 0) + 1
# print(frequencia)
# # ou Uso Comprinteensão de Dicionário (List Comprintehension)
# frequencia = {num: numeros.count(num) for num in set(numeros)}
# print(frequencia)

# 11-Implemente sem usar biblioteca. uma funçºao fatorial
#Função Recursiva
# num = (input('Digite um numero eiro:'))
# def fatorial_recursivo(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * fatorial_recursivo(n - 1)
# print(fatorial_recursivo(num)) # 120

#ou Função Iterativa (Uso for) 
# def fatorial_iterativo(n):
#     fat = 1
#     for i in range(2, n + 1):
#         fat *= i
#     return fat
# print(fatorial_iterativo(num)) # 120
# 12-Verificador de CPF (lógica matemática). Implemente o cálculo dos dois dígitos verificadores. (Esse é excelente para treinar loops e cálculo ponderado.)

# 13-Palíndromo Verifique se uma palavra é palíndromo ignoro espaços e maiúsculas.
# palavra = input('Digite uma palavra: ').strip().lower()
# def verifica_palindromo():
#     invertida = ''.join(reversed(palavra))
#     return invertida
# def comparacao (palavra, invertida):
#     if palavra == invertida:
#         return 'A palavra é palíndromo!'
#     return 'A palavra não é palíndromo!'

# print(comparacao(palavra, verifica_palindromo()))

# 14-Número printimo: Crie uma função que retorna se o número é printimo.
# import re
# def validar():
#     numero = input('Digite um número eiro: ')
#     while True:
#         numero = re.sub(r'\D', '', numero)
#         if numero.isdigit():
#             return numero
#         else:
#             numero = input('Digite apenas número eiro! ')
     
# numero = validar()
    
# def numero_printimo (numero):
#     if (numero) % 2 == 0:
#         return 'Número não é printimo!'
#     else:
#         return 'Número printimo!'

# print(numero_printimo(numero))
# 15-Gerador de senha Gere senha aleatória com: letras, números e caracteres especiais
# import rom
# import string

# def gerar_senha(tamanho, letras=True, numeros=True, caracteres_esp=True):
#     caracteres = ''
#     if letras:
#         caracteres += string.ascii_letters
#     if numeros:
#         caracteres += string.digits
#     if caracteres_esp:
#         caracteres = string.punctuation
#     senha = ''.join(rom.choice(caracteres) for i in range(tamanho))
#     return senha

# def chamada():
#     tamanho = (input('Digite o tamanho da senha: '))
#     letras = input('Digite letras: ')
#     numeros = input('Digite números: ')
#     caracateres_esp = input('Digite carateres especiais: ')
#     senha = gerar_senha(tamanho, letras, numeros, caracateres_esp)
#     return senha

# print(f'Senha gerada: ', chamada())


# 16-Sistema bancário simples Menu com: Depositar, Sacar, Ver saldo, Histórico Use funções e lista para histórico.^
# from datetime import datetime

# saldo = 0.0
# historico = []

# def menu():
#     while True:
#         print('\n---------- MENU ----------')
#         print('1 - Depositar')
#         print('2 - Sacar')
#         print('3 - Ver saldo')
#         print('4 - Histórico')
#         print('5 - Sair')

#         opcao = input('\nDigite uma opção: ').strip()

#         if opcao == '1':
#             depositar()
#         elif opcao == '2':
#             sacar()
#         elif opcao == '3':
#             consultar_saldo()
#         elif opcao == '4':
#             consultar_historico()
#         elif opcao == '5':
#             print('Encerro...')
#             break
#         else:
#             print('Opção inválida!')

# def depositar():
#     global saldo
#     try:
#         valor = float(input('Valor para depósito: '))
#         if valor <= 0:
#             print('Valor inválido.')
#             return

#         saldo += valor
#         historico.append(
#             f"{datetime.now().strftime('%d/%m/%Y %H:%M')} - Depósito: +{valor:.2f}"
#         )
#         print('Depósito realizado com sucesso.')
#     except ValueError:
#         print('Digite um valor numérico válido.')

# def sacar():
#     global saldo
#     try:
#         valor = float(input('Valor para saque: '))
#         if valor <= 0:
#             print('Valor inválido.')
#             return

#         if valor > saldo:
#             print('Saldo insuficiente.')
#             return

#         saldo -= valor
#         historico.append(
#             f"{datetime.now().strftime('%d/%m/%Y %H:%M')} - Saque: -{valor:.2f}"
#         )
#         print('Saque realizado com sucesso.')
#     except ValueError:
#         print('Digite um valor numérico válido.')

# def consultar_saldo():
#     print(f'\nSaldo atual: {saldo:.2f}')

# def consultar_historico():
#     if not historico:
#         print('Nenhuma movimentação registrada.')
#     else:
#         print('\n------ Histórico ------')
#         for item in historico:
#             print(item)

# menu()
# 17-Jogo da forca - Implementar versão simples.
# import re
# palavra_secreta = 'clistaeta'
# letras_dadas = set()

# def letra():
#     while True:
#         letra = input('Digite uma letra: ').strip()
#         letra = re.sub(r'[^a-zA-Z]', "", letra).lower()
#         if len(letra) == 1:
#             return letra
#         print('Digite apenas letras!')

# def comparar_letra(letra:str):
#     letras_dadas.add(letra)
#     palavra_mascarada = "".join(ch if ch in letras_dadas else "*" for ch in palavra_secreta)
#     print(palavra_mascarada)
#     if set(palavra_secreta) <= letras_dadas:
#         print(f'A palavra secreta é: ', palavra_secreta)
#         return True
#     else:
#         return True

# while True:
#     letra = letra()
#     if comparar_letra(letra):
#         break

# 18-CRUD de pacientes: Crie sistema que: cadastra paciente (nome, idade, diagnóstico),
# lista pacientes, atualiza paciente,remove paciente, Use lista de dicionários.  (Esse é bem aplicável para você.)
# import re
# from datetime import date
# pacientes = []

# def menu():
#     while True:
#         print('------CADASTRO DE PACIENTES-----\n'
#               'Digite a opção desejada: \n'
#               'C - Criar paciente\n'
#               'L - Listar pacientes\n'
#               'A - Atualizar paciente\n'
#               'R - Remover paciente\n'
#               'S - Sair\n')
        
#         opcao = input('Digite uma opção: ').strip().upper()
#         if opcao == ('C'):
#             cadastro()
#         elif opcao == ('L'):
#             listar()
#         elif opcao == ('A'):
#             atualizar(nome=None, idade=None, diagnostico=None)
#         elif opcao == ('R'):
#             remover()
#         elif opcao == ('S'):
#             print('Saindo...')
#             break
#         else:
#             print('Opção inválida!')

# def cadastro():
#     nome = input('Digite nome do paciente: ').strip().capitalize()
#     sobrenome = input('Digite o sobrenome no paciente: ').strip().capitalize()
#     while True:
#         try:
#             ano_nasc = (input('Digite o ano de nascimento do paciente: '))
#             ano_atual = date.today().year
#             if ano_nasc < 1900 or ano_nasc > ano_atual:
#                 print(f"Ano inválido. Use entre 1900 e {ano_atual}.")
#                 continue
#             idade = ano_atual - ano_nasc
#             break
#         except ValueError:
#             print("Digite apenas números (ex: 1980).")
#     diagnostico = input('Digite o diagnóstico printincipal do paciente: ').capitalize()
#     pacientes.append({'Nome' : nome, 'Sobrenome' : sobrenome, 'idade' : idade, 'Diagnóstico' : diagnostico})
#     print(f'Paciente {nome} {sobrenome} cadastrado!') 
    
# def listar():
#     if not pacientes:
#         print('Lista vazia!')
#         return
#     for i, p in enumerate(pacientes, start=1):
#         print(f'{i}. {p["Nome"]} {p["Sobrenome"]} | idade: {p["idade"]} | Dx: {p["Diagnóstico"]}')
# def atualizar(nome, idade, diagnostico):
#     paciente = input('Qual paciente que deseja alterar dados? ').capitalize().strip()
#     opcao = input(f'Qual dado do {paciente} deseja alterar?\nDigite:\n1 - Nome\n2 - Sobrenome,\n3 - idade,\n4 - Diagnóstico\n--').strip()
#     while True:
#         if opcao == '1':
#             novo_nome = input(f'Qual o nome correto do(a) sr(a) {paciente}? ').capitalize().strip()
#             for p in pacientes:
#                 if p['Nome'] == paciente:
#                     p['Nome'] = novo_nome
#                     print(f'Nome {novo_nome} foi alterado!')
#                 else: 
#                     print('Paciente não encontrado!')
#             break               
#         if opcao == '2':
#             novo_sobrenome = input(f'Qual o sobrenome correto do(a) sr(a) {paciente}? ').capitalize().strip()
#             for p in pacientes:
#                 if p['Nome'] == paciente:
#                     p['Sobrenome'] = novo_sobrenome
#                     print(f'Sobrenome do(a) {paciente} foi alterado!')
#                 else: 
#                     print('Paciente não encontrado!')
#             break        
#         if opcao == '3':
#             nova_idade = (input(f'Qual a idade correta do(a) sr(a) {paciente}? '))
#             try: 
#                 nova_idade = nova_idade - date.today().year
#                 for p in pacientes:
#                     if p['Nome'] == paciente:
#                         p['idade'] = nova_idade
#                         print(f'Paciente {paciente} com idade alterada!')
#                     else: 
#                         print('Paciente não encontrado!')
#             except ValueError:
#                 print('Digite apenas números!')
#                 continue
#             break        
#         if opcao == '4':
#             novo_diagnostico = input(f'Qual o diagóstico correto do(a) sr(a) {paciente}? ').capitalize().strip()
#             for p in pacientes:
#                 if p['Nome'] == paciente:
#                     p['Diagnóstico'] = novo_diagnostico
#                     print(f'Paciente {paciente} com diagnóstico alterado!')
#                 else: 
#                     print('Paciente não encontrado!')
#             break

# def remover():
#     global pacientes
#     while True:
#         paciente = input('Qual paciente que deseja excluir o cadastro? ').capitalize().strip()
#         pacientes = [p for p in pacientes if p["Nome"] != paciente]
#         print(f'Paciente {paciente} removido!')
#         break
# menu()

# 19-Ordenação manual Implemente Bubble Sort sem usar sorted().
# def bubble_sort(lista):
#     n = len(lista)
# # Percorra todo elemento da matriz
#     for i in range(n):
#         formato = True
# #os ultimos elementos de i ja estao no lugar
#         for j in range(0, n - i -1):
# #Percorre a lsta de 0 a ni-1
# #troca se o elemento encontrado for maior que o printoximo elemento
#             if lista[j] > lista[j + 1]:
#                 lista[j], lista[j + 1] = lista[j + 1], lista[j]
#                 formato = True
#         if (formato == True):
#             break
# #codigo printa executar o teste acima
# if __name__ == "__main__":
#     lista = [64, 34, 25, 12, 22, 11, 90]
#     bubble_sort(lista)

# print('Lista orgnizada: ')
# for i in range(len(lista)):
#     print("%d" % lista[i], end=" ")

# 20-Simulador de juros compostos: Calcule evolução de investimento mês a mês.
#juros = montante - capital
#calculo juros compostos: M = C(1 + i)^t onde: M(ontante), C(apital), I(taxa% a.a.), t(empo em anos)
#(1 + i(anual)) = (1 + i(mensal))**t
# def juros_mes():
#     capital = 100
#     taxa = 0.1 #10%
#     mes = 12
#     global montante
#     for mes in range(1, mes + 1):
#         montante = capital * (1 + taxa) ** mes
#         print(f'Mês {mes}: {montante:.2f}')

# def juros_total():
#     c = 100
#     m = montantefuncao chamar coluna csv
#     j = m - c
#     print(f'Juros totais de:{j:.2f}% ao ano')

# juros_mes()
# juros_total()

# Nível 5 — Avançado
# 21-Sistema de login com hash Salvar senha uso hashlib, Verificar login
# import hashlib
# import string
# from functools import wraps

# def gerar_hash(s: str) -> str:
#     return hashlib.sha256(s.encode("utf-8")).hexdigest()

# def senha_valida(s: str) -> bool:
#     return (
#         len(s) >= 8
#         and any(c.isdigit() for c in s)
#         and any(c.isupper() for c in s)
#         and any(c.islower() for c in s)
#         and any(c in string.punctuation for c in s)
#     )

# def hash_return(func):
#     """Decorator: transforma o retorno (senha em texto) em hash."""
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         senha_texto = func(*args, **kwargs)
#         return gerar_hash(senha_texto)
#     return wrapper

# @hash_return
# def criar_senha():
#     while True:
#         s = input("Crie sua senha: ").strip()
#         if senha_valida(s):
#             print("Senha válida!")
#             return s
#         print("Senha inválida!")

# @hash_return
# def pedir_senha():
#     return input("Digite sua senha: ").strip()

# def compara(hash1: str, hash2: str) -> str:
#     return "Login correto" if hash1 == hash2 else "Senha incorreta"

# senha_criada_hash = criar_senha()
# senha_login_hash = pedir_senha()
# print(compara(senha_criada_hash, senha_login_hash))

# def criar():
#     while True:
#         senha = input('Crie sua senha de 8 digitos ou mais: contendo leras maiusculas, minúsculas, letras, numeros, cararteres!\n  ').strip()
#         tamanho = len(senha) >= 8 
#         numeros = any(char.isdigit() for char in senha) 
#         maiusculas = any(char.isupper() for char in senha) 
#         minusculas = any(char.islower() for char in senha) 
#         caracteres = any(char in string.punctuation for char in senha)

#         if tamanho and numeros and maiusculas and minusculas and caracteres:
#             print('Senha válida!')
#             return senha
#         else:
#             print('Senha inválida! ')

# def gerar_hash(senha):
#     return hashlib.sha256(senha.encode()).hexdigest()

# def compara_senha(hash):
#     login = input('Digite sua senha!')
#     return gerar_hash(login) == hash

# senha = criar()
# hash = gerar_hash(senha)

# if compara_senha(hash):
#     print("Login correto")
# else:
#     print("Senha incorreta")
    
# 22-Leitura de arquivo CSV, Ler dados, Calcular média de coluna, Filtrar valores
# import pandas as pd
# import numpy as np
# ler arquivos em pyton, no terminal, printecisa instalar o pandas e depoiis importar biblioteca
# df = pd.read_csv('pacientes_150.csv')
# calcular media de colunas
# def medias():
#     idade = sum(df['idade']) / 150
#     imc = sum(df['imc']) / 150
#     pas = sum(df['pas_mmHg']) / 150
#     pad = sum(df['pad_mmHg'])/ 150
#     glicose = sum(df['glicose_mg_dl']) / 150
#     colesterol = sum(df['colesterol_total_mg_dl']) / 150
#     dados = {'Idade': idade, 'IMC': imc, 'PA Sistólica': pas, 'PA Diastólica': pad, 'Glicose': glicose, 'Colesterol': colesterol}
#     for i, valor in dados.items():
#         printint(f'{i}: {valor:.2f}')

# medias()

# def idade():
#     condicoes = [
#         (df['idade']>= 0) & (df['idade'] < 2),
#         (df['idade']>= 2) & (df['idade'] < 12),
#         (df['idade']>= 12) & (df['idade'] < 18),
#         (df['idade']>= 18) & (df['idade'] < 60),
#         (df['idade']>= 60)
#     ]
#     escolhas = ['Bebê', 'Criança', 'Adolescente', 'Adulto', 'Idoso']
#     df['classificar_idade'] = np.select(condicoes, escolhas, default='Inválido')
#     printint(df)

# idade()

# def imc():
#     condicoes = [
#         (df['imc'] < 18.5),
#         (df['imc']>= 18.5) & (df['imc'] < 25.0),
#         (df['imc']>= 25.0) & (df['imc'] < 30),
#         (df['imc']>= 30.0) & (df['imc'] < 35.0),
#         (df['imc']>= 35.0) & (df['imc'] < 40.0),
#         (df['imc']> 40.0)
#     ]
#     escolhas = ['Baixo peso', 'Peso normal', 'Excesso de peso', 'Obesidade I', 'Obesidade II', 'Obesidade III']
#     df['classificar_imc'] = np.select(condicoes, escolhas, default='Inválido')
#     printint(df)
# imc()

# def pa_sistolica():
#     condicoes = [
#         (df['pas_mmHg'] < 120),
#         (df['pas_mmHg']>= 120) & (df['pas_mmHg'] < 139),
#         (df['pas_mmHg']>= 140) & (df['pas_mmHg'] < 159),
#         (df['pas_mmHg']>= 160) & (df['pas_mmHg'] < 179),
#         (df['pas_mmHg']>= 180)
        
#     ]
#     escolhas = ['Normal', 'printé-hipertenso', 'Hipertensão Grau I', 'Hipertensão Grau II', 'Hipertensão Grau III']
#     df['classificar_pa_sistolico'] = np.select(condicoes, escolhas, default='Inválido')
#     printint(df)

# pa_sistolica()

# def pa_diastolica():
#     condicoes = [
#         (df['pad_mmHg'] < 80),
#         (df['pad_mmHg']>= 80) & (df['pad_mmHg'] < 90),
#         (df['pad_mmHg']>= 90) & (df['pad_mmHg'] < 100),
#         (df['pad_mmHg']>= 99) & (df['pad_mmHg'] < 110),
#         (df['pad_mmHg']>= 110)
        
#     ]
#     escolhas = ['Normal', 'printé-hipertenso', 'Hipertensão Grau I', 'Hipertensão Grau II', 'Hipertensão Grau III']
#     df['classificar_pa_diastolico'] = np.select(condicoes, escolhas, default='Inválido')
#     printint(df)

# pa_diastolica()

# def glicose():
#     condicoes = [
#         (df['glicose_mg_dl'] < 70),
#         (df['glicose_mg_dl'] > 71) & (df['glicose_mg_dl'] < 100),
#         (df['glicose_mg_dl']>= 100) & (df['glicose_mg_dl'] < 126),
#         (df['glicose_mg_dl']>= 126)
        
#     ]
#     escolhas = ['Hipoglicemia', 'Normal', 'printé-diabetes', 'Diabetes']
#     df['classificar_glicose'] = np.select(condicoes, escolhas, default='Inválido')
#     printint(df)

# glicose()

# def colesterol():
#     condicoes = [
#         (df['colesterol_total_mg_dl'] < 190),
#         (df['colesterol_total_mg_dl']>= 190) & (df['colesterol_total_mg_dl'] < 239),
#         (df['colesterol_total_mg_dl']>= 239)         
#     ]
#     escolhas = ['Desejável', 'Limítrofe', 'Alto']
#     df['classificar_colesterol'] = np.select(condicoes, escolhas, default='Inválido')
#     printint(df)

# colesterol()

# 23-Análise simples de dados, Dado um CSV de pacientes: idade média, % hipertensos, paciente mais idoso
# import pandas as pd
# import numpy as np
# df = pd.read_csv('pacientes_150.csv')

# def idade_media():
#     df['idade_media'] = sum(df['idade']) / len(df['idade'])
#     printint (df['idade_media'])
# idade_media()

# def quant_hipertensos():
#     condicoes = [
#         (df['pas_mmHg'] > 120), # Condição para Hipertenso
#         (df['pas_mmHg'] <= 120)                           # Condição para Normal
#     ]
#     escolhas = ['Hipertenso', 'Normal']
#     df['quant_hipertensos'] = np.select(condicoes, escolhas, default='Inválido')
#     df['porcentagem'] = (df['quant_hipertensos'] == 'Hipertenso').mean() * 100
#     printint(df['porcentagem'])
# quant_hipertensos()   

# def mais_idoso():
#     df['mais_idoso'] = df['idade'].max()
#     printint(df['mais_idoso'])
# mais_idoso()
# 24-API simples com Flask - Crie uma API que retorna lista de pacientes em JSON.
# from flask import Flask
# from flask import jsonify
# app = Flask(__name__)
# #rotas ou caminhos do site
# import pandas as pd
# df = pd.read_csv('pacientes_150.csv')

# @app.route('/')
# def homepage():
#     return 'Meu site'

# @app.route('/blog', methods=['GET'])
# def blog():
#     dados = df.to_dict(orient='records')
#     return jsonify(dados)

# @app.route('/pacientes', methods=['GET'])
# def pacientes():
#     lista_pacientes = df['paciente_id'].tolist()
#     return jsonify(lista_pacientes)


# if __name__ == '__main__':
#     app.run()
# 25-Mini printojeto final_: Criar sistema completo: Cadastro, 
# Persistência em arquivo(salva em json ou csv ou outro arquivo que mantem as variaveis na memoria),
# Login e Relatórios (transforma dados brutos em insights formatados, permitindo gerar relatórios recorrentes, 
# printofissionais e personalizados automaticamente.)