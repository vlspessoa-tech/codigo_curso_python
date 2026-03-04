import re
from datetime import date
pacientes = []

def menu():
    while True:
        print('------CADASTRO DE PACIENTES-----\n'
              'Digite a opção desejada: \n'
              'C - Criar paciente\n'
              'L - Listar pacientes\n'
              'A - Atualizar paciente\n'
              'R - Remover paciente\n'
              'S - Sair\n')
        
        opcao = input('Digite uma opção: ').strip().upper()
        if opcao == ('C'):
            cadastro()
        elif opcao == ('L'):
            listar()
        elif opcao == ('A'):
            atualizar(nome=None, idade=None, diagnostico=None)
        elif opcao == ('R'):
            remover()
        elif opcao == ('S'):
            print('Saindo...')
            break
        else:
            print('Opção inválida!')

def cadastro():
    nome = input('Digite nome do paciente: ').strip().capitalize()
    sobrenome = input('Digite o sobrenome no paciente: ').strip().capitalize()
    while True:
        try:
            ano_nasc = (input('Digite o ano de nascimento do paciente: '))
            ano_atual = date.today().year
            if ano_nasc < 1900 or ano_nasc > ano_atual:
                print(f"Ano inválido. Use entre 1900 e {ano_atual}.")
                continue
            idade = ano_atual - ano_nasc
            break
        except ValueError:
            print("Digite apenas números (ex: 1980).")
    diagnostico = input('Digite o diagnóstico principal do paciente: ').capitalize()
    pacientes.append({'Nome' : nome, 'Sobrenome' : sobrenome, 'idade' : idade, 'Diagnóstico' : diagnostico})
    print(f'Paciente {nome} {sobrenome} cadastrado!') 
    
def listar():
    if not pacientes:
        print('Lista vazia!')
        return
    for i, p in enumerate(pacientes, start=1):
        print(f'{i}. {p["Nome"]} {p["Sobrenome"]} | idade: {p["idade"]} | Dx: {p["Diagnóstico"]}')

def atualizar(nome, idade, diagnostico):
    paciente = input('Qual paciente que deseja alterar dados? ').capitalize().strip()
    opcao = input(f'Qual dado do {paciente} deseja alterar?\nDigite:\n1 - Nome\n2 - Sobrenome,\n3 - idade,\n4 - Diagnóstico\n--').strip()
    while True:
        if opcao == '1':
            novo_nome = input(f'Qual o nome correto do(a) sr(a) {paciente}? ').capitalize().strip()
            for p in pacientes:
                if p['Nome'] == paciente:
                    p['Nome'] = novo_nome
                    print(f'Nome {novo_nome} foi alterado!')
                else: 
                    print('Paciente não encontrado!')
            break               
        if opcao == '2':
            novo_sobrenome = input(f'Qual o sobrenome correto do(a) sr(a) {paciente}? ').capitalize().strip()
            for p in pacientes:
                if p['Nome'] == paciente:
                    p['Sobrenome'] = novo_sobrenome
                    print(f'Sobrenome do(a) {paciente} foi alterado!')
                else: 
                    print('Paciente não encontrado!')
            break        
        if opcao == '3':
            nova_idade = (input(f'Qual a idade correta do(a) sr(a) {paciente}? '))
            try: 
                nova_idade = nova_idade - date.today().year
                for p in pacientes:
                    if p['Nome'] == paciente:
                        p['idade'] = nova_idade
                        print(f'Paciente {paciente} com idade alterada!')
                    else: 
                        print('Paciente não encontrado!')
            except ValueError:
                print('Digite apenas números!')
                continue
            break        
        if opcao == '4':
            novo_diagnostico = input(f'Qual o diagóstico correto do(a) sr(a) {paciente}? ').capitalize().strip()
            for p in pacientes:
                if p['Nome'] == paciente:
                    p['Diagnóstico'] = novo_diagnostico
                    print(f'Paciente {paciente} com diagnóstico alterado!')
                else: 
                    print('Paciente não encontrado!')
            break

def remover():
    global pacientes
    while True:
        paciente = input('Qual paciente que deseja excluir o cadastro? ').capitalize().strip()
        pacientes = [p for p in pacientes if p["Nome"] != paciente]
        print(f'Paciente {paciente} removido!')
        break
    
